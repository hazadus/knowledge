📂 [[Tooling]]
Keywords: JSON, CLI, tool, Linux, MacOS

----
[jq](https://stedolan.github.io/jq/?ref=its-foss) is a command line JSON processor. You can use it to slice, filter, map and transform structured data.
## Installation

```bash
brew install jq
apt install jq
```
## Usage

```bash
cat sample.json | jq
```

## Queries

Ref: https://gist.github.com/ipbastola/2c955d8bf2e96f9b1077b15f995bdae3

```bash
cat stdout.log | jq -c '. | select( .status == 400)' | jq
cat logs/backend.log | jq -c '. | select( .level == "error")' | jq
```

----
📂 [[Tooling]] | Последнее изменение: 13.02.2025 14:19