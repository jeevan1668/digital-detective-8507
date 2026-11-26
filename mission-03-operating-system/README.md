# Mission 3 - Understand the Operating System

## Task 3.1 - Explore Your Operating System

| Information Explored | What It Tells You | Your Observation (Privacy-Safe) |
| :--- | :--- | :--- |
| Operating system / system details | Identifies the OS version, kernel, and hardware architecture | macOS 27.2.1 (Darwin kernel 27.2.0) on arm64 (`sw_vers`, `uname -srm`) |
| Current account identity | Shows which user account is currently logged in | The account name appeared in the Terminal prompt; it is redacted here to protect privacy. |
| Available and used storage | Shows total size, used space, and free space on the volume | Root volume `/` shows 460Gi total, 13Gi used (4%), 339Gi available (`df -h /`) |
| System activity snapshot | Shows a brief snapshot of CPU/memory load and process counts | `top -l 1`: 859 processes total (2 running, 857 sleeping), 3,957 threads, 88.74% idle CPU, 15G physical memory used and 284M unused. This is one snapshot and will change over time. |

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
| Memory management | Allocates RAM to running programs and releases it when finished | Keeping the data that active apps need in memory while they run |
| Device management | Coordinates hardware and peripherals through drivers so apps don't access hardware directly | Displaying text on the screen or taking input from the keyboard/trackpad |
| File management | Organizes files and folders on storage and tracks where data is stored | Creating `os-practice/sample.txt` and reading/saving Markdown files in mission folders |
| User interface / shell | Provides graphical or command-line interfaces for users to interact with the OS | Using the macOS desktop or typing commands into `zsh` in Terminal |
| Security and permissions | Controls account access and file permissions to protect data and system stability | Restricting write/execute permissions on files and separating user accounts |

## Commands Used
- `sw_vers`, `uname -srm` - checked macOS version, kernel, and architecture
- `df -h /` - checked root-volume storage
- `top -l 1 | head -n 10` - viewed a short system-activity snapshot
- `ps -Ao pid,comm | head -n 12` - viewed process IDs and names

## Difficulties Faced
- The first `df -h /` attempt was entered at Python's `>>>` prompt and produced a syntax error. I exited Python with `exit()`, then ran the command at the Terminal prompt.
- Keeping account and device names out of public evidence.

## How I Resolved Them
- Exited Python and reran the command in Terminal.
- Redacted account and device names from the public notes.

## Evidence / files
- `os-practice/sample.txt`
- `evidence/mission-03-operating-system/observations.txt`

## Commit details
- Corrected Mission 3 storage observation
- Recorded privacy-safe Mission 3 storage results
- Recorded observed Mission 3 process examples
