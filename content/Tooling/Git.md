📂 [[Tooling]]

----
## The Git Song
(Verse 1)  
Yo, listen up, I got a story to tell,  
'Bout programmers and how they use Git so well,  
It's a version control system, a developer's delight,  
Helping us collaborate and code with all our might.  
(Chorus)  
Git, Git, it's the way we commit,  
Branching, merging, pushing, we never quit,  
With Git, we track changes, keep our code in line,  
Programmers unite, let's make our projects shine.  
(Verse 2)  
In the command line, we start with a clone,  
Pulling down the repo, making it our own,  
We create branches, each with a unique name,  
Working on features, fixing bugs, it's all fair game.  
(Chorus)  
Git, Git, it's the way we commit,  
Branching, merging, pushing, we never quit,  
With Git, we track changes, keep our code in line,  
Programmers unite, let's make our projects shine.  
(Verse 3)  
We add files, make changes, and stage them too,  
Committing our work, leaving a message that's true,  
Pushing to the remote, sharing with the team,  
Collaboration at its finest, fulfilling our dream.  
(Chorus)  
Git, Git, it's the way we commit,  
Branching, merging, pushing, we never quit,  
With Git, we track changes, keep our code in line,  
Programmers unite, let's make our projects shine.  
(Bridge)  
Merge conflicts may arise, but we'll find a way,  
Resolving differences, making sure all's okay,  
Git stash, rebase, cherry-pick, we got the tricks,  
Programmers using Git, we're a force that sticks.  
(Chorus)  
Git, Git, it's the way we commit,  
Branching, merging, pushing, we never quit,  
With Git, we track changes, keep our code in line,  
Programmers unite, let's make our projects shine.  
(Outro)  
So raise your keyboards high, let's give a cheer,  
For Git, the tool that brings us all near,  
Programmers united, we'll never be split,  
With Git in our hands, we'll code and never quit.  
## The Basics
### Basic git commands
```Bash
sudo apt install git
```
```Bash
# Show config info
git config --list
# Set user name and email
git config --global user.name "hazadus"
git config --global user.email "hazadus7@gmail.com"
```
```Bash
# Check if repo already exists
git status
# Creates '.git' directory
git init
# Add all directory contents to repo
git add .
# Remove files '.DS_Store' from cached files
git rm --cached .DS_Store
# Make commit
git commit -m 'Initial commit'
git commit
# ...Enter (multiline) commit message
# ...Press `Esc`, `:wq` to save and exit vim
# Show info on last commit and its contents
# (enter to scroll, 'q' to quit)
git show
# Show commit history (log)
git log
```
### gitignore

> [!info] Git - gitignore Documentation  
> A gitignore file specifies intentionally untracked files that Git should ignore.  
> [https://git-scm.com/docs/gitignore](https://git-scm.com/docs/gitignore)  
```Markdown
[Official docs](https://git-scm.com/docs/gitignore)
Exclude file:
`error.log`
Exlude files:
`*.log`
Exlude folder:
`logs/`
Exclude folder except one file:
`logs/*.log`
`!logs/special.log`
```
### Working with remote origin
```Bash
# Show URL of remote origin
git remote -v
# Remove
git remote remove origin
# Add
git remote add origin https://github.com/sortedmap/git-basics
```
```Bash
# create repo on GitHub before pushing
git push -u origin master
# use Personal token instead of password, if asked (see 1Pwd/GitHub site).
```
## Ветки
### Работа с локальными ветками
```Bash
# Посмотреть существующие ветки, и узнать текущую (*)
git branch
# Посмотреть ВСЕ существующие ветки (в тч remote), и узнать текущую (*)
git branch -a 
# Create & checkout new branch
# NB: перед сменой ветки, изменения должны быть committed или stashed (спрятаны)!
git checkout -b add-new-feature
# or:
git branch add-new-feature
git checkout add-new-feature
# Удалить ветку
git branch -d 21-unused-feat
```
### Работа с удалёнными ветками
```Bash
# 1) ветка создана локально, но отсутствует на удаленном сервере
# Отправить текущую ветку на сервер и связать её с текущей с таким же именем
# (предполагается что активна нужная ветка!)
git push --set-upstream origin add-new-feature
# идентично
git push -u origin add-new-feature
```
```Bash
# 2) ветка создана на сервере, её нужно загрузить в локальный репозиторий
git pull
# ...и новые ветки появятся локально
```
```Bash
# 3) ветки есть и локально, и на сервере. но внесены изменения, которые нужно синхронизировать
git push / git pull
```
### Откладывание изменений (stash)
```Bash
git stash
# ^ все сделанные изменения откладываются, файлы возвращаются к состоянию последнего коммита
# Что-то меняем, делаем коммит...
# Восстановить отложенные изменения, они вольются в новую версию файлов:
git stash pop
# Изменения можно откладывать последовательно несколько раз!
# Список можно посмотреть командой:
git stash list
# Достаются изменения последовательно, как из стека, командой
git stash pop
# Удалить "заначку" под номером Х можно командой
git stash drop X
```
git stash позволяет “заначить” изменения в одной ветке, потом их восстановить в другой ветке. Таким образом, если изменения начали вносить по ошибке не в ту ветку, можно перенести их в нужную!
### Слияние веток
```Bash
# Допустим, мы хотим влить ветку add-new-feature в ветку master.
# Для этого, будучи в ветке master:
git merge add-new-feature
# Если мы наоборот хотим влить ветку master в другую, делаем:
git checkout add-new-feature
git merge master
```
### Конфликты git
**Конфликт** – ситуация, при которой изменения не могут быть слиты гитом автоматически.
В случае конфликта, смотрим файлы, где они произошли, командой `git status`.
`<<<<<<< HEAD` означает часть, которая находится в **текущей ветке** (в которую вливаем изменения).
`>>>>>>> feat-name` означает часть, которая находится в сливаемой ветке.
Идём в эти файлы, разрешаем конфликты в помеченных местах руками. После этого, помечаем файлы командой `git add .` . Командой `git status` проверяем, что файлы с разрешенными конфликтами добавлены в индекс.

> [!info] Meld  
> All development happens on GNOME's Gitlab instance.  
> [http://meldmerge.org/](http://meldmerge.org/)  
Установить Meld инструментом для слияния по умолчанию: `git config —-global merge.tool meld`
Для запуска инструмента в случае конфликта: `git mergetool`
После разрешения конфликта, исполнить `git commit -m ‘Merge main into branch’`. Или просто `git commit` , тогда он сам напишет сообщение.
### Запрос на слияние
GitHub – pull request == GitLab – merge request
![[attachments/Untitled 4.png|Untitled 4.png]]
**Create a merge commit** – все коммиты из сливаемой ветки будут добавлены в основную.
**Squash and merge** – все коммиты будут объединены в один и влиты.
**Rebase and merge** – перебазирование коммитов в основную ветку так, как будто они туда и делались.
### Модели ветвления
![[attachments/Untitled 1 2.png|Untitled 1 2.png]]
**Trunk Based Development**
![[attachments/Untitled 2 2.png|Untitled 2 2.png]]
## Сравнение версий и отмена изменений
### Журнал коммитов
```Bash
# Вывести краткий журнал со схематичным графом
git log --oneline --all --graph
```
### Просмотр изменений
```Bash
# Просмотр незакоммиченных изменений
# Сравнивает рабочий каталог с индексом
# Показать изменения файла
git diff filename
# Показать все изменения
git diff
# В выводе:
# --- то что в индексе
# +++ то что в рабочем каталоге
# @@ -6,8 +6,8 @@
# 6,8 означает "с шестой строки ещё 8 строк"
# Показать изменения внутри строк:
git diff --word-diff
# Сравнивать коммиты можно, даже если они находятся в разных ветках -
# хэши в рамках одного репозитория уникальны.
# Просмотр разницы между коммитами (у файла)
git diff hash1 hash2 filename
# Просмотр разницы между коммитами (у всего проекта)
git diff hash1 hash2
# Посмотреть кто что правил в файле
git blame filename
```
### Удаление незакоммиченных изменений
Следующими командами необходимо пользоваться осторожно, так как отмененные изменения будут потеряны безвозвратно.
```Bash
git restore filename
# Если файл уже в индексе (делали git add .):
git restore --staged filename
git restore filename
# Удалить из рабочей директории все незакомиченные изменения, в тч
# добавленные в индекс.
git reset --hard
# Удалить новые неотслеживаемые и незакомиченные изменения:
git clean -f
```
### Удаление файлов из отслеживания
Сначала добавить файл в `.gitignore`.
```Bash
git rm --cached filename
```
### Отмена закоммиченных изменений
```Bash
# Вернуть файл к нужной версии
git checkout <hash> filename
# Отменить КОНКРЕТНЫЙ коммит (не только последний, любой)
git revert <hash>
# Последовательно отменять коммиты:
git revert --no-commit <hash> 
```
### Отмена (сброс) комитов
```Bash
# Отправка изменений в индекс
git reset --soft <commit>
# Отправка изменений в рабочую директорию
git reset --mixed <commit>
# СБРОС изменений с их утратой!
git reset --hard <commit>
# Добавить изменения к последнему коммиту, и:
# - поправить комит месидж:
git commit --amend -m <new_comment>
# - оставить комит месидж как есть:
git commit --amend --no-edit
```
### Отмена слияний, переименование и удаление веток
```Bash
# Указать хэш коммита, который был крайний перед мердж-коммитом
git reset --merge <hash>
# Когда в ходе мерджа случился конфликт:
git merge --abort
```
### Перенести коммит из ветки в ветку
```Bash
# через сташ
git reset <hash>
git stash
git checkout right-branch
git stash pop
# 2) или после коммита сначала делаем нужную ветку
git checkout -b right-branch
git checkout master
git reset --hard HEAD~1
# в ветке right-branch изменение будет, так как она отпочкована с уже
# измененного мастера. А в мастере мы жестко откатываем один последний комит.
```
## Правила работы в git
![[attachments/Untitled 3 2.png|Untitled 3 2.png]]
Комментарии к комитам должны конкретно отражать их суть, что в них сделано.

> [!info] Conventional Commits  
> A specification for adding human and machine readable meaning to commit messages  
> [https://www.conventionalcommits.org/en/v1.0.0/](https://www.conventionalcommits.org/en/v1.0.0/)  
## Tagging

> [!info] Git - Tagging  
>  
> [https://git-scm.com/book/en/v2/Git-Basics-Tagging](https://git-scm.com/book/en/v2/Git-Basics-Tagging)  
```Bash
git push origin --tags
```
## Misc stuff
```Bash
# Count lines in project
git ls-files | xargs wc -l
git ls-files | grep '\.js' | xargs wc -l
```
[https://stackoverflow.com/questions/26881441/can-you-get-the-number-of-lines-of-code-from-a-github-repository](https://stackoverflow.com/questions/26881441/can-you-get-the-number-of-lines-of-code-from-a-github-repository)

----
📂 [[Tooling]] | Последнее изменение: 07.02.2024 20:16