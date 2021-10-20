import time, sys

# update_progress() : Displays or updates a console progress bar
## Accepts a float between 0 and 1. Any int will be converted to a float.
## A value under 0 represents a 'halt'.
## A value at 1 or bigger represents 100%
def update_progress(progress):
    barLength = 10 # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(barLength*progress))
    text = "\rPercent: [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), progress*100, status)
    sys.stdout.write(text)
    sys.stdout.flush()


# update_progress test script
print ("progress : 'hello'")
update_progress("hello")
time.sleep(1)

# print("progress : 3")
# update_progress(3)
# time.sleep(1)

print("progress : [23]")
update_progress([23])
time.sleep(1)


# print ("\nprogress : -10")
# update_progress(-10)
# time.sleep(2)


print ("progress : 10")
for i in range(21):
    time.sleep(0.1)
    update_progress(i/20.0)


# print ("progress : 0->1")
# for i in range(101):
#     time.sleep(0.1)
#     update_progress(i/100.0)


print ("\nTest completed")
time.sleep(10)