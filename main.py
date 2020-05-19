import sys
from addQuiz import *
from getQuiz import *
from time import time
import multiprocessing


def program():
    mode = input("""Select your mode:
        Enter 1 for Teacher
        Enter 2 for Student
        """)

    if (mode == '1'):
        Add_Quiz()

    elif (mode == '2'):
        getQuiz()


def main():
    # Start foo as a process
    p = multiprocessing.Process(target=program,name="program",args=())
    p.start()

    # Wait 10 seconds for foo
    time.sleep(50)

    # Terminate foo
    p.terminate()

    # Cleanup
    p.join()


def timer():
    duration=program()
    start = time.time()
    if (time.time() - start <duration * 60):
        sys.exit()


if __name__ == '__main__':
  main()