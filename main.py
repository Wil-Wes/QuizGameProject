# Step 2: Import Data list and question model
from question_model import Question
from question_model import Question
from data import question_data

# Step 3 Create question bank using the question_data that has been imported (hint: loops)

# 3a. Place to store our questions in the question bank, i.e. an empty list
question_bank = []

# 3b loop through question data
print(question_bank)

# 3b. loop through the question_data
for question in question_data:
    # 3c get a hold of question text and question answers from the question_data list
    question_text = question["question"]
    question_answer = question["correct answer"]
    # 3d Create a new question using imported class
    new_question = Question(question_text, question_answer)
    # 3e. Add question to the question_bank list
    question_bank.append(new_question)

print(question_bank[1].answer)

# 3f. Test to see if the loop working
# Should print out a list of Question objects

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz!", f"Your final score was: {quiz.score}/{quiz.question_number}")

# Step 6: Create new QuizBrain object using the QuizBrain Class and pass in the question_bank
quiz = QuizBrain(question_bank)

# 6a. Run the next_question() method on the object just created
# quiz.next_question()

# 7a. Create "game loop" (while loop) to run the game
while quiz.still_has_questions():
    # 7b. Move the next_question() method from step 6a into the while loop
    quiz.next_question()

# Step 9: Notify user when quiz is completed and show the final score
print("You've completed the quiz!", f"Your final score was: {quiz.score}/{quiz.question_number}")