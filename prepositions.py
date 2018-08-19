# -*- coding: utf-8 -*-

import sys
import numpy as np

def main():
    list_de = ["accepter", "avoir peur", "choisir", "conseiller", "décider", "demander", "dire", "empêcher qqun",
               "essayer", "éviter", "finir", "oublier", "permettre à qqun", "promettre à qqun", "refuser", "regretter", "rêver",
               "venir"]
    list_a = ["aider qqun", "arriver", "chercher", "commencer", "continuer", "enseigner à qqun", "hésiter",
              "inviter qqun", "réussir", "servir", "tenir"]
    n = start()
    main_loop(n, list_de, list_a)


def start():
    number_words = int(input("How many words would you like to see?"))
    return number_words

def main_loop(n, list_de, list_a):
    num_a = len(list_a)
    num_de = len(list_de)
    total_words = num_a + num_de
    for number in range(n):
        random_num = np.random.randint(low=0, high=total_words)
        word = exercise(random_num, list_de, list_a)
        answer = evaluation(list_de, list_a, word)
        exercise_input(answer, word)


def exercise(random_num, list_de, list_a):
    total_list = list_a + list_de
    word = total_list[random_num]
    return word

def evaluation(list_de, list_a, word):
    if word in list_de:
        answer = "de"
    elif word in list_a:
        answer = "a"
    else:
        sys.exit(1)
    return answer

def exercise_input(answer, word):
    user_response = input("What preposition goes with (à/de): {}".format(word))
    response_a = ("à", "a")
    response_de = ("de")
    if user_response in response_a:
        if answer == user_response:
            print("Bravo!")
        else:
            print("Dommage...")
    elif user_response in response_de:
        if answer == user_response:
            print("Bravo!")
        else:
            print("Dommage")
    else:
        print("Ceci n'est pas une option")

main()