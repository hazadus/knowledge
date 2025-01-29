To properly call a function from one service in another service in Go, follow these steps:

### 1. **Define Services with Dependency Injection**

Each service should accept its dependencies explicitly through its constructor. This promotes loose coupling and testability.

**Example: ServiceB**
```go
package serviceb

// ServiceB provides specific functionality.
type ServiceB struct {
    // Dependencies (e.g., databases, logs)
}

// NewServiceB creates a new instance of ServiceB.
func NewServiceB() *ServiceB {
    return &ServiceB{}
}

// DoSomething is an exported method (note the uppercase "D").
func (s *ServiceB) DoSomething() error {
    // Business logic
    return nil
}
```

### 2. **Define Interfaces for Dependencies**

In the calling service's package, define an interface that describes the methods you need from the dependency. This decouples your service from concrete implementations.

**Example: ServiceA with Interface**
```go
package servicea

// ServiceBInterface defines the methods ServiceA needs from ServiceB.
type ServiceBInterface interface {
    DoSomething() error
}

// ServiceA depends on ServiceBInterface.
type ServiceA struct {
    serviceB ServiceBInterface
}

// NewServiceA injects a ServiceBInterface dependency.
func NewServiceA(sb ServiceBInterface) *ServiceA {
    return &ServiceA{
        serviceB: sb,
    }
}

// SomeMethod in ServiceA uses ServiceB's method.
func (s *ServiceA) SomeMethod() error {
    return s.serviceB.DoSomething() // Call via interface
}
```

### 3. **Wire Dependencies in Main**

Initialize services and inject dependencies at the application entry point (e.g., `main` function).

```go
package main

import (
    "yourproject/servicea"
    "yourproject/serviceb"
)

func main() {
    // Initialize ServiceB
    sb := serviceb.NewServiceB()

    // Inject ServiceB into ServiceA
    sa := servicea.NewServiceA(sb)

    // Use ServiceA
    sa.SomeMethod()
}
```

### Key Considerations:

- **Interfaces for Decoupling**: By depending on interfaces, `ServiceA` isn't tied to `ServiceB`'s concrete type, making it easy to swap implementations (e.g., mocks for testing).
- **Exported Methods**: Methods called across packages must be exported (start with a capital letter).
- **Avoid Circular Dependencies**: Structure your code to prevent services from depending on each other cyclically. Use interfaces or intermediate services if needed.
- **Testing**: Mock `ServiceBInterface` in tests for `ServiceA` to isolate behavior.

### Testing Example:

```go
package servicea_test

import (
    "testing"
    "yourproject/servicea"
)

// MockServiceB implements ServiceBInterface for testing.
type MockServiceB struct{}

func (m *MockServiceB) DoSomething() error {
    return nil // Mock behavior
}

func TestSomeMethod(t *testing.T) {
    mockSB := &MockServiceB{}
    sa := servicea.NewServiceA(mockSB)
    
    if err := sa.SomeMethod(); err != nil {
        t.Errorf("Unexpected error: %v", err)
    }
}
```

By following these practices, you ensure clean, maintainable, and testable service interactions in Go.

----

## References

- DeepSeek 

----
📂 [[Best Practices]] | Последнее изменение: 29.01.2025 14:16