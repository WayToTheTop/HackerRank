import re
tester = re.compile(
    r'^'
    r'(?!.*(\d)(?:-?\1){3})'
    r'[456]\d{3}-?(?:\d{4}-?){3}'
    r'$'
)
for _ in range(int(input())):
    if re.match(tester, input().strip()):
        print ("Valid")
    else:
        print ("Invalid")
