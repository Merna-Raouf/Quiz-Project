from addQuiz import *
from getQuiz import *


def main():
    mode=0

    while (mode !=1 and mode!=2):
        try:
            mode = input("""Select your mode:
                    Enter 1 for Teacher
                    Enter 2 for Student
                    """)
            mode=int(mode)
            if (mode == 1):
                Add_Quiz()

            elif (mode == 2):
                getQuiz()

        except:
            print("please Enter the mode again: ")


if __name__ == '__main__':
  main()