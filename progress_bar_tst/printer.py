import sys
import subprocess
import progressbar

# Draw spinner:
bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)

# Execute some job with multiple lines on stdout:
p = subprocess.Popen("C:\Python34\python.exe worker.py", shell=True, stdout=subprocess.PIPE,
                                                                     stderr=subprocess.PIPE)
# Lines will be collected in list:
result = []

# Until I get last line and the end of string:
while p.stdout is not None:

    # Update spinner on one step:
    # It will update only when any line was printed to stdout!
    bar.update()
    # Read each line:

    line = p.stdout.readline()
    # Add line in list and remove carriage return

    result.append(line.decode('UTF-8').rstrip('\r'))

    # When no lines appears:
    if not line:
        print("\n")
        p.stdout.flush()
        break

# Show finish message, it also useful because bar cannot start new line on console, why?
print("Finish:")
# Results as string:
print(''.join(result))