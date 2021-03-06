import sys
import time
import subprocess
from tqdm import tqdm
# Draw spinner:

# Execute some job with multiple lines on stdout:
p = subprocess.Popen("C:\Python34\python.exe worker.py", shell=True, stdout=subprocess.PIPE,
                                                                     stderr=subprocess.PIPE)
# Lines will be collected in list:
result_out = []
result_err = []

# Until I get last line and the end of string:
while (p.stdout or p.stderr) is not None:

    for line in (p.stdout and p.stderr):
        tqdm.write("Done task %i" % len(line))

    out = p.stdout.readline()
    err = p.stderr.readline()

    result_out.append(out.decode('UTF-8').rstrip('\r'))
    result_err.append(err.decode('UTF-8').rstrip('\r'))
    time.sleep(0.5)

    if not out:
        print("")
        break

# Show finish message, it also useful because bar cannot start new line on console, why?
print("Finish:")
# Results as string:
print(''.join(result_out))
print("Errors:")
print(''.join(result_err))