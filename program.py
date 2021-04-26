def program():
    import random
    print("Welcome To The Number Guessing Game ! In This Game You Will Have To Correctly Guess A Number Between 1 And 10 .")
    num = random.randint(1, 10)
    user = int(input("Guess Any Number Between 1 And 10 : "))
    if user == num:
        print("You Guessed The Correct Number ! You Win 🏆 ! ")
    elif user > num and user < 11:
        print("It 's Higher ! You Lose !")
    elif user < num and user > 0:
        print("It 's Lower ! You Lose !")
    elif user > 10 or user < 1:
        print("Enter A Number Between 1 To 10 . Restart The Application And Try Again .")


if __name__ == '__main__':
    program()
