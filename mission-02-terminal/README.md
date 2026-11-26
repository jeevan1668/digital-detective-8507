# Mission 2 - Become Comfortable with the Terminal

## 1. Task / objective
Use Terminal to inspect folders, create and manage practice files, understand flags and pipes, and explain package managers.

## 2. Work completed

### Task 2.1 - Basic Terminal operations

| Operation | Command | What it does / observation |
| :--- | :--- | :--- |
| Show current directory | `pwd` | Displays the current folder path. |
| List files and folders | `ls` | Shows the items in the current folder. |
| Detailed listing | `ls -l` | Shows details such as permissions, sizes and dates. |
| Move to parent folder | `cd ..` | Changes the current location to its parent. |
| Create a folder | `mkdir sample-folder` | Creates a new folder. |
| Create an empty file | `touch original.txt` | Creates an empty file. |
| Copy a file | `cp original.txt copied.txt` | Creates another copy of the file. |
| Rename or move a file | `mv copied.txt renamed.txt` | Changes its name or location. |
| Display file contents | `cat original.txt` | Prints the file's contents in Terminal. |

### Task 2.2 - File management practice

The `terminal-practice/` folder at the repository root contains the practice files. The `practice.txt` file has two lines, and `renamed-backup.txt` contains the same text.

- `echo "text" > practice.txt` writes text and replaces any previous contents.
- `echo "text" >> practice.txt` adds another line at the end.
- `cat practice.txt` displays both lines.
- `cp practice.txt backup.txt` makes a copy.
- `mv backup.txt renamed-backup.txt` renames the backup.

Copying leaves the original in place and creates another file. Moving changes the file's location or name. The current-directory command tells you where relative commands will apply. A directory listing helps you see which files and folders are available.

### Task 2.3 - Flags and pipes

- `ls` shows a normal listing.
- `ls -l` shows detailed information.
- `ls -lah` includes hidden files and displays readable file sizes.
- `ls -lah | head -n 5` sends the listing through a pipe to show only its first five lines.

Flags change a command's behavior: `-a` includes hidden files, `-l` shows details, and `-h` makes sizes easier to read. The pipe symbol (`|`) sends the output of the command on its left as input to the command on its right.

### Task 2.4 - Package managers

Homebrew version 7.0.9 was checked with `brew --version`. The installed-package list was viewed with `brew list`; examples included `cairo` and `openjdk`. No packages were installed or uninstalled.

A package manager helps install, update and remove software. It can also manage software dependencies, making it easier to keep tools organized.

## 3. Commands / tools used
- `pwd`, `ls`, `ls -l`, `cd`, `mkdir`, `touch`, `cp`, `mv`, `cat`, `echo`, `head)
- `brew --version`, `brew list`
- macOS Terminal, Homebrew, Git and GitHub

## 4. My understanding
The Terminal accepts typed commands to inspect and manage files. Flags add options to commands, and a pipe connects one command's output to another. A package manager organizes software installation and updates.

## 5. Difficulties faced
It was confusing at first to distinguish copying from moving files and replacing text from appending text.

## 6. How I resolved them
The practice files made the difference clear: `>` replaces contents, `>>` appends, `cp` keeps the source and creates a copy, and `mv` renames or relocates a file.

## 7. Evidence / files
- `../terminal-practice/original.txt`
- `../terminal-practice/practice.txt`
- `../terminal-practice/renamed.txt`
- `../terminal-practice/renamed-backup.txt`

## 8. Commit details
Committed as `Complete Terminal and file management mission` and pushed to GitHub.
