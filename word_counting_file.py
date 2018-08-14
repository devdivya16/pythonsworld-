Filename="C:\\Users\div\Desktop\demo.txt"
with open(Filename,'r') as file:
    lines_of_file=file.read()
    print (lines_of_file)
    print(lines_of_file.split())
    print(len(lines_of_file.split()))