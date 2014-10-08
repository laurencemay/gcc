import random,time
tries = 6
attempts = 0
secret = random.randint(1, 99)
guess = 0


def inputNumber():
    try:
        user_input = raw_input("enter a number between 1 and 99: ")
        if user_input == "end":
             exit(0)
        n = int(user_input)
        if n>99 or n<1:
            print("You are an IDIOT")
            time.sleep(0.25)
            return inputNumber()
        else:
            return n
    except ValueError:
        print("You are an IDIOT")
        time.sleep(0.25)
        return inputNumber()


print('Access DENIED: this system is locked with a code between 1-99')

while guess != secret and attempts < tries:
    remaining = tries - attempts

    print('you have ' + str(remaining) + ' remaining attempts')

    guess = inputNumber()
    if guess < secret:
        print("code: FAIL:  Too low. don't you know any bigger numbers")
    if guess > secret:
        print("code: FAIL:  Too high. Cool your boots and try something smaller")
    attempts = attempts + 1

if guess == secret:
    print("Confirmed")
    time.sleep(0.5)
    print("Access: ENABLED. Please proceed to the Nuclear Launch Stations. Have a nice day")
else:
    time.sleep(0.5)
    print("Access: LOCKED: Black helicopters have been sent to your location")
    time.sleep(1)
    print("Before you are terminated we would like you to know that the number was " + str(secret))