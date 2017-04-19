import re
f = lambda m: 'and' if m.group(1) == '&&' else 'or'
for _ in range(int(input())):
    print (re.sub(r'(?<= )(\|\||\&\&)(?= )', f, input()))
