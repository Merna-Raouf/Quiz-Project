from addQuiz import *
from getQuiz import *

def main():
    mode=input("""Select your mode:
    Enter 1 for Teacher
    Enter 2 for Student
    """)

    if (mode=='1'):
        Add_Quiz()

    elif(mode=='2') :
        getQuiz()

if __name__ == '__main__':
    main()