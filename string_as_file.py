with open ("C:\\Users\div\Desktop\demo.txt", "r") as BigFile:
    data=BigFile.readlines()

# Print each line
for i in range(len(data)):
     print ("Line No- ",i) 
     print (data[i])
