import pandas as pd
from utils import *
import time


def main():
    # text = input('Please Enter your condition: ').lower()
    # Diseases(filtered_sentence=removeWords(text))

    print('Doc Bot: '+'Hi! What is your name?')

    while(True):
        user_input = input()
        userDetail(user_input)


if __name__ == "__main__":

    start_time = time.process_time()
    main()
    print(time.process_time() - start_time, "seconds")
