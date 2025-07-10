from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)

# Reading group A
for i in range(1, n + 1):
    word = input()
    d[word].append(i)

# Reading group B and printing results
for _ in range(m):
    word = input()
    if word in d:
        print(' '.join(map(str, d[word])))
    else:
        print(-1)
