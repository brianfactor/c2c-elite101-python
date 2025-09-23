import datetime
import time

timeoutStr = input("How many minutes should we time? ")
timeout = datetime.timedelta(minutes=int(timeoutStr))
start_time = current_time = datetime.datetime.now()

print(start_time)
print(start_time.minute)

while start_time - current_time < timeout:
    print(current_time.time(), end="\r")
    time.sleep(1)
    current_time = datetime.datetime.now()
