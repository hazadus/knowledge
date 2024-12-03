Иточник: https://www.alexedwards.net/blog/understanding-mutexes

----
## Creating a Basic Mutex

Let's create some toy code to mimic the bank balance example:

```go
import (
	"fmt"
)

var myBalance = &balance{amount: 5000, currency: "GBP"}

type balance struct {
	amount   int
	currency string
}

func (b *balance) Add(i int) {
	// This is racy
	b.amount += i
}

func (b *balance) Get() string {
	// This is racy
	return fmt.Sprintf("%d %s", b.amount, b.currency)
}
```

We know that if there are multiple goroutines using this code and calling `myBalance.Add() `and `myBalance.Get()` frequently enough, then at some point a data race is likely to occur.

One way we could prevent the data race is to ensure that if one goroutine is using the myBalance variable, then all other goroutines are prevented (or mutually excluded) from using it at the same time.

We can do this by creating a `sync.Mutex` and setting a lock around particular lines of code with it. While one goroutine holds the lock, all other goroutines are prevented from executing any lines of code protected by the same mutex, and are forced to wait until the lock is yielded before they can proceed.

In practice, it's simpler than it sounds:

```go
import (
	"fmt"
	"sync"
)

var mu sync.Mutex

var myBalance = &balance{amount: 5000, currency: "GBP"}

type balance struct {
	amount   int
	currency string
}

func (b *balance) Add(i int) {
	mu.Lock()
	b.amount += i
	mu.Unlock()
}

func (b *balance) Get() string {
	mu.Lock()
	amt := b.amount
	cur := b.currency
	mu.Unlock()

	return fmt.Sprintf("%d %s", amt, cur)
}
```

Here we've created a new mutex and assigned it to the variable mu. We then use `mu.Lock()` to create a lock immediately before both racy parts of the code, and `mu.Unlock()` to yield the lock immediately after.

There's a couple of things to note:

- The same mutex variable can be used in multiple places throughout your code. So long as it's the same mutex (in our case mu) then none of the chunks of code protected by it can be executed at the same time.
- Holding a mutex lock doesn't 'protect' a memory location from being read or updated. A non-mutex-locked line of code could still access it at any time and create a race condition. Therefore you need to be careful to make sure all points in your code which are potentially racy are protected by the same mutex.

Let's tidy up the example a bit:

```go
import (
	"fmt"
	"sync"
)

var myBalance = &balance{amount: 5000, currency: "GBP"}

type balance struct {
	amount   int
	currency string
	mu       sync.Mutex
}

func (b *balance) Add(i int) {
	b.mu.Lock()
	b.amount += i
	b.mu.Unlock()
}

func (b *balance) Get() string {
	b.mu.Lock()
	defer b.mu.Unlock()

	return fmt.Sprintf("%d %s", b.amount, b.currency)
}
```

So what's changed here?

Because our mutex is only being used in the context of a balance object, it makes sense to embed it in the balance struct (an idea borrowed from Andrew Gerrard's excellent 10 things you (probably) don't know about Go slideshow). If you look at a larger codebase with lots of mutexes, like Go's HTTP Server, you can see how this approach helps to keep locking rules nice and clear.

We've also made use of the defer statement in the `Get()` method, which ensures that the mutex gets unlocked immediately before the function executing it returns. This is common practice for functions that contain multiple return statements, or where the return statement itself is racy (like in our example).

## Read Write Mutexes

It is important to emphasize that data races aren't a concern if the only thing you are doing concurrently is reading the shared data.

In our bank balance example, having a full mutex lock on the `Get()` function isn't strictly necessary. It would be OK for us to have multiple reads of myBalance happening at the same time, so long as nothing is being written.

We can achieve this using `sync.RWMutex`, a reader/writer mutual exclusion lock which allows any number of readers to hold the lock or one writer. This tends to be more efficient than using a full mutex in situations where you have a high ratio of reads to writes.

Reader locks can be opened and closed with the `RLock()` and `RUnlock()` methods like so:

```go
import (
	"fmt"
	"sync"
)

var myBalance = &balance{amount: 5000, currency: "GBP"}

type balance struct {
	amount   int
	currency string
	mu       sync.RWMutex
}

func (b *balance) Add(i int) {
	b.mu.Lock()
	b.amount += i
	b.mu.Unlock()
}

func (b *balance) Get() string {
	b.mu.RLock()
	defer b.mu.RUnlock()

	return fmt.Sprintf("%d %s", b.amount, b.currency)
}
```



----
📂 [[Go]] | Последнее изменение: 03.12.2024 10:35