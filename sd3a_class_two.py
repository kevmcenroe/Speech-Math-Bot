from time import sleep

from sys import argv



def get_positive_integer():
    while True:
        n = int(input("Positive integer"))
        if n > 0:
            break
    return n

def printQuestionMarks(number):
    for i in range(number):
        print("?", end = "")


"""
    INPUT:
    One number which gives the size of the pyramid. Only one number needed as the
    width and the height have to be equal. For example, a pyramid of width 3 and height 7
    makes no sense.
    
    OUTPUT:
    Prints a pyramid
"""
def print_pyramid(size):
    for i in range(height):
        for j in range((i + 1)):
            print("#", end = "")
        print()

print

def grow_integer(start):
    while True:
        start *= 10
        sleep
        print(start)

grow_integer(50)

def play_list():
    scores = []
    scores.append(72)
    scores.append(73)
    scores.append(33)
    print(f"Average: {sum(scores) / len(scores)}")

def command_line_args():
    for i in range(len(argv)):
        print(argv[i])

command_line_args()

def play_dictionary():
    people = {
        "John" : "083-1234567",
        "Himansh" : "086-1234765",
        "Mark" : "085-4321454"
    }

    if "Amrita" in people:
        print("Found")
    else:
        print("Not Found")