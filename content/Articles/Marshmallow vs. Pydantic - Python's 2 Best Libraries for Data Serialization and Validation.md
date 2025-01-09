# Marshmallow vs. Pydantic - Python's 2 Best Libraries for Data Serialization and Validation

![rw-book-cover](https://www.augmentedmind.de/wp-content/uploads/2020/10/marshmallow-vs-pydantic-feature.png)

## Metadata
- Author: [[Denis 2022-04-01 at 2:26 AM]]
- Full Title: Marshmallow vs. Pydantic - Python's 2 Best Libraries for Data Serialization and Validation
- Category: #articles
- Document Tags: [[marshmallow]] [[pydantic]] 
- Summary: An introduction and comparison of the Python libraries marshmallow vs. pydantic, which (de-) serialize data from and to Python objects and validate your data.
- URL: https://www.augmentedmind.de/2020/10/25/marshmallow-vs-pydantic-python/

## Highlights
- **Pydantic is not a direct competitor to marshmallow**, because the goal of Pydantic is to add validation to (schema-)objects _throughout their lifetime_. **Pydantic basically applies dynamic type checking at run-time, e.g. when instantiating an object, at configurable levels.** In contrast, **marshmallow only applies type checking (including data validation) _at specific points_**, whenever you call `schema.load()`, `schema.dump()` or `schema.validate()`. ([View Highlight](https://read.readwise.io/read/01jdc0fqqxn7t57g0scew3erc2))

- **Be sure to closely study Pydantic’s manual, because there are some interesting caveats. For instance, Pydantic is actually not that pedantic when it comes to type matching. The call `BookModel(title=1337, isbn=1234)` works** (no validation error is raised), **even though `1337` is a number and not a string**. Pydantic _converts_ provided data where no (or little) loss would occur. **To avoid this behavior, you have to annotate the attributes using _strict_ types**, e.g. `pydantic.StrictStr` instead of `str`, as documented [here](https://pydantic-docs.helpmanual.io/usage/types/#strict-types). ([View Highlight](https://read.readwise.io/read/01jdc0fqy7t5hfcqsbtabazqqg))

- If all you need is serialization and deserialization at specific points in your application, I recommend marshmallow. Pydantic is a good choice if you want type safety throughout the whole lifetime of your objects at run-time, better interoperability with standards, or require very good run-time performance. ([View Highlight](https://read.readwise.io/read/01jdc0fr3wp22tcmqyznt84caz))

- **If you use marshmallow, you need to call a schema’s `dump(obj)` method**. Note that this call will validate your data again, which may raise unexpected errors for objects you created _manually_ (using their normal constructor, not using `schema.load()`), with actually invalid data. **With Pydantic you call the `o.dict()` method on a model object `o` which inherits from `pydantic.BaseModel`, to get a nested `dict`. Note that this `dict` might still contain non-primitive types, such as `datetime` objects, which many converters** (including Python’s `json` module) **cannot handle. Consider using `o.json()` instead.** ([View Highlight](https://read.readwise.io/read/01jdc0fr9p8jhk1x10advad5xs))

- Fortunately, **both marshmallow and Pydantic offer support to actually rename fields dynamically**. See [here](https://marshmallow.readthedocs.io/en/latest/examples.html#inflection-camel-casing-keys) for marshmallow and [here](https://pydantic-docs.helpmanual.io/usage/model%5Fconfig/#alias-generator) for Pydantic. In case of Pydantic, the linked docs just cover _de_serialization – for _serialization_ you simply need to call `o.dict(by_alias=True)` instead of `o.dict()`. ([View Highlight](https://read.readwise.io/read/01jdc0frfyah6t0kxpacm3earg))



----
📂 [[Articles]] | Последнее изменение: 23.11.2024 16:34