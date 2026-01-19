# Create a dictionary of people with their personal info
people = {
    "0001": {"Аты": "Айбек", "Туған күні": "2005-01-15", "Телефон": "+77011234567"},
    "0002": {"Аты": "Аружан", "Туған күні": "2004-09-10", "Телефон": "+77023456789"},
    "0003": {"Аты": "Мирас", "Туған күні": "2003-07-05", "Телефон": "+77039876543"}
}

# Ask user for ID
person_id = input("ЖСН немесе ID енгізіңіз: ")

# Show personal info if ID exists
if person_id in people:
    info = people[person_id]
    print("Толық ақпарат:")
    for key, value in info.items():
        print(f"{key}: {value}")
else:
    print("Адам табылған жоқ.")

