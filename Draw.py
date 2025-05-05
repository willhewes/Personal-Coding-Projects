import random, sys, time

print("Fast draw - reflex tester")
time.sleep(1)
print("When you see \"draw\", you have 0.3 seconds to press enter")
print("but if you press enter too early you lose")
time.sleep(1)
input("Press enter to begin")

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
    elif timeElapsed < 0.3:
        print(f"You took {timeElapsed} seconds to draw")
        print("You win")
    else:
        print(f"You took {timeElapsed} seconds to draw")
        print("You LOSE!")

    print("Enter \"exit\" to stop, or press Enter to play again")
    response = input(">").lower()
    if response == "exit":
        print("Thanks for playing")
        sys.exit()
