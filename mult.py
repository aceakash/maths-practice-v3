from random import shuffle
from time import time

multiples = list(range(2, 13))

times = []

while(True):
    print(" ")

    num = input("which multiplication table do you want to practise? ")
    num = int(num)
    shuffle(multiples)
    start_time = time()
    correct = 0
    for i in multiples:
        guess = input(f"{num} x {i} = ")
        guess = int(guess)
        
        if guess == i * num:
            print("Correct")
            correct += 1
        else:
            print(f"Wrong, {num} x {i} = {num*i}")

    end_time = time()
    print(f"That took {round(end_time - start_time, 1)} seconds")
    times.append({
        "num": num,
        "correct": correct,
        "time": round(end_time - start_time, 1)
    })
    print("")
    print(times)
    print("")
    ans = input("Go again (y/n)?: ")
    if (ans != 'y'):
        break    
    

