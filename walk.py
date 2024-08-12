"""
Рекурсивно сканирует директорию с контентом, и составляет оглавление
в файле index.md.
"""

import os

CONTENT_PATH = "./content"

exclude_folders = [
    "attachments",
    "content",
]

toc_dirs = ""
toc_full = ""

# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk(CONTENT_PATH):
    path = root.split(os.sep)
    folder = os.path.basename(root)

    if folder in exclude_folders:
        continue

    file_tabs = len(path) - 2
    folder_tabs = file_tabs - 1

    line = folder_tabs * "\t" + f"- 📂 [[{folder}]]<br>\n"
    toc_dirs += line
    toc_full += line

    for file in files:
        if file.endswith("md"):
            toc_full += file_tabs * "\t" + f"- 📄 [[{file[:-3]}]]<br>\n"

            # Добавим ссылку на директорию в конце каждой заметки
            full_path = os.path.join(root, file)
            with open(full_path, "a") as note:
                note.write(f"\n\n----\n📂 [[{folder}]]")

index_md = f"""
---
title: Оглавление
---

Здесь находится статическая сборка [моих](https://hazadus.ru/about/) заметок, касающихся программирования,
разработки, технической литературы и т.п.

Эти заметки предназначены для личного пользования и удобного обмена информацией с коллегами.
Информация может быть неполной, неактуальной – используйте на свой страх и риск ☠️!

О концепции _цифрового сада_ вы можете почитать [тут](https://jzhao.xyz/posts/networked-thought).

----

## Актуальное

- [[FastAPI]]
- [[Go]]

----

## Краткое оглавление
{toc_dirs}

## Полное оглавление
{toc_full}
"""

print(index_md)
with open(f"{CONTENT_PATH}/index.md", "w") as file:
    file.write(index_md)
