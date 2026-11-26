# Mission 3 - Understand the Operating System

## Task 3.1 - Explore Your Operating System

| Information Explored | What It Tells You | Your Observation (Privacy-Safe) |
| :--- | :--- | :--- |
| Operating system / system details | Identifies the OS version, kernel, and hardware architecture | macOS 27.2.1 (Darwin kernel 27.2.0) on arm64 (`uname -a`, `sw_vers`) |
| Current account identity | Shows which user account is currently logged in | Active account: `[redacted]` (`whoami`) |
| Available and used storage | Shows total size, used space, and free space on the volume | Root volume `/` shows 460Gi total, 13Gi used (4%), 339Gi available (`df -h /`) |
| System activity snapshot | Shows a brief snapshot of CPU/memory load and process counts | 926 total processes (2 running, 924 sleeping), ~80.0% idle CPU, 0 swap (`top -l 1`) |

## Task 3.2 - Understand Processes

- **What is a process?** A process is a program that is currently running in memory with its own execution state and system resources.
- **What does the PID column represent?** PID stands for **Process Identifier**—a unique number assigned by the operating system to each running process so it can be tracked and managed.
- **Two processes visible in the Terminal snapshot:** `launchd` (PID 1) and `logd` (PID 535). These were visible when `ps -Ao pid,comm | head -n 12` was run. PIDs can change when processes restart or the computer reboots.

## Task 3.3 - Understand Paths and Permissions

### Navigation and Paths
- Navigating between `mission-03-operating-system` and `os-practice` using `cd` and `pwd` updates the displayed current working directory.
- **Absolute vs. Relative Path:**
  - **Absolute path:** Starts from `/` with the full path from root—for example, `/Users/[redacted]/digital-detective-8507/mission-03-operating-system`.
  - **Relative path:** Relative to the current working directory—for example, `os-practice/sample.txt` from inside `mission-03-operating-system`.

### File Permissions
- `ls -la os-practice/sample.txt` displays `-rw-r--r--`.
- For the **owner** (`rw-`):
  - **Read (`r`):** Allowed—the owner can view the file's contents.
  - **Write (`w`):** Allowed—the owner can edit or overwrite the file.
  - **Execute (`x`):** Not allowed (`-`)—the file is not marked to run as an executable program/script.

## Task 3.4 - Explain Operating-System Responsibilities

| OS Responsibility | Your Explanation | Example |
| :--- | :--- | :--- |
| Process management | Creates, schedules, pauses, and ends running programs and shares CPU time | Running browser windows alongside Terminal and background system processes |
| Memory management | Allocates RAM to running programs and releases it when finished | Holding active apps/tabs in memory and keeping swap usage at zero when enough RAM is free |
| Device management | Coordinates hardware and peripherals through drivers so apps don't access hardware directly | Displaying text on the screen or taking input from the keyboard/trackpad |
| File management | Organizes files and folders on storage and tracks where data is stored | Creating `os-practice/sample.txt` and reading/saving Markdown files in mission folders |
| User interface / shell | Provides graphical or command-line interfaces for users to interact with the OS | Using the macOS desktop or typing commands into `zsh` in Terminal |
| Security and permissions | Controls account access and file permissions to protect data and system stability | Restricting write/execute permissions on files and separating user accounts |

## Commands Used
- `pwd`, `cd`, `mkdir`, `echo`, `ls -la`
- `uname -a`, `sw_vers`, `whoami`, `df -h /`, `top -l 1`, `ps -Ao pid,comm | head -n 12`
- `git status`, `git add`, `git commit`, `git push`

## Difficulties Faced
- Keeping notes and evidence free of personal usernames or device identifiers (`[redacted]`) and filtering long command outputs (`head`, `grep`) so key details are easy to read.

## Completion Status
Mission 3 - Understand the operating system completed.
