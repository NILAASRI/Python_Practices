#Just simple Countdown Timer

import time

n = int(input("Enter seconds: "))
for i in range(n, 0, -1):
    print(i)
    time.sleep(1)
print("Time's up! ⏳")