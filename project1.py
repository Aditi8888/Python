import random 
secret = random.randint(1,100)
attempts = 0
print("Welcome ! I'hve picked a number between 1 -100")
while True :
    guess = int(input("Your guess :"))
    attempts+= 1
    if guess < secret :
     print("TOO LOW")
    elif guess > secret:
        print("TOO HIGH!")
    else:
        print(f"\nCORRECT! The number was {secret}.")
        print(f"You got it in {attempts} attempts!")
        break