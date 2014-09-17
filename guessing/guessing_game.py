import random

tries = 6
attempts = 0
secret = random.randint(1, 99)
guess = 0

print('Access DENIED: this system is locked with a code between 1-99')

while guess != secret and attemps < tries:
    remaining = tries - attempts
    print('you have' + str(remaining) + 'remaining attempts')
    guess = int(input("enter code now..."))
    if guess < secret:
        print("code: FAIL:  Too low. don't you know any smaller numbers")
    if guess > secret:
        print("code: FAIL:  Too high. Cool your boots and try something smaller")
    attempts = attempts + 1

if guess==secret:
    print("Confirmed"

