import re
text = "Please contact us at contact@tutorialspoint.com for further information."+\
        " You can also give feedbacl at feedback@tp.com"
emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
print (emails)
with open("C:\\Users\div\Desktop\demo.txt") as file:
    for line in file:
        urls=re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
        print (urls)