- **Keep Headings Simple**
  While it might be tempting to include information like dates or codenames in a release's top-level heading, avoid it. Include only the version string from your package manifest. This makes for easier visual scanning and deterministic markdown anchors.

- **Note the Date**
  Knowing how old a specific version is provides useful context about the release. For instance, it was released before a certain module convention was commonplace, or before certain language features were available.
  Even if you use a versioning scheme that [includes the date](https://calver.org/), note the release date explicitly at the top of each release section. The exact syntax doesn't matter, but ISO format is recommended.

- **Be Iconic**
  Changelogs can get lengthy, making them hard for readers to parse when skimming. Adding emoji to highlight certain sections or items helps readers visually identify different sections.

- **Focus on Impact**
  Changelog items should focus on what changed, not why. This keeps each line focused and factual, ideal for a busy reader. If they're curious they can click through to the commit / pull request for the context behind the change.

- **Give (Some) Context**
  Though the actual log of changes should be bullet points that link to PRs/commits, feel free to include text that gives context around the release. This is a good place to highlight top-level features, link to migration resources, or talk about future plans.

- **Don't Include Everything**
  There are many commits that aren't relevant to users of your package; things like docs updates, repo configuration changes, formatting, or misc typos. While these contributions are worth highlighting, they don't belong in a changelog.
  Instead, focus on changes that impact the way your library is used: features, breaking changes, and bug fixes.

## Example

```json
# Changelog

This project adheres to [SemVer](https://semver.org/); the public API surface will not change outside major releases. The public API includes:

- all documented functions
- supported language versions
- import paths.

## 2.0.0

_released `2024-08-07`_

This is our big async release! We've made a host of changes ensuring the package spends less time blocking the main thread. You can read about it in our [blog post](https://example.com/blog/async)

- ❗**Breaking**: Remove function `do_the_thing()`. It's replaced by `do_thing_better()` (https://github.com/example/repo/pull/123)
- ❗**Breaking**: Drop support for Florp versions before 3.0 (https://github.com/example/repo/pull/456)
- Add new optional parameters to `has_some_args()` (https://github.com/example/repo/pull/789):
  - `explode` (boolean; defaults to `false`) triggers self-destruct after calling
  - `countdown` (int, seconds; defaults to `300`) controls the default timer
- add new function `very_cool_func()` to generate cool things (https://github.com/example/repo/pull/098)

## 1.3.5

_released `2024-07-01`_

- ⚠️ The `do_the_thing()` function is deprecated and will be removed in `2.0.0`. Use `do_thing_better()` instead (https://github.com/example/repo/pull/765)
- ⚠️ Fixed a bug in `qwer()` where errors weren't always thrown correctly. If you weren't validating input before, errors may start being thrown in places they weren't (https://github.com/example/repo/pull/432)
- added `some_neat_feature()` (https://github.com/example/repo/pull/101)

## 1.3.4

_released `2024-06-12`_

- update error text (https://github.com/example/repo/pull/234)
- improve performance of `was_slow_func()` (https://github.com/example/repo/pull/567)
```

----
## References

- [[Effective Changelogs  xavd.id]]
	- https://xavd.id/blog/post/effective-changelogs/


----
📂 [[Misc]] | Последнее изменение: 21.01.2025 09:01