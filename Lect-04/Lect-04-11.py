"""
ans = input("Enter a word: ").strip()
while ans != "END":
    print(f"You entered: {ans}")
    ans = input("Enter a word: ").strip()
"""
while (ans := input("Enter a word: ").strip()) != "END":
    print(f"You entered: {ans}")