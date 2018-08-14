import re
if re.search('tor','tutorial'):
    print('search of tor is succsessful')

if re.match('tut','tutorial'):
    print('match sucsses')

if not re.search('ter','tutorial'):
    print('not happen search in string')

if not re.match('tor','tutorial'):
    print('not matched')

if not re.search('^tor','tutorial'):
    print(' sucsses as match')