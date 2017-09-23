import time
import random

print("START SOMETHING")

for i in range(5):
    sec = random.randint(1, 3)
    print("Sleeping for: %d" % sec)
    time.sleep(sec)
    print("Making job, line: %d" % i)

print("END SOMETHING")