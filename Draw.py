import random, sys, time

print("Fast draw - reflex tester")
time.sleep(1)
print("When you see \"draw\", you have 0.3 seconds to press enter")
print("but if you press enter too early you lose")
time.sleep(1)
difficulty = [0.5, 0.3, 0.1]

win_counter = 0
loss_counter = 0
best_time = None

while True:
    while True:
        response = input("Input 1 for easy, 2 for hard, 3 for unfair: ")
        if response in ("1", "2", "3"):
            break
        print("Invalid input. Please enter 1, 2, or 3")

    time.sleep(2)
    print()
    print("This towns not big enough for the two of us")
    time.sleep(random.randint(20, 50) / 10)
    print("DRAW!")

    drawTime = time.time()
    input()
    timeElapsed = time.time() - drawTime
    timeElapsed = round(timeElapsed, 4)

    if best_time is None or 0.01 < timeElapsed < best_time:
        best_time = timeElapsed
        print(f"You beat your best time! Your new best time is {best_time}")

    if timeElapsed < 0.01:
        print("You drew too early")
    elif timeElapsed < difficulty[int(response) - 1]:
        print(f"You took {timeElapsed} seconds to draw")
        print("You win")
        time.sleep(1)
        win_counter += 1
        print(f"You have {win_counter} wins and {loss_counter} losses")
    else:
        print(f"You took {timeElapsed} seconds to draw")
        print("You LOSE!")
        time.sleep(1)
        loss_counter += 1
        print(f"You have {win_counter} wins and {loss_counter} losses")

    time.sleep(1)
    print("Enter \"exit\" to stop, or press Enter to play again")
    leave = input(">").lower()
    if leave == "exit":
        print("Thanks for playing")
        sys.exit()
