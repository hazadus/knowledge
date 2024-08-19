📂 [[Tooling]]

----
### `npm install`
Get help: `npm install help`
Basic options:
```Bash
npm install saves any specified packages into dependencies by default. Additionally, you can control where and how they get saved with some additional flags:
           •   -P, --save-prod: Package will appear in your dependencies. This is the default unless -D or -O are present.
           •   -D, --save-dev: Package will appear in your devDependencies.
           •   -O, --save-optional: Package will appear in your optionalDependencies.
           •   --no-save: Prevents saving to dependencies.
       When using any of the above options to save dependencies to your package.json, there are two additional, optional flags:
           •   -E, --save-exact: Saved dependencies will be configured with an exact version rather than using npm's default semver range operator.
           •   -B, --save-bundle: Saved dependencies will also be added to your bundleDependencies list.
```

----
📂 [[Tooling]] | Последнее изменение: 07.02.2024 20:16