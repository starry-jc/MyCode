# Problem: 2dperm

N, M, Q = map(int, input().split())
queries = []

for i in range(Q):
    query = int(input())
    queries.append(query)

def array(i, j, query):
    if i * j <= query and (N - (i - 1)) * (M - (j - 1)) <= (M * N - query) + 1:
        return True
    else:
        return False

for query in queries:
    count = 0
    
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if array(i, j, query):
                count += 1
                
    print(count)
    
    sdfsdsdsdf