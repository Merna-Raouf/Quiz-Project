from model import *

def getQuiz():
    """
    it allows the student to take the quiz and gets his mark
    :return:
    """
    Total=0
    Quizes = session.query(Quiz).all()
    for quiz in Quizes:
        print(quiz.name)
    name=input("Enter the name of the quiz: ")

    for quiz in Quizes:
        if (quiz.name==name):
            print(f"The Duration of the quiz is : {quiz.Duration} minutes")
            print("Let's start the quiz!")

            Mcq=session.query(MCQ).all()
            for q in Mcq:
                if(q.Quiz_id==quiz.id):
                    print(q.Question)
                    print(q.first_Choice)
                    print(q.second_Choice)
                    print(q.third_Choice)
                    print(q.fourth_Choice)
                    answer=input("Answer: ")
                    if(answer==q.answer):
                        Total+=q.mark

            Trueorfalse=session.query(TrueOrFalse).all()
            for q in Trueorfalse:
                if (q.Quiz_id == quiz.id):
                    print(q.Question)
                    answer = input("Answer: ")
                    if (bool(answer) == q.answer):
                        Total += q.mark

            Essay = session.query(Essay_Question).all()
            for q in Essay:
                if (q.Quiz_id == quiz.id):
                    print(q.Question)
                    answer = input("Answer: ")
                    if (answer == q.answer):
                        Total += q.mark

            integer_qus = session.query(Integer_Question).all()
            for q in integer_qus:
                if (q.Quiz_id == quiz.id):
                    print(q.Question)
                    answer = input("Answer: ")
                    if (int(answer) == q.answer):
                        Total += q.mark

            float_qus = session.query(Float_Question).all()
            for q in float_qus:
                if (q.Quiz_id == quiz.id):
                    print(q.Question)
                    answer = input("Answer: ")
                    if (float(answer) == q.answer):
                        Total += q.mark
            print(f"Mark: {Total}")
