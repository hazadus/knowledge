📂 [[Tooling]]

----
## Installation
### MacOS
```Bash
brew install tmux
```
## Commands Cheatsheet
### CLI
```Bash
# Create new session "dev"
tmux new-session -s dev
# Attach to session "dev"
tmux attach -t dev
```
### `tmux` Hotkeys
|   |   |
|---|---|
|Ctrl + B, C|Create new window|
|Ctrl + B, 0 or 1|Switch windows|
|Ctrl + B, %|Split windows vertically|
|Ctrl + B, “|Split windows horizontally|
|Ctrl + B, →, ←|Select right, left window|
|Ctrl + B, D|Detach from session|
|Ctrl + B, W|Window list|
|Ctrl + B, S|Session list|
|Ctrl + B, `,`|Rename current window|
|Ctrl + B, `?`|Cheatsheet|
## Configuring `tmux`
```Bash
nano ~/.tmux.conf
```
- `set-option -g prefix C-q` – change default `Ctrl + B` to `Ctrl + Q`.
- `set g mouse on` – turn on mouse controls.
## References
https://github.com/gpakosz/.tmux

> [!info] Настраиваем tmux по хардкору! Копирование из tmux, статус бар, цвета, hot keys  
> Запущен первый курс мощной образовательной программы от Диджитализируй: «Основы компьютерных и веб-технологий с Python»  
> [https://www.youtube.com/watch?v=LkFtvMzMwjw&list=PLAk6CfuV7hyqHyQVHZMQRihAfebXpxn2O&index=10](https://www.youtube.com/watch?v=LkFtvMzMwjw&list=PLAk6CfuV7hyqHyQVHZMQRihAfebXpxn2O&index=10)