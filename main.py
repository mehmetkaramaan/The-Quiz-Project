from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []
for data in question_data:
    q_text = data['text']
    q_answer = data['answer']
    questions = Question(q_text,q_answer)
    question_bank.append(questions)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz.\nYour final score was: {quiz.user_points}/{quiz.question_number}")
