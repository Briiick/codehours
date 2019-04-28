import os

def createFile():
    if os.path.exists('tracker.txt'): # if file exists
        return False # continue
    else:
        f = open("tracker.txt","w+") # else open file or create it if not there
        f.write("0") # write 0
        f.close() # close file
        return True

def getNumber():
    # Call create file
    if (createFile() == True):
        return 0
    else:    
        f = open("tracker.txt","r") #open it
        number = f.read() # read file for number
        f.close()
        return int(number) #return the number

def updateNumber(addition):
    number = getNumber() # get the current number
    number += addition # add the extra hours
    f = open("tracker.txt","r+") # open the file
    f.truncate(0) # delete the number in the file
    f.write(str(number)) # add the new number to the file
    f.close() # close the file
    return number