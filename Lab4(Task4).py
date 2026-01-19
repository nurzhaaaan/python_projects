word = input("Enter a word: ")  # Asking user to enter a word
reverse = ''
for ch in word:
    reverse = ch + reverse
print("Reversed word:", reverse)

