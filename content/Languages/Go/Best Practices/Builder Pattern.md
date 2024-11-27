**Источник**: рассылка Jon Calhoun (calhoun.io)

----
The builder pattern is a technique where a developer uses a "builder" to construct an object. The end result could be anything - a string, a struct instance, or even a closure - but it is built using a builder. More often than not a builder is used because the object being created is complex and needs to be constructed in multiple steps, so the builder helps isolate each step and prevent bugs.

This is much easier to understand with an example, so imagine you have an Employee struct:

```go
type Employee struct {
  Name      string
  Role      string
  MinSalary int
  MaxSalary int
}
```

Under most circumstances a developer would create an instance of the Employee struct in their code and assign a value to each of these fields, but in some circumstances you might want to do more than that. For instance, you might decide that when the Role field is set that you can also assign the min and max salary fields based on the role. This could be achieved using a builder.

```go
type Builder struct {
  e Employee
}

func (b *Builder) Build() Employee {
  return b.e
}

func (b *Builder) Name(name string) *Builder {
  [b.e.Name](http://b.e.name/) = name
  return b
}

func (b *Builder) Role(role string) *Builder {
  if role == "manager" {
    b.e.MinSalary = 20000
    b.e.MaxSalary = 60000
  }
  b.e.Role = role
  return b
}
```

Now when we are constructing an Employee we can use the builder to ensure that the min and max salary get set when we set the Role field. We could even add validation in and verify that the role is a valid one - though at that point we would need to also return an error.

Below we can see how this builder might be used:

```go
b := &Builder{}
employee := b.
  Name("Michael Scott").
  Role("manager").
  Build()
fmt.Println(employee)
// {Michael Scott manager 20000 60000}
```

_On the Go Playground:_ [_https://play.golang.org/p/2Lo0rIt80Yx_](https://click.convertkit-mail.com/v8ukomwl2eamuoleppiwuvnkpllls9/8ghqhoh54dnq77hk/aHR0cHM6Ly9wbGF5LmdvbGFuZy5vcmcvcC8yTG8wckl0ODBZeA==)_​_

This is a more basic example so the builder pattern might feel like overkill, but much more complex scenarios exist where the builder pattern is incredibly helpful. For instance, constructing SQL queries can become complex and we might need to handle conditional queries. In this case a builder can simplify things a bit.

One such library is [squirrel](https://click.convertkit-mail.com/v8ukomwl2eamuoleppiwuvnkpllls9/vqh3hrhk50req6bg/aHR0cHM6Ly9naXRodWIuY29tL01hc3Rlcm1pbmRzL3NxdWlycmVs). We are going to look at a few examples from the squirrel docs below, starting with a basic example of how squirrel can be used to generate the SQL query string we might use with the standard library's database/sql package and then moving to slightly more complex examples.

```go
users := sq.Select("*").From("users").Join("emails USING (email_id)")
sql, args, err := users.ToSql() 
// sql == "SELECT * FROM users JOIN emails USING (email_id)"

active := users.Where(sq.Eq{"deleted_at": nil})
sql, args, err := active.ToSql()
// sql == "SELECT * FROM users JOIN emails USING (email_id) WHERE deleted_at IS NULL"
```

Next we will look at an example of a conditional query, which is as simple as adding an if statement and adding the conditional query.

```go
if len(q) > 0 {
  users = users.Where("name LIKE ?", fmt.Sprint("%", q, "%"))
}
```

Notice how we assign the result of the users.Where function call to the users variable, allowing us to retain this new build step. Now whenever we call users.ToSql() it will have the Where clause here only if the if statement was true.

Builders can even be found in Go's standard library. Both of the template packages have a Template type that uses the builder pattern:

- ​[text/template](https://click.convertkit-mail.com/v8ukomwl2eamuoleppiwuvnkpllls9/l2hehmhkg276dgh6/aHR0cHM6Ly9nb2xhbmcub3JnL3BrZy90ZXh0L3RlbXBsYXRlLyUyMA==)​
- ​[html/template](https://click.convertkit-mail.com/v8ukomwl2eamuoleppiwuvnkpllls9/m2h7h5hnr5zmxkcm/aHR0cHM6Ly9nb2xhbmcub3JnL3BrZy9odG1sL3RlbXBsYXRlLw==)​

In both of these packages the [Template](https://click.convertkit-mail.com/v8ukomwl2eamuoleppiwuvnkpllls9/dpheh0h736n8x4am/aHR0cHM6Ly9nb2xhbmcub3JnL3BrZy9odG1sL3RlbXBsYXRlLyNUZW1wbGF0ZQ==) type is a builder of itself. By that I mean calling almost any function on the Template type will return a new, modified instance of the Template.

```go
tmpl, err := template.New("titleTest").
  Funcs(funcMap).
  Delims("[[", "]]").
  Parse(templateText)
```

Both [Funcs](https://click.convertkit-mail.com/v8ukomwl2eamuoleppiwuvnkpllls9/e0hph7hnxvoqzla8/aHR0cHM6Ly9nb2xhbmcub3JnL3BrZy9odG1sL3RlbXBsYXRlLyNUZW1wbGF0ZS5GdW5jcw==) and [Delims](https://click.convertkit-mail.com/v8ukomwl2eamuoleppiwuvnkpllls9/7qh7h8h4gl5we8tz/aHR0cHM6Ly9nb2xhbmcub3JnL3BrZy9odG1sL3RlbXBsYXRlLyNUZW1wbGF0ZS5EZWxpbXM=) return a *[Template](https://click.convertkit-mail.com/v8ukomwl2eamuoleppiwuvnkpllls9/dpheh0h736n8x4am/aHR0cHM6Ly9nb2xhbmcub3JnL3BrZy9odG1sL3RlbXBsYXRlLyNUZW1wbGF0ZQ==), and [Parse](https://click.convertkit-mail.com/v8ukomwl2eamuoleppiwuvnkpllls9/owhkhqh8z9dgeltv/aHR0cHM6Ly9nb2xhbmcub3JnL3BrZy9odG1sL3RlbXBsYXRlLyNUZW1wbGF0ZS5QYXJzZQ==) returns both a *Template and an error kinda like our Role example in the employee builder would have if we validated the role.

To sum up - the builder pattern in Go usually involves chaining functions on a single type as we "build" the end result. It is used to build complex objects, and can be found in quite a few libraries.

----
📂 [[Go]] #go


----
📂 [[Best Practices]] | Последнее изменение: 27.11.2024 14:32