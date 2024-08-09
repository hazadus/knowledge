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

index_md = """
---
title: Оглавление Базы Знаний
---\n
"""

# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk(CONTENT_PATH):
    path = root.split(os.sep)
    folder = os.path.basename(root)

    if folder in exclude_folders:
        continue

    file_tabs = len(path) - 2
    folder_tabs = file_tabs - 1

    index_md += folder_tabs * "\t" + f"- 📂 [[{folder}]]<br>\n"
    print(folder_tabs * "-" + "📂", folder)

    for file in files:
        if file.endswith("md"):
            index_md += file_tabs * "\t" + f"- 📄 [[{file[:-3]}]]<br>\n"
            print(file_tabs * "-" + "📄", file)


print(index_md)
with open(f"{CONTENT_PATH}/index.md", "w") as file:
    file.write(index_md)
