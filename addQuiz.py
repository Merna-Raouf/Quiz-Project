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
    print(num)
    for i in num:
        Question = input('Enter the Question: ')
        answer = input('Enter the right answer of the Question: ')
        mark = input('Enter the mark of the Question: ')

    new = TrueOrFalse(Question,answer, mark, Quiz.id)
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
    print(num)
    for i in num:
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
    print(num)
    for i in num:
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
    print(num)
    for i in num:
        Question = input('Enter the Question: ')
        answer = input('Enter the right answer of the Question: ')
        mark = input('Enter the mark of the Question: ')

    new = Float_Question(Question,answer, mark, Quiz.id)
    Quiz.Float_Question.append(new)
    session.add(new)
    session.commit()

def Add_Quiz():
    """
    to Add a q
    :return:
    """
    Duration=input('Enter the Duration of the Quiz: ')
    quiz = Quiz(Duration=Duration)
    session.add(quiz)
    session.commit()
    MORE='YES'
    while(MORE=='YES'):
        TypeofQuestion=input("""
        Choose the Type of the Question
        MCQ
        True or False
        Essay Question
        Integer Question
        Float Question
        """)

        if (TypeofQuestion=='MCQ'):
            Add_MCQ(quiz)

        elif (TypeofQuestion=='True or False'):
            Add_TrueOrFalse(quiz)

        elif (TypeofQuestion == 'Essay Question'):
            Add_EssayQuestion(quiz)

        elif (TypeofQuestion == 'Integer Question'):
            Add_IntegerQuestion(quiz)

        elif (TypeofQuestion == 'Float Question'):
            Add_FloatQuestion(quiz)

        MORE=input("""Do you want to add more questions? 
        YES
        NO 
        """)

Add_Quiz()
#records = session.query(Quiz).all()
#for record in records:
#    print(record)

