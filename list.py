as1 = ['love', 'pig', 'dog', 'cat', 'monkey']
bs1 = ['like', 'dog', 'chicken', 'rice', 'race']
for b in bs1:
    if b not in as1:
        as1.append(b)
print(as1)