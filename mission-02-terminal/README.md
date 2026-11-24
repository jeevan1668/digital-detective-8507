# Mission 2 – Become Comfortable with the Terminal

## Task Completed

Practised basic Terminal commands, file management, command flags, pipes and package managers using macOS Terminal.

## Task 2.1 – Basic Terminal Operations

| Operation | Command | Purpose |
|---|---|---|
| Current directory | `pwd` | Displays the current folder path |
| Directory listing | `ls` | Lists files and folders |
| Detailed listing | `ls -l` | Shows file permissions, sizes and dates |
| Change directory | `cd ..` | Moves to the parent directory |
| Create directory | `mkdir sample-folder` | Creates a new folder |
| Create empty file | `touch original.txt` | Creates an empty file |
| Copy file | `cp original.txt copied.txt` | Creates a copy |
| Rename file | `mv copied.txt renamed.txt` | Renames or moves a file |
| Display contents | `cat original.txt` | Displays file contents |

## Task 2.2 – File Management Practice

Created a folder named `terminal-practice` and practised creating, editing, copying and renaming files.

Used:
- `echo "text" > practice.txt` to write the first line.
- `echo "text" >> practice.txt` to append another line.
- `cat practice.txt` to verify both lines.
- `cp practice.txt backup.txt` to create a backup.
- `mv backup.txt renamed-backup.txt` to rename the backup.

**Understanding:**

The `>` operator replaces existing file contents, whereas `>>` adds new content without deleting previous lines.

Copying creates another version of a file, while moving transfers the file to another location or changes its name.

## Task 2.3 – Flags and Pipes

Commands practised:

- `ls` – Normal directory listing.
- `ls -l` – Detailed listing.
- `ls -lah` – Includes hidden files and human-readable file sizes.
- `ls -lah | head -n 5` – Displays only the first five lines.

**Understanding:**

Flags modify how a command behaves. The `-a` flag includes hidden files, `-l` displays detailed information and `-h` makes file sizes easier to read.

The pipe symbol (`|`) sends the output of one command as input to another command. Here, `ls -lah` provides the listing and `head -n 5` displays its first five lines.

## Task 2.4 – Package Managers

Checked Homebrew using:

- `brew --version`
- `brew list`

Homebrew version: 7.0.9

Homebrew is a package manager for macOS. It helps users install, update and manage software packages from the Terminal. Package managers make software management easier and help maintain required dependencies.

No packages were installed or uninstalled during this mission.

## Tools and Commands Used

- macOS Terminal
- Homebrew
- Git and GitHub

## What I Understood

I learned how to navigate directories, create and manage files, copy backups and rename files using Terminal commands.

I also understood the difference between replacing and appending file contents, how command flags modify output and how pipes connect commands.

I learned that package managers simplify software installation and maintenance.

## Difficulties Faced

Initially, understanding the difference between copying and moving files and between the `>` and `>>` operators was slightly confusing. Practising these commands helped me understand them better.

## Completion Status

Mission 2 – Become Comfortable with the Terminal completed.


