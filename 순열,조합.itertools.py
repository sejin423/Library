import itertools

data = [1,2,3]

# 순열
for x in itertools.permutations(data,2):
    print(list(x))
    
# 조합
for a in itertools.combinations(data,2):
    print(list(a), end=' ')
