# ORM

ORM – это библиотека, которая связывает БД с концепциями объектно-ориентированных языков. Избавляет от работы с чистым SQL. Меньше кода, проект легче сопровождать.

Из минусов использования ORM: снижение скорости работы с БД, затраченное время на освоение ORM, потеря контроля над SQL-запросами.
# Documentation and Tutorials
- [Flask-SQLAlchemy - Flask-SQLAlchemy Documentation (2.x) ](https://flask-sqlalchemy.palletsprojects.com/en/2.x/index.html)  
- [How To Query Tables and Paginate Data in Flask-SQLAlchemy | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-query-tables-and-paginate-data-in-flask-sqlalchemy)  
- [SQLAlchemy 1.4 Documentation](https://docs.sqlalchemy.org/en/14/)  
# Code snippets
## **Querying Records**
```Python
posts = Posts.query.order_by(Posts.date_posted.desc())  # order 'clause', nb desc
```
### Retrieving All Records
```Python
all_employees = Employee.query.all()
print(all_employees)
```
### **Retrieving the First Record**
```Python
first_employee = Employee.query.first()
print(first_employee)
```
### **Retrieving a Record by ID**
```Python
employee5 = Employee.query.get(5)
employee3 = Employee.query.get(3)
print(f'{employee5} | ID: {employee5.id}')
print(f'{employee3} | ID: {employee3.id}')
```
### **Retrieving a Record or Multiple Records by a Column Value**
```Python
employee = Employee.query.filter_by(age=52).first()
print(employee)
```
### **Equals**
```Python
mary = Employee.query.filter(Employee.firstname == 'Mary').all()
print(mary)
```
### **Not Equals**
```Python
out_of_office_employees = Employee.query.filter(Employee.active != True).all()
print(out_of_office_employees)
```
### **Less Than / Greater Than**
```Python
employees_under_32 = Employee.query.filter(Employee.age < 32).all()
for employee in employees_under_32:
    print(employee.firstname, employee.lastname)
    print('Age: ', employee.age)
    print('----')
```
```Python
employees_32_or_younger = Employee.query.filter(Employee.age <=32).all()
for employee in employees_32_or_younger:
    print(employee.firstname, employee.lastname)
    print('Age: ', employee.age)
    print('----')
```
Greater than is similar, just use > / ≥ signs.
### In (iterable)
SQLAlchemy also provides a way to get records where a column’s value matches a value from a given list of values using the `in_()` method on the column like so; Here, you use a condition with the syntax `Model.column.in_(iterable)`, where `iterable` is any type of [object you can iterate through](https://docs.python.org/3.8/glossary.html#term-iterable).
```Python
names = ['Mary', 'Alex', 'Emily']
employees = Employee.query.filter(Employee.firstname.in_(names)).all()
print(employees)
```
For another example, you can use the `range()`Python function to get employees from a certain age range. The following query gets all the employees that are in their thirties.
```Python
employees_in_30s = Employee.query.filter(Employee.age.in_(range(30, 40))).all()
for employee in employees_in_30s:
    print(employee.firstname, employee.lastname)
    print('Age: ', employee.age)
    print('----')
```
```Python
post = Posts.query.filter(Posts.slug == post_slug).first_or_404()
similar_posts = Posts.query.join(Tags.posts).filter(Tags.id.in_(tag.id for tag in post.tags)).all()
```
### Not In
```Python
names = ['Mary', 'Alex', 'Emily']
employees = Employee.query.filter(Employee.firstname.not_in(names)).all()
print(employees)
```
### And
```Python
active_and_32 = Employee.query.filter(db.and_(Employee.age == 32,
                                      Employee.active == True)).all()
print(active_and_32)
```
### And + Date
```Python
from datetime import date
hired_in_2019 = Employee.query.filter(
				db.and_(Employee.hire_date >= date(year=2019, month=1, day=1), 
				Employee.hire_date < date(year=2020, month=1, day=1))).all()
for employee in hired_in_2019:
    print(employee, ' | Hired: ', employee.hire_date)
```
### Or
```Python
employees_32_or_52 = Employee.query.filter(
					db.or_(Employee.age == 32, Employee.age == 52)).all()
for e in employees_32_or_52:
    print(e, '| Age:', e.age)
```
```Python
employees = Employee.query.filter(
						db.or_(Employee.firstname.startswith('M'), 
										Employee.lastname.endswith('e'))).all()
for e in employees:
    print(e)
```
## **Ordering, Limiting, and Counting Results**
### **Ordering Results**
```Python
employees = Employee.query.order_by(Employee.firstname).all()
print(employees)
```
```Python
em_ordered_by_hire_date_desc = Employee.query.order_by(
					Employee.hire_date.desc()).all()
for employee in em_ordered_by_hire_date_desc:
    print(employee.firstname, employee.lastname, employee.hire_date)
```
You can also combine the `order_by()`method with the `filter()`method to order filtered results. The following example gets all the employees hired in 2021 and orders them by age:
```Python
from datetime import date
hired_in_2021 = Employee.query.filter(
		db.and_(Employee.hire_date >= date(year=2021, month=1, day=1), 
		Employee.hire_date < date(year=2022, month=1, day=1))).order_by(Employee.age).all()
for employee in hired_in_2021:
    print(employee.firstname, employee.lastname,
          employee.hire_date, '| Age', employee.age)
```
### **Limiting Results**
```Python
employees = Employee.query.limit(3).all()
print(employees)
```
You can use `limit()`with other methods, such as `filter`and `order_by`. For example, you can get the last two employees hired in 2021 using the `limit()`method like so:
```Python
from datetime import date
hired_in_2021 = Employee.query.filter(
	db.and_(Employee.hire_date >= date(year=2021, month=1, day=1), 
	Employee.hire_date < date(year=2022, month=1, day=1))).order_by(
			Employee.age).limit(2).all()
for employee in hired_in_2021:
    print(employee.firstname, employee.lastname,
          employee.hire_date, '| Age', employee.age)
```
### **Counting Results**
```Python
employee_count = Employee.query.count()
print(employee_count)
```
You can combine the `count()`method with other query methods similar to `limit()`. For example, to get the number of employees hired in 2021:
```Python
from datetime import date
hired_in_2021_count = Employee.query.filter(
		db.and_(Employee.hire_date >= date(year=2021, month=1, day=1), 
		Employee.hire_date < date(year=2022, month=1, day=1))).order_by(
				Employee.age).count()
print(hired_in_2021_count)
```