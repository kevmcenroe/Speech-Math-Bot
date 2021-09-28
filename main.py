import pyttsx3
engine = pyttsx3.init()

import speech_recognition
recognizer = speech_recognition.Recognizer();


def recogniseVoice():
    with speech_recognition.Microphone() as source:
        print("Say something")
        audio = recognizer.listen(source)

    print("Google speech recognition thinks you said: ")
    print(recognizer.recognize_google(audio))
    return recognizer.recognizegoogle(audio)


def speak(message):
    engine.say(message)
    engine.runAndWait()


def speakAndPrint(message):
    print(message)
    engine.say(message)
    engine.runAndWait()


def solveProblem(category):
    speakAndPrint(f"\nYou have chosen {category}!")
    while True:
        try:
            speakAndPrint("Enter a first number ")
            x = int(input())
            speak(x)

            speakAndPrint("Enter a second number ")
            y = int(input())
            speak(y)

            if category == "Addition":
                answer = x + y
                speakAndPrint(f"{x} plus {y} is {answer}")
            elif category == "Subtraction":
                answer = x - y
                speakAndPrint(f"{x} minus {y} is {answer}")
            elif category == "Multiplication":
                answer = x * y
                speakAndPrint(f"{x} multiplied by {y} is {answer}")
            elif category == "Division":
                answer = x / y
                speakAndPrint(f"{x} divided by {y} is {answer}")
            return
        except:
            speakAndPrint("Please enter valid numbers");


#Referenced from https://jaxenter.com/implement-switch-case-statement-python-138315.html
def selectProblem(input):
    switcher = {
        1: "Addition",
        2: "Subtraction",
        3: "Multiplication",
        4: "Division"
    }
    solveProblem(switcher.get(input))


def main():
    speakAndPrint("What kind of problem would you like me to solve?")
    print("1 = Addition")
    print("2 = Subtraction")
    print("3 = Multiplication")
    print("4 = Division")

    option = (int)(input())
    selectProblem(option)


speakAndPrint("Welcome to Math Bot!")
while True:
    main()
    print()