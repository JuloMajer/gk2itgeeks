from sys import argv

target = open("file_to_read.txt")
dataFromFile = target.read()
print ("The file content:\n%s") % (dataFromFile)
print ("The file has %s characters.") % (len(dataFromFile))

target.close()



