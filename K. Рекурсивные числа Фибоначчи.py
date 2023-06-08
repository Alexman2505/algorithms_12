def find_commits(n):
    if n == 0 or n == 1:
        return 1
    else:
        return find_commits(n - 1) + find_commits(n - 2)


n = int(input())
result = find_commits(n)
print(result)

# тоже прошло
# n = int(input())
# f1, f2 = 1, 1
# for i in range(2, n+1):
#     f1, f2 = f2, f1 + f2

# print(f2)
