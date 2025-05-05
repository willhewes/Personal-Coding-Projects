import random, sys, time

print("Fast draw - reflex tester")
time.sleep(1)
print("When you see \"draw\", you have 0.3 seconds to press enter")
print("but if you press enter too early you lose")
time.sleep(1)
response = input("Input 1 for easy, 2 for hard, 3 for unfair")
difficulty = [0.5, 0.3, 0.1]

while True:
    print()
    print("This towns not big enough for the two of us")
    time.sleep(random.randint(20, 50) / 10)
    print("DRAW!")

    drawTime = time.time()
    input()
    timeElapsed = time.time() - drawTime
    timeElapsed = round(timeElapsed, 4)

    if timeElapsed < 0.01:
        print("You drew too early")
    elif timeElapsed < difficulty[int(response) - 1]:
        print(f"You took {timeElapsed} seconds to draw")
        print("You win")
    else:
        print(f"You took {timeElapsed} seconds to draw")
        print("You LOSE!")

    print("Enter \"exit\" to stop, or press Enter to play again")
    leave = input(">").lower()
    if leave == "exit":
        print("Thanks for playing")
        sys.exit()
