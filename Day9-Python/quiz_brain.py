class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
            # This code is too long:
            # if self.question_number == len(self.question_list):
            #     return False
            # else: return True

            # Simplified version:
            return self.question_number < len(self.question_list)
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question.text} 'True' or 'False': " ).capitalize()
        self.check_answer(user_answer, current_question.answer)
        
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("Your answer is correct!")
            self.score += 1
        else: 
            print("Your answer is wrong.")
        print(f"The correct answer is {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}.")
         
        
    
    
