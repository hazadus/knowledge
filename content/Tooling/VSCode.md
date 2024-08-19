📂 [[Tooling]]

----
## Shortcuts

https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf

⌘P – Recent Files
^Tab – Cycle Editor Tabs
⌘⇧P – Command Palette
⇧⌘O – Go To Symbol
⌘] / ⌘[ – Indent/outdent Line
^~ – Terminal
⌘B – Toggle Sidebar
F2 – Rename Variable
⌘\ – Split Current Editor
⌘D – Select Current Word
⇧⌥O – Organize Imports

## Create Snippets

> [!info]  
>  
> [https://code.visualstudio.com/docs/editor/userdefinedsnippets#_create-your-own-snippets](https://code.visualstudio.com/docs/editor/userdefinedsnippets#_create-your-own-snippets)  
```JavaScript
// Ref: https://github.com/joschan21/breadit
// vscode settings -> user snippets -> typescriptreact.json
"Typescript React Function Component": {
    "prefix": "fc",
    "body": [
      "import { FC } from 'react'",
      "",
      "interface ${TM_FILENAME_BASE}Props {",
      "  $1",
      "}",
      "",
      "const $TM_FILENAME_BASE: FC<${TM_FILENAME_BASE}Props> = ({$2}) => {",
      "  return <div>$TM_FILENAME_BASE</div>",
      "}",
      "",
      "export default $TM_FILENAME_BASE"
    ],
    "description": "Typescript React Function Component"
  },
```

----
📂 [[Tooling]] | Последнее изменение: 05.05.2024 16:55