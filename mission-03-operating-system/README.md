# Mission 3 - Understand the Operating System

## 1. Task / objective
Explore the operating system, processes, storage, paths and file permissions, and describe the operating system's responsibilities.

## 2. Work completed

### Task 3.1 - Operating system and system activity

| Information explored | What it tells you | Privacy-safe observation |
| :--- | :--- | :--- |
| Operating system and system details | Shows the OS version, kernel and hardware architecture | macOS 27.2.1 (Darwin 27.2.0) on arm64 |
| Current account | Identifies the signed-in account | Account name was visible in the Terminal prompt and is redacted here. |
| Storage | Shows total, used and available space | Root volume `/`: 460Gi total, 13Gi used, 339Gi available, 4% capacity |
| System activity | Shows running processes, threads, CPU and memory | Snapshot: 859 processes (2 running, 857 sleeping), 3,957 threads, 88.74% idle CPU, 15G physical memory used and 284M unused |

### Task 3.2 - Processes
A process is a program that is currently running. A PID (Process Identifier) is the number the OS uses to distinguish one running process from another. The process listing showed `launchd` (PID 1) and `logd` (PID 535). PIDs can change when a process restarts or the computer reboots.

### Task 3.3 - Paths and permissions
- The redacted absolute path observed was `/Users/[redacted]/digital-detective-8507/mission-03-operating-system`.
- From that folder, `os-practice/sample.txt` is a relative path.
- `ls -l os-practice/sample.txt` showed `-rw-r--r--`: the owner can read and write; the group and other users can read; no one has execute permission.

### Task 3.4 - Operating-system responsibilities

| Responsibility | Explanation | Example |
| :--- | :--- | :--- |
| Process management | Starts, schedules and stops running programs | Sharing CPU time between Terminal and other apps |
| Memory management | Gives running programs RAM and reclaims it when no longer needed | Keeping active app data available while the apps run |
| Device management | Helps programs use connected hardware | Sending keyboard input to the computer and displaying text |
| File management | Organizes files and folders on storage | Saving and opening `os-practice/sample.txt` |
| User interface / shell | Provides ways for a person to interact with the computer | macOS desktop and the `zsh` shell in Terminal |
| Security and permissions | Controls who can access files and system resources | Read/write/execute permissions on a file |

## 3. Commands / tools used
- `sw_vers`, `uname -srm` - checked OS version, kernel and architecture
- `df -h /` - checked root-volume storage
- `top -l 1 | head -n 10` - viewed a short activity snapshot
- `ps -Ao pid,comm | head -n 12` - viewed process IDs and names
- `cd`, `pwd`, `sed`, and `ls -l` - navigated, checked the location, redacted the username and viewed permissions

## 4. My understanding
The OS manages running programs, memory, devices, files, the user interface and access permissions. An absolute path starts at `/`; a relative path starts from the current folder. In a permission string such as `-rw-r--r--`, the letters are grouped for the owner, group and other users.

## 5. Difficulties faced
The first `df -h /` command was entered at Python's `>>>` prompt, which produced a syntax error. Account and device names also needed to be kept out of public notes.

## 6. How I resolved them
Exited Python with `exit()` and ran the command at the Terminal prompt. Redacted the account and device names from the notes.

## 7. Evidence / files
- `os-practice/sample.txt`
- `observations.txt` - privacy-safe system, process, path and permission results

## 8. Commit details
The mission was committed as `Document operating system and file management`. Follow-up commits record the updated live observations and keep the evidence inside this mission folder.
