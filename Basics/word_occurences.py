s = "I work in bloomberg work work"

tokens=s.split(" ")
d={}
for token in tokens:
    if token in d:
        d[token] += 1
    else:
        d[token] = 1

print(d)

#{'I': 1, 'work': 3, 'in': 1, 'bloomberg': 1}
