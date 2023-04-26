import random

def computerguess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            # It is needed as randint produces an error is both limits are equal
            # If we give this in while, we will not get the exact correct number as it breaks the loop before
            guess = random.randint(low, high)
        else:
            guess = low # can also be equal to high as low = high
        feedback = input(f'Is {guess} is too low(L) or too high(H) or correct(C)?: ').lower()
        # lower() is needed as we are using lower case letters for comparision
        if feedback == 'l':
            low = guess + 1
        elif feedback == 'h':
            high = guess - 1
    print(f'Yay! The computer guessed your number {guess}, correctly!!!')

computerguess(10)