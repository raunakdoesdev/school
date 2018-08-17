content = '((())))'

with open('clumsy.in') as f:
    content = f.read()

balance = 0
num_flip = 0

for c in content:
    if c == '(':
        balance += 1
    elif c == ')':
        if balance == 0:
            num_flip += 1  # flip this one
            balance += 1
        else:
            balance -= 1
    
num_flip += balance / 2

fout = open ('clumsy.out', 'w')
fout.write (str(int(num_flip)) + '\n')
fout.close()
