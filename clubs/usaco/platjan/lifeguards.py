"""
ID: your_id_here
LANG: PYTHON2
TASK: test
"""

shifts = [0,] *  10000000
updated_shifts = [0,] *  10000000
first =  10000000
last = 0
longest = 0

fin = open ('lifeguards.in', 'r')
fout = open ('lifeguards.out', 'w')
n,k = map(int, fin.readline().split())
lifeguards = []

for i in range(n):
    start, end = map(int, fin.readline().split())
    for t in range(start,end):
        shifts[t] += 1

    lifeguards.append((start, end,))
    if start < first:
        first = start
    if end > last:
        last = end

removed = []
for i in range(k):
    for i in range(n):
        if i in removed:
            continue
        count = 0
        start = lifeguards[i][0]
        end = lifeguards[i][1]
        for t in range(first, last):
            updated_shifts[t] = shifts[t]
            if t >= start and t < end:
                if shifts[t] > 1:
                    count += 1
                updated_shifts[t] = shifts[t] - 1
            elif shifts[t] > 0:
                count += 1
        if count > longest:
            longest = count
            shifts = list(updated_shifts)
            removed.append(i)

fout.write (str(longest - 1) + '\n')
fout.close()
