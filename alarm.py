from datetime import datetime
from datetime import timedelta
from random import randint

now = datetime.now()  
print now


mins = randint(1, 10)

minsTwo = randint(1, 10)

while minsTwo==mins:
    minsTwo = randint(1, 10)

print(mins,minsTwo)


newnow1 = now + timedelta(minutes = mins)
newnow2 = now + timedelta(minutes = minsTwo)

print newnow1
print newnow2