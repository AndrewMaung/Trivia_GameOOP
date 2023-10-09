class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.count = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{current_question}:{current_question.text}(True or False):")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self,user_answer,answer):
        if user_answer.lower() == answer.lower():
            print("You got it right!")
            self.count += 1
        else:
            print("That's wrong")
        print(f"The correct answer was {answer}")
        print(f"Your current score is {self.count}/{self.question_number}")


