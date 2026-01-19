# Create a small dictionary of words and their meanings
word_dict = {
    "Алма": "Жеміс түрі, қызыл немесе жасыл болады",
    "Python": "Бағдарламалау тілі",
    "Дос": "Жақын адам, сенімді жолдас"
}

# Ask user to input a word
word = input("Сөзді енгізіңіз: ")

# Check if word exists in dictionary
if word in word_dict:
    print("Анықтама:", word_dict[word])
else:
    print("Бұл сөз сөздікте жоқ.")
