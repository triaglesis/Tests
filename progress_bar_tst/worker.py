import time
import random
import sys

print("START SOMETHING")

for i in range(4):
    sec = random.randint(1, 2)
    print("JOB: Sleeping for: %d" % sec)
    time.sleep(sec)
    print("JOB: Making job, line: %d" % i)

for i in range(5):
    sec = random.randint(1, 2)
    print("ERROR: Sleeping for: %d" % sec, file=sys.stderr)
    time.sleep(sec)
    print("ERROR: During job %d" % i, file=sys.stderr)

print("END SOMETHING")

