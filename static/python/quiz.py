from flask import Flask, redirect, render_template, request

question_one = "1. Which planet is nearest to the sun?\na. Venus\nb. Mercury\nc. Pluto\nType the letter of your answer"
question_two = "2. What is the largest planet in the solar system?\na. Jupiter\nb. Uranus\nc. Saturn\nType the letter of your answer"
question_three = "3. Between which two planets do you find the asteroid belt?\na. Earth and Mars\nb. Mars and Jupiter\nc. Jupiter and Saturn\nType the letter of your answer"
question_four = "4. What is the name of the largest object in the asterid belt?\na. Ceres\nb. Juno\nc. Hygiea\nType the letter of your answer"
question_five = "5. Now pluto has been downgraded as a planet, which planet is the furthest from the sun?\na. Uranus\nb. Neptune\nc. Venus\nType the letter of your answer"
question_six = "6. How many planets are there?\na. Eight\nb. Six\nc. Seven\nType the letter of your answer"
question_seven = "7. How many of these are gas giants?\na. Five\nb. Three\nc. Four\nType the letter of your answer"
question_eight = "8. Umbriel is a moon of which planet?\na. Saturn\nb. Neptune\nc. Uranus\nType the letter of your answer"
question_nine = "9. How many moons orbit Mars?\na. One\nb. Two\nc. Three\nType the letter of your answer"
question_ten = "10. Which of these is a moon of Mars?\na. Makemake\nb. Europa\nc. Phobos\nType the letter of your answer"
question_eleven = "11. Pluto is the largest object in which part of the solar system?\na. Kuiper Belt\nb. Inner Planets\nc. Oort Cloud\nType the letter of your answer"
question_twelve = "12. Which of these is not one of Plutos moons?\na. Hydra\nb. Io\nc. Nix\nType the letter of your answer"
question_thirteen = "13. Which planet is famous for its large rings?\na. Venus\nb. Neptune\nc. Saturn\nType the letter of your answer"
question_fourteen = "14. Which of the planets is thought to have the warmest climate?\na. Mars\nb. Venus\nc. Mercury\nType the letter of your answer"
question_fifteen = "15. After the sun, which is the nearest star to the solar system at four light years?\na. Proxima Centauri\nb. Barnards Star\nc. Centauri A\nType the letter of your answer"
question_sixteen = "16. The solar system is a part of which galaxy?\na. The Sombrero Galaxy\nb. Andromeda\nc. Milky Way\nType the letter of your answer"
question_seventeen = "17. Approximately how old is the solar system thought to be?\na. 6 Billion Years\nb. 4.5 Billion Years\nc. 3 Billion Years\nType the letter of your answer"
question_eighteen = "18. When the moon passes across the sun and blocks the daylight, this is called a solar...\na. Eclipse\nb. Storm\nc. Flair\nType the letter of your answer"
question_nineteen = "19. Makemake is part of the asteroid belt. True or false?\na. True\nb. False\nc. There is no such object\nType the letter of your answer"
question_twenty = "20. Which of these is a comet?\na. Halley's\nb. Eris\nc. Callisto\nType the letter of your answer"

"""

questions = [
    {
        "question": "Which planet is nearest to the sun?",
        "answers": 
            ["a. Venus",
            "b. Mercury",
            "c. Pluto"],
        "correct_answer": "b"
    },
    {
        "question": "What is the largest planet in the solar system?",
        "answers": 
            ["a. Jupiter",
            "b. Uranus",
            "c. Saturn"],
        "correct_answer": "a"
    },
    {
        "question": "Between which two planets do you find the asteroid belt?",
        "answers": 
            ["a. Earth and Mars",
            "b. Mars and Jupiter",
            "c. Jupiter and Saturn"],
        "correct_answer": "b"
    },
    {
        "question": "What is the name of the largest object in the asterid belt?",
        "answers": 
            ["a. Ceres",
            "b. Juno",
            "c. Hygiea"],
        "correct_answer": "a"
    },
    {
        "question": "Now pluto has been downgraded as a planet, which planet is the furthest from the sun?",
        "answers": 
            ["a. Uranus",
            "b. Neptune",
            "c. Venus"],
        "correct_answer": "b"
    },
    {
        "question": "How many planets are there?",
        "answers": 
            ["a. Eight",
            "b. Six",
            "c. Seven"],
        "correct_answer": "a"
    },
    {
        "question": "How many of these are gas giants?",
        "answers": 
            ["a. Five",
            "b. Three",
            "c. Four"],
        "correct_answer": "c"
    },
    {
        "question": "Umbriel is a moon of which planet?",
        "answers": 
            ["a. Saturn",
            "b. Neptune",
            "c. Uranus"],
        "correct_answer": "c"
    },
    {
        "question": "How many moons orbit Mars?",
        "answers": 
            ["a. One",
            "b. Two",
            "c. Three"],
        "correct_answer": "b"
    },
    {
        "question": "Which of these is a moon of Mars?",
        "answers": 
            ["a. Makemake",
            "b. Europa",
            "c. Phobos"],
        "correct_answer": "c"
    },
    {
        "question": "Pluto is the largest object in which part of the solar system?",
        "answers": 
            ["a. Kuiper Belt",
            "b. Inner Planets",
            "c. Oort Cloud"],
        "correct_answer": "a"
    },
    {
        "question": "Which of these is not one of Plutos moons?",
        "answers": 
            ["a. Hydra",
            "b. Io",
            "c. Nix"],
        "correct_answer": "b"
    },
    {
        "question": "Which planet is famous for its large rings?",
        "answers": 
            ["a. Venus",
            "b. Neptune",
            "c. Saturn"],
        "correct_answer": "c"
    },
    {
        "question": "Which of the planets is thought to have the warmest climate?",
        "answers": 
            ["a. Mars",
            "b. Venus",
            "c. Mercury"],
        "correct_answer": "b"
    },
    {
        "question": "After the sun, which is the nearest star to the solar system at four light years?",
        "answers": 
            ["a. Proxima Centauri",
            "b. Bernards Star",
            "c. Centauri A"],
        "correct_answer": "a"
    },
    {
        "question": "The solar system is part of which galaxy?",
        "answers": 
            ["a. The Sombrero Galaxy",
            "b. Andromeda",
            "c. Milky Way"],
        "correct_answer": "c"
    },
    {
        "question": "Approximately how old is the solar system thought to be?",
        "answers": 
            ["a. 6 Billion Years",
            "b. 4.5 Billion Years",
            "c. 3 Billion Years"],
        "correct_answer": "b"
    },
    {
        "question": "When the moon passes across the sun and blocks the daylight, this is called a solar...",
        "answers": 
            ["a. Eclipse",
            "b. Storm",
            "c. Flair"],
        "correct_answer": "a"
    },
    {
        "question": "Makemake is part of the asteroid belt. True or false?",
        "answers": 
            ["a. True",
            "b. False",
            "c. There is no such object?"],
        "correct_answer": "b"
    },
    {
        "question": "Which of these is a comet?",
        "answers":  
            ["a. Halley's",
            "b. Eris",
            "c. Callisto"],
        "correct_answer": "a"
    }
]

score = 0

for ask_question in questions:
    print(ask_question["question"])
    for answer_choices in questions["answers"]:
        print(answer_choices)
        
    answer = input("Type your answer: ")
    if answer.lower().strip() == questions["correct_answer"]:
        score += 1
"""

def solar_system_quiz():
    
    score = 0
  
    #Question one
    print(question_one)
    question_one_answer = input()
    if question_one_answer.lower() == "b":
        score += 1
    elif question_one_answer.lower() != "a" and question_one_answer.lower() != "c":
        print("Invalid input... try again")

    #Question two  
    print(question_two)
    question_two_answer = input()
    if question_two_answer.lower() == "a":
        score += 1
    elif question_one_answer.lower() != "b" and question_one_answer.lower() != "c":
        print("Invalid input... try again")
        
    #Question three            
    print(question_three)
    question_three_answer = input()
    if question_three_answer.lower() == "b":
        score += 1
    elif question_one_answer.lower() != "a" and question_one_answer.lower() != "c":
        print("Invalid input... try again")
        
    #Question four            
    print(question_four)
    question_four_answer = input()
    if question_four_answer.lower() == "a":
        score += 1
    elif question_one_answer.lower() != "b" and question_one_answer.lower() != "c":
        print("Invalid input... try again")
        
    #Question five            
    print(question_five)
    question_five_answer = input()
    if question_five_answer.lower() == "b":
        score += 1
    elif question_one_answer.lower() != "a" and question_one_answer.lower() != "c":
        print("Invalid input... try again")
        
    #Question six            
    print(question_six)
    question_six_answer = input()
    if question_six_answer.lower() == "a":
        score += 1
    elif question_one_answer.lower() != "b" and question_one_answer.lower() != "c":
        print("Invalid input... try again")
        
    #Question seven            
    print(question_seven)
    question_seven_answer = input()
    if question_seven_answer.lower() == "c":
        score += 1
    elif question_one_answer.lower() != "a" and question_one_answer.lower() != "b":
        print("Invalid input... try again")
        
    #Question eight            
    print(question_eight)
    question_eight_answer = input()
    if question_eight_answer.lower() == "c":
        score += 1
    elif question_one_answer.lower() != "a" and question_one_answer.lower() != "b":
        print("Invalid input... try again")
        
    #Question nine            
    print(question_nine)
    question_nine_answer = input()
    if question_nine_answer.lower() == "b":
        score += 1
    elif question_one_answer.lower() != "a" and question_one_answer.lower() != "c":
        print("Invalid input... try again")
        
    #Question ten            
    print(question_ten)
    question_ten_answer = input()
    if question_ten_answer.lower() == "c":
        score += 1
    elif question_one_answer.lower() != "a" and question_one_answer.lower() != "b":
        print("Invalid input... try again")
        
    #Question eleven            
    print(question_eleven)
    question_eleven_answer = input()
    if question_eleven_answer.lower() == "a":
        score += 1
    elif question_one_answer.lower() != "b" and question_one_answer.lower() != "c":
        print("Invalid input... try again")
        
    #Question twelve            
    print(question_twelve)
    question_twelve_answer = input()
    if question_twelve_answer.lower() == "b":
        score += 1
    elif question_one_answer.lower() != "a" and question_one_answer.lower() != "c":
        print("Invalid input... try again")
        
    #Question thirteen            
    print(question_thirteen)
    question_thirteen_answer = input()
    if question_thirteen_answer.lower() == "c":
        score += 1
    elif question_one_answer.lower() != "a" and question_one_answer.lower() != "b":
        print("Invalid input... try again")
        
    #Question fourteen            
    print(question_fourteen)
    question_fourteen_answer = input()
    if question_fourteen_answer.lower() == "b":
        score += 1
    elif question_one_answer.lower() != "a" and question_one_answer.lower() != "c":
        print("Invalid input... try again")
        
    #Question fifteen            
    print(question_fifteen)
    question_fifteen_answer = input()
    if question_fifteen_answer.lower() == "a":
        score += 1
    elif question_one_answer.lower() != "b" and question_one_answer.lower() != "c":
        print("Invalid input... try again")
        
    #Question sixteen            
    print(question_sixteen)
    question_sixteen_answer = input()
    if question_sixteen_answer.lower() == "c":
        score += 1
    elif question_one_answer.lower() != "a" and question_one_answer.lower() != "b":
        print("Invalid input... try again")
        
    #Question seventeen            
    print(question_seventeen)
    question_seventeen_answer = input()
    if question_seventeen_answer.lower() == "b":
        score += 1
    elif question_one_answer.lower() != "a" and question_one_answer.lower() != "c":
        print("Invalid input... try again")
        
    #Question eighteen            
    print(question_eighteen)
    question_eighteen_answer = input()
    if question_eighteen_answer.lower() == "a":
        score += 1
    elif question_one_answer.lower() != "b" and question_one_answer.lower() != "c":
        print("Invalid input... try again")
        
    #Question nineteen            
    print(question_nineteen)
    question_nineteen_answer = input()
    if question_nineteen_answer.lower() == "b":
        score += 1
    elif question_one_answer.lower() != "a" and question_one_answer.lower() != "c":
        print("Invalid input... try again")
        
    #Question twenty            
    print(question_twenty)
    question_twenty_answer = input()
    if question_twenty_answer.lower() == "a":
        score += 1
    elif question_one_answer.lower() != "b" and question_one_answer.lower() != "c":
        print("Invalid input... try again")
        
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
            
    if score == 20:
        print("Thanks for playing {}. You scored {}. That is a perfect score. Very well done!".format(first_name, score))
    elif score > 15 and score <= 19:
        print("Thanks for playing {}. You scored {} out of 20. Very good score. You know your stuff!".format(first_name, score))
    elif score > 10 and score <= 15:
        print("Thanks for playing {}. You scored {} out of 20. Good effort!".format(first_name, score))
    elif score > 0 and score <= 10:
        print("Thanks for playing {}. You only scored {} out of 20. That's not a good score. Go to the Solar System info section.".format(first_name, score))
    else:
        print("Thanks for playing {}. You scored {} out of 20. Go to Solor System info section.".format(first_name, score))
        
def write_score_to_file():
    message = []
    with open("assets/data/results.txt", "a+") as chat_messages:
        message = chat_messages.readlines()
    return message
 
if __name__ == '__main__':
    solar_system_quiz()