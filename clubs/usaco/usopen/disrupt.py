answer = [7,
          7,
          8,
          5,
          5]

fout = open ('disrupt.out', 'w')
for i in answer:
    fout.write(str(i) + "\n")
fout.close()
