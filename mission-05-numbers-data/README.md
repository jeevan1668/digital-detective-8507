# Mission 5 - Numbers and Data

## 1. Task / objective
Convert numbers between decimal, binary and hexadecimal; verify conversions with Python; build and run a number converter; explain text encoding.

## 2. Work completed
- Worked the required conversions and checked them with Python's conversion functions.
- Ran `number_converter.py` with the decimal inputs 13, 25 and 42.
- Recorded the ASCII values for uppercase `A` and lowercase `a`.

## 3. Commands / tools used
- `cd ../mission-05-numbers-data` - moved from Mission 3 into the Mission 5 folder.
- `python3` - checked number conversions.
- `python3 number_converter.py` - ran the converter.
- `printf '13\n' | python3 number_converter.py` (repeated with 25 and 42) - supplied test values and captured outputs.

## 4. My understanding

### Task 5.1 - Manual conversions

**Decimal 13 to binary:** Divide by 2 and read the remainders from bottom to top.

```text
13 ÷ 2 = 6 remainder 1
 6 ÷ 2 = 3 remainder 0
 3 ÷ 2 = 1 remainder 1
 1 ÷ 2 = 0 remainder 1
Result: 1101
```

**Decimal 25 to binary:**

```text
25 ÷ 2 = 12 remainder 1
12 ÷ 2 =  6 remainder 0
 6 ÷ 2 =  3 remainder 0
 3 ÷ 2 =  1 remainder 1
 1 ÷ 2 =  0 remainder 1
Result: 11001
```

**Binary to decimal:**

- `1010₂ = 1×8 + 0×4 + 1×2 + 0×1 = 10₁₀`
- `1101₂ = 1×8 + 1×4 + 0×2 + 1×1 = 13₁₀`

**Hexadecimal to decimal:**

- `A₁₆ = 10₁₀`
- `1F₁₆ = 1×16 + 15 = 31₁₀`

**Binary to hexadecimal:**

- `1111₂` is one four-bit group. Its value is 15, which is `F₁₆`.

### Task 5.2 - Python verification

| Check | Python expression | Result |
| :--- | :--- | :--- |
| Decimal 13 to binary | `bin(13)` | `0b1101` |
| Decimal 25 to binary | `bin(25)` | `0b11001` |
| Binary 1010 to decimal | `int("1010", 2)` | `10` |
| Binary 1101 to decimal | `int("1101", 2)` | `13` |
| Hexadecimal A to decimal | `int("A", 16)` | `10` |
| Hexadecimal 1F to decimal | `int("1F", 16)` | `31` |
| Binary 1111 to hexadecimal | `hex(int("1111", 2))` | `0xf` |

### Task 5.3 - `number_converter.py` and test runs

The program reads text with `input()`, converts it to an integer with `int()`, and uses `bin()` and `hex()` to display the result. Python includes `0b` and `0x` prefixes to show the number base.

| Decimal input | Binary output | Hexadecimal output |
| :--- | :--- | :--- |
| 13 | `0b1101` | `0xd` |
| 25 | `0b11001` | `0x19` |
| 42 | `0b101010` | `0x2a` |

### Task 5.4 - Text encoding

- Uppercase `A` has ASCII decimal code 65.
- Lowercase `a` has ASCII decimal code 97.
- An encoding standard maps characters to numbers so computers can store and exchange text consistently. UTF-8 can represent many characters beyond basic ASCII, such as `₹`.

## 5. Difficulties faced
The converter prints base prefixes (`0b` and `0x`), which can look like part of the number.

## 6. How I resolved them
The prefixes identify whether the displayed value is binary or hexadecimal; the digits after each prefix are the converted value.

## 7. Evidence / files
- `number_converter.py`
- This README with conversion working, Python checks and converter test outputs

## 8. Commit details
The converter was previously committed with the message `Build number converter and practise data representation`. The verified test results and required conversion notes were added in a follow-up commit.
