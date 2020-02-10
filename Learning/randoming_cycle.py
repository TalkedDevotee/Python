import random
import time

number = 0
end = random.randint(1, 100)
stop = random.randint(1, 5)

print(end, "cycles and", stop, "second(s).")

for number in range(end):
    int = random.randint(0, 1000)
    print(int)
    if number != end:
        time.sleep(stop)
