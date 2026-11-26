# Mission 5 - Numbers and Data

## 1. Task / objective
Convert values between decimal, binary and hexadecimal; verify conversions with Python; build and run a number converter; explain text encoding.

## 2. Work completed
- The `number_converter.py` program is present.
- Ran the program with the positive decimal inputs 13, 25 and 42 and recorded the outputs below.
- Manual conversion working, Python interactive checks and text-encoding answers still need to be added before submission.

## 3. Commands / tools used
- `cd ../mission-05-numbers-data` - moved from Mission 3 into the Mission 5 folder.
- `python3 number_converter.py` - ran the converter.
- `printf '13\n' | python3 number_converter.py` (and the same command with 25 and 42) - supplied test values and captured the program output.

## 4. My understanding

### Task 5.1 - Manual conversions
Add the division or place-value steps for each conversion here before submission.

### Task 5.2 - Python verification
Record the Python expressions, results, and whether they match the manual working here before submission.

### Task 5.3 - `number_converter.py` and test runs
The program uses `int()` to turn the typed decimal text into an integer. Python's `bin()` and `hex()` functions return binary and hexadecimal representations; their results include `0b` and `0x` prefixes.

| Decimal input | Binary output | Hexadecimal output |
| :--- | :--- | :--- |
| 13 | `0b1101` | `0xd` |
| 25 | `0b11001` | `0x19` |
| 42 | `0b101010` | `0x2a` |

### Task 5.4 - Text encoding
Add the ASCII decimal codes for `A` and `a`, explain why computers use character encodings, and name a character outside basic ASCII before submission.

## 5. Difficulties faced
No major difficulties were recorded during the converter test.

## 6. How I resolved them
Not applicable for the converter test.

## 7. Evidence / files
- `number_converter.py`
- This README with the converter test outputs

## 8. Commit details
The converter was previously committed with the message `Build number converter and practise data representation`. This README was updated with the verified test outputs.
