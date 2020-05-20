from model import *

def Add_MCQ(Quiz):
    """
    it adds new MCQ question to the quiz
    :param Quiz:
    :return:
    """
    num = input('How many Questions do you need to add ? ')
    for i in range(int(num)):
        Question = input('Enter the Question: ')
        first_choice = input('Enter the first choice: ')
        second_choice = input('Enter the second choice: ')
        third_choice = input('Enter the third choice: ')
        fourth_choice = input('Enter the fourth choice: ')
        answer = input('Enter the right answer of the Question: ')
        mark = input('Enter the mark of the Question: ')

        new = MCQ(Question, first_choice, second_choice, third_choice, fourth_choice, answer, mark, Quiz.id)
        Quiz.Mcq.append(new)
        session.add(new)
        session.commit()


def Add_TrueOrFalse(Quiz):
    """
    it adds new True or false question to the Quiz
    :param Quiz:
    :return:
    """
    num = input('How many Questions do you need to add ? ')
    for i in range(int(num)):
        Question = input('Enter the Question: ')
        answer = input('Enter the right answer of the Question: ')
        mark = input('Enter the mark of the Question: ')

        new = TrueOrFalse(Question,bool(answer), mark, Quiz.id)
        Quiz.TrueOrFalse.append(new)
        session.add(new)
        session.commit()


def Add_EssayQuestion(Quiz):
    """
    it adds new Essay Question question to the Quiz
    :param Quiz:
    :return:
    """
    num = input('How many Questions do you need to add ? ')
    for i in range(int(num)):
        Question = input('Enter the Question: ')
        answer = input('Enter the right answer of the Question: ')
        mark = input('Enter the mark of the Question: ')
        new = Essay_Question(Question,answer, mark, Quiz.id)
        Quiz.Essay_Question.append(new)
        session.add(new)
        session.commit()


def Add_IntegerQuestion(Quiz):
    """
    it adds new Integer question to the Quiz
    :param Quiz:
    :return:
    """
    num = input('How many Questions do you need to add ? ')
    for i in range(int(num)):
        Question = input('Enter the Question: ')
        answer = input('Enter the right answer of the Question: ')
        mark = input('Enter the mark of the Question: ')

        new = Integer_Question(Question,answer, mark, Quiz.id)
        Quiz.Integer_Question.append(new)
        session.add(new)
        session.commit()


def Add_FloatQuestion(Quiz):
    """
    it adds new Float question to the Quiz
    :param Quiz:
    :return:
    """
    num = input('How many Questions do you need to add ? ')
    for i in range(int(num)):
        Question = input('Enter the Question: ')
        answer = input('Enter the right answer of the Question: ')
        mark = input('Enter the mark of the Question: ')

        new = Float_Question(Question,answer, mark, Quiz.id)
        Quiz.Float_Question.append(new)
        session.add(new)
        session.commit()


def Add_Quiz():
    """
    it allows the teacher to add a new quiz
    :return:
    """
    name=input('Enter the name of the Quiz: ')
    Duration=input('Enter the Duration of the Quiz: ')
    quiz = Quiz(name=str(name),Duration=Duration)
    session.add(quiz)
    session.commit()
    MORE='Y'

    while(MORE=='Y'):
        TypeofQuestion=input("""
        Choose the Type of the Question
        1.MCQ
        2.True or False
        3.Essay Question
        4.Integer Question
        5.Float Question
        Enter The Number of the Question:
        """)

        if (TypeofQuestion=='1'):
            Add_MCQ(quiz)

        elif (TypeofQuestion=='2'):
            Add_TrueOrFalse(quiz)

        elif (TypeofQuestion == '3'):
            Add_EssayQuestion(quiz)

        elif (TypeofQuestion == '4'):
            Add_IntegerQuestion(quiz)

        elif (TypeofQuestion == '5'):
            Add_FloatQuestion(quiz)

        MORE=input("""Do you want to add more questions? 
        Enter Y for YES
        Enter N for NO 
        """)
        while (MORE != "Y" and MORE!= "N"):
            print("please Try again")
            MORE = input("""Do you want to add more questions? 
                   Enter Y for YES
                   Enter N for NO 
                   """)



