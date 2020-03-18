#Create a program that once executed the programs prints Hello  instantly first,
# then it prints it after 1 second, then after 2, 3, and then the program
# prints out the message "End of the Loop" and stops.

import time
timer = 0
threshold = 4
while timer < threshold:
    time.sleep(timer)
    print("Hello")
    timer = timer + 1
print("End of the Loop")


#Alternatively use the break statement
timer = 0
while True:
    time.sleep(timer)
    print("Hello")
    timer = timer + 1
    if timer > 3:
        print("End of the loop")
        break


