"""
ID: your_id_here
LANG: PYTHON2
TASK: test
"""

fin = open ('greedy.in', 'r')
fout = open ('greedy.out', 'w')
n = map(int, fin.readline().split())[0]
cuts = map(int, fin.readline().split())

cow_get_food = [False] * n
seen = []
line = [i for i in range(n)]
seen.append(list(line[:10]))
cow_get_food[0] = True

while True:
    gifted_cow = line.pop(0)
    cow_get_food[line[0]] = True
    line.insert(n - cuts[gifted_cow] - 1, gifted_cow)
    if line[:10] in seen:
        break
    seen.append(list(line[:10]))

fout.write (str(n - sum(cow_get_food)) + str('\n'))
fout.close()
