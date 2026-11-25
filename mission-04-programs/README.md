# Mission 4 - How Programs Run

## 1. Task / objective
Create and run a one-line Python script (`hello.py`) and compare how compilers and interpreters execute programs[cite: 27].

## 2. Work completed
- Created `hello.py` inside `mission-04-programs/` printing `Hello from Python` and ran it with Python 3[cite: 27].
- Added a comparison table and short explanation comparing compilers and interpreters[cite: 27].

## 3. Commands / tools used
- `cd` and `pwd`: Move into `mission-04-programs` and verify the working path.
- `cat`: Create `hello.py` and `README.md`.
- `python3 hello.py`: Run the Python program from Terminal[cite: 27].
- `git status`, `git add`, `git commit`, `git push`: Stage, commit, and push Mission 4 changes.

## 4. My understanding

### Task 4.1 - Running `hello.py`
Running `python3 hello.py` executes `print("Hello from Python")` and displays `Hello from Python` in Terminal[cite: 27].

### Task 4.2 - Compiler vs. Interpreter Comparison

| Point | Compiler | Interpreter |
| :--- | :--- | :--- |
| When translation / execution happens | Translates source code before running the program[cite: 27] | Reads and executes instructions at runtime[cite: 27] |
| Typical output | Compiled output or executable | Direct runtime execution and output |
| One example | C compiler (example) | Python (`python3`) |
| One advantage | Optimizes code ahead of execution | Runs directly without a separate compile step |

A compiler translates source code before execution, whereas an interpreter reads and executes instructions at runtime[cite: 27]. Based on the comparison table, a compiler produces compiled output ahead of running and can optimize code beforehand, while an interpreter runs code directly at runtime for quick testing. Some language implementations also combine both approaches[cite: 27].

## 5. Difficulties faced
No major difficulties[cite: 31].

## 6. How I resolved them
Not applicable[cite: 31].

## 7. Evidence / files
- `mission-04-programs/hello.py`[cite: 27]
- `mission-04-programs/README.md`[cite: 27]

## 8. Commit details
Committed with message `"Compare compilers and interpreters"` and pushed to `origin/main`.
