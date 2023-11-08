from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for line in question_data:
    question_text = line['text']
    question_answer = line['answer']
    new_question = Question(text=question_text, answer=question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(q_list=question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/ {len(question_bank)}")
