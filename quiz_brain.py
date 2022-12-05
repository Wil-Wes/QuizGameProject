# Step 4 Bri ng up question and ask the user to answer the question
# All of quiz functionality will bei n this file
class QuizBrain:
    # 4b Create constructor to initialize the necessary attributes: question number and user score which will have default values and question list which will be passed into the constructor
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

def next_question(self):
    current_question = self.question_list[self.question_number]
    # 4d. Lists start at 0 so to display the question number for the next step increase question number by 1
    self.question_number += 1
    # 4e Show the numbber, text, and ask for the user's answer
    user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
    self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right! :)")
        else: 
            print("Wrong!!! :(")
    # 8f
    print(f"The correct answer was: {correct_answer}")
    # 8g displays user score out of how many questions asked
    print(f"Your current score is: {self.score}/{self.question_number}")

print("\n")