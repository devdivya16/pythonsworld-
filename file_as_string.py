with open ("C:\\Users\div\Desktop\demo.txt", "r") as BigFile:
    data=BigFile.read().replace("\n","")
print(type(data))
print (data)