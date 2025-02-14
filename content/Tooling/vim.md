## References

- https://www.warp.dev/topic/vim

----
## Vim Modes

Reference: https://www.warp.dev/terminus/vim-modes

### Insert Mode

 It allows you to modify the text buffer by typing and removing characters, the same way you would do in most modern text editors.

There are 3 ways to enter the Insert mode from the default Normal mode:
- Pressing `i` (for _insert_) will directly switch to Insert mode.
- Pressing `a` (for _append_) will switch to Insert mode and move the cursor after the current character.
- Pressing `o` will switch to Insert mode and insert a new line below the line the cursor is on.

## Go to line

Reference: https://www.warp.dev/terminus/vim-go-to-line

To ==go to a specific line number==, enter the line number in Command-line Mode (`:<line number>`) or the line number and G (`<line number>G`) in Normal Mode.

## Deleting lines

Reference: https://www.warp.dev/terminus/delete-line-vim

- `dd` ==deletes the whole line under the cursor==.
- `5dd` deletes multiple (5) lines, starting at the cursor.
- `d$` deletes to the end of the line, starting at the cursor.
- `dG` deletes all lines starting from the line under the cursor.

_However_, those only work in normal mode. Ex mode has some more capable and interesting ways to remove lines!

## Searching

Reference: https://www.warp.dev/terminus/searching-in-vim

#### Search for next word (forward search)

To search in vim, open up your file with vim `vim myfile.txt`, and press ESC to switch to normal mode. Type `/` followed by the word you are searching for. For example, if we want to search for ‘ERROR’ in our file. We type `/ERROR`. This will take us to the first occurrence of the word.

To find the next occurrence, simply type `n`. And to go back to the previous occurrence, type `N`. To stop searching press ESC to go normal mode.

#### Search for previous word (backwards search)

To search backwards in a file, open up the file, `vim myfile.txt`, and press ESC to switch to normal mode. Type `?` followed by the word. If we are searching for the word ‘INFO’ backwards, we type `?INFO`. Type `N` to search backwards and `n` to search forwards. To stop searching press ESC to go normal mode.

### Find And Replace

Reference: https://www.warp.dev/terminus/vim-find-and-replace

- `:s/<pattern>/<replacement>`



----
📂 [[Tooling]] | Последнее изменение: 10.02.2025 09:51