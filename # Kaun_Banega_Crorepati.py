# Kaun_Banega_Crorepati
print("Kaun_Banega_Crorepati")
A1 = str(input("Enter Your Name: "))
print(f"Welcome to KBC {A1}")
total_score = 0

def ask_question(question, options, correct_answer, points):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}: {option}")
    user_answer = int(input("Enter Answer: "))
    if user_answer == correct_answer:
        global total_score
        total_score += points
        print(f"Congratulations! You Won {points}")
    else:
        print("Incorrect Answer")

# Question 1
ask_question("What is Polaris also known as?", ["North Star", "Sirius", "Betelgeuse", "R13A61"], 1, 500)

# Question 2
ask_question("Which Technology do the Latest Charger use?", ["Silicon", "Germanium", "Gallium Nitride", "Boron"], 3, 1000)

# Question 3
ask_question("Name the Fastest Unmanned Aircraft?", ["X-43A", "X-15", "SR-72", "F-22"], 1, 2000)

# Question 4
ask_question("Name the Fastest Spy Aircraft?", ["F-16", "SU-57", "SR-71", "F-22"], 3, 5000)

# Question 5
ask_question("Mother of Most of Modern Languages?", ["C", "C#", "C++", "Java"], 1, 10000)

# Question 6
ask_question("Who Discovered Expansion of Universe?", ["Einstein", "Hubble", "Oppenheimer", "Fermi"], 2, 25000)

# Question 7
ask_question("Which Country is known as Graveyard of Empires?", ["Iran", "Iraq", "Vietnam", "Afghanistan"], 4, 50000)

# Question 8
ask_question("First Indian to Travel in a Submarine?", ["Rash Behari Bose", "Netaji", "Savarkar", "Gandhi"], 2, 100000)

# Question 9
ask_question("Highest Mountain on Earth from SeaBed?", ["Mt_Everest", "Mauna Kea", "Mt_Fuji", "Mt_Vesuvis"], 2, 250000)

# Question 10
ask_question("Teacher of Plato?", ["Alexander", "Aristotle", "Socrates", "Archimedes"], 3, 500000)

# Display the final score
print(f"Total Score: {total_score}")
print("Thanks For Submitting The Quiz")
