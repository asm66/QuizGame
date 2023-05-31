import time

# Quiz Game

# Define a list of questions and answers
questions = [
    "What is the capital of France?",
    "What is the largest planet in our solar system?",
    "What is the tallest mammal?",
    "What is the smallest country in the world?",
    "What is the meaning of the acronym WYSIWYG?",
    "Who founded Apple Computer?",
    "Who is the maker of the iPhone?"
]

answers = [
    "Paris",
    "Jupiter",
    "Giraffe",
    "Vatican City",
"What you see is what you get",
    "Steve Jobs",
    "Apple"
]

# Define a function to ask a question and check the answer
def ask_question(question, answer, timeout):
    print(question)
    user_answer = input("Answer: ")
    start_time = time.time()
    while time.time() - start_time < timeout:
        if user_answer.lower() == answer.lower():
            print("Correct!")
            return True
        else:
            print("Incorrect!")
            return False
    print("Time's up!")
    return False
    user_answer = input("Answer: ")

# Set the total quiz time to len(questions) * 10 seconds
total_time = len(questions) * 10  # seconds

# Loop through the questions and ask them one by one
num_correct = 0
timeout = 10  # seconds
start_time = time.time()

for i in range(len(questions)):
    if time.time() - start_time > total_time:
        print("Time's up! You didn't finish the quiz.")
        break
    if ask_question(questions[i], answers[i], timeout):
        num_correct += 1

# Calculate the user's score as a percentage
score = num_correct / len(questions) * 100

# Print the final score
print("You got", num_correct, "out of", len(questions), "questions correct.")
print("Your score is", score, "%.")
