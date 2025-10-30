import random

Questions_list = {
    "What is the largest planet in our solar system?": "jupiter",
    "Who painted the Mona Lisa?": "leonardo da vinci",
    "What is the capital city of Australia?": "canberra",
    "Which ocean is the deepest on Earth?": "pacific",
    "How many bones are in the adult human body?": "206",
    "What is the hardest natural substance on Earth?": "diamond",
    "Which country is known as the Land of the Rising Sun?": "japan",
    "Who wrote the play 'Hamlet'?": "william shakespeare",
    "What is the chemical symbol for water?": "h2o",
    "Which planet is closest to the Sun?": "mercury",
    "What is the largest mammal in the world?": "blue whale",
    "In what year did man first land on the moon?": "1969",
    "Which animal is known for its black and white stripes?": "zebra",
    "What is the smallest prime number?": "2",
    "Which element has the chemical symbol 'O'?": "oxygen",
    "Who invented the telephone?": "alexander graham bell",
    "How many continents are there on Earth?": "7",
    "What is the capital city of Canada?": "ottawa",
    "Which bird is known for its colorful tail feathers?": "peacock",
    "Which language has the most native speakers worldwide?": "mandarin"
}

#A function for quiz running
def run_quiz(questions):
    score = 0
    for question, answer in questions.items():
        print(question)
        user_answer = input("Answer: ").strip().lower()
        if user_answer == answer:
            score += 1
    return score

#Selecting unique questions
selected_questions = dict(random.sample(list(Questions_list.items()), 5))