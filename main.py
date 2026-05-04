import random #import module
import time

def getRandomDate(startDate, endDate): #defining function
    print("Printing a random date in between:", startDate, "and", endDate)
    randomGenarator = random.random()
    dateFormat = '%m%d%Y'

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + randomGenarator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

#Display results
print("Random Date = ", getRandomDate("26/11/2012", "14/05/2012"))