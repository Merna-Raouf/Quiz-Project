from model import *
import time
import signal
def getQuiz():
    """
    it allows the student to take the quiz and gets his mark
    :return:
    """
    start = time.time()
    Total=0
    Quizes = session.query(Quiz).all()
    for quiz in Quizes:
        print("{} . {} ".format(quiz.id,quiz.name))
    ID= input("Enter the id of the quiz: ")

    quiz=session.query(Quiz).filter(Quiz.id == int(ID))
    for row in quiz:
        print(f"The Duration of the quiz is : {row.Duration} minutes")
        print("Let's start the quiz!")
        Mcq=session.query(MCQ).filter(MCQ.Quiz_id == int(ID))
        for q in Mcq :
            print(q.Question)
            print(q.first_Choice)
            print(q.second_Choice)
            print(q.third_Choice)
            print(q.fourth_Choice)
            answer = input("Answer: ")
            if(answer==q.answer):
                Total+=q.mark

        Trueorfalse = session.query(TrueOrFalse).filter(TrueOrFalse.Quiz_id == int(ID))
        for q in Trueorfalse:
            print(q.Question)
            answer = input("Answer: ")
            if (bool(answer) == q.answer):
                Total += q.mark


        Essay = session.query(Essay_Question).filter(Essay_Question.Quiz_id == int(ID))
        for q in Essay:
            print(q.Question)
            answer = input("Answer: ")
            if (answer == q.answer):
                Total += q.mark

        integer_qus = session.query(Integer_Question).filter(Integer_Question.Quiz_id == int(ID))
        for q in integer_qus:
            print(q.Question)
            answer = input("Answer: ")
            if (int(answer) == q.answer):
                Total += q.mark

        float_qus = session.query(Float_Question).filter(Float_Question.Quiz_id == int(ID))
        for q in float_qus:
            print(q.Question)
            answer = input("Answer: ")
            if (float(answer) == q.answer):
                Total += q.mark

        print(f"Mark: {Total}")

