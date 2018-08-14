import re
text="this is we address http://www.tutorialspoint.com"
result=re.search('([\w.-]+)://([\w.-]+)\.([\w.-]+)', text)
if result:
    print("the main address",result.group())
    print("the protocol",result.group(1))
    print("domain",result.group(2))
    print("tld",result.group(3))