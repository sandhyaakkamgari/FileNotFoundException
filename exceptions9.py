# trying to open a file, which does not exist
try:
    #trying to open a file in read mode
    fo = open("myfile.txt","rt")
    print("File opened")
except FileNotFoundError:
    print("File does not exist")
except:
    print("Other error")