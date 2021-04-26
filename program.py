def program():
    import random
    print("Welcome To The Number Guessing Game ! In This Game You Will Have To Correctly Guess A Number Between 1 And 10 .")
    num = random.randint(1, 10)
    user = int(input("Guess Any Number Between 1 And 10 : "))
    if user == num:
        print("You Guessed The Correct Number ! You Win 🏆 ! ")
    elif user > num:
        print("It 's Higher ! You Lose !")
    elif user < num:
        print("It 's Lower ! You Lose !")


if __name__ == '__main__':
    program()
