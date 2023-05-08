from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for data in question_data:
    question = Question(data['question'], data['correct_answer'])
    # question_bank.append({'text' : question.text, 'answer' : question.answer})
    # code for more easy access to the data:
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("\nHoorraayy!! You've completed the test!")
print(f"Your final score was {quiz.score}/{quiz.question_number}. ")