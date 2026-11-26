def main():
    raw = input("Enter a decimal number: ").strip()
    number = int(raw)
    print(f"Binary: {bin(number)}")
    print(f"Hexadecimal: {hex(number)}")


if __name__ == "__main__":
    main()
