def levelshtein_distance(source: str, target: str) -> int:
    n, m = len(source), len(target)
    dist = [[None] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dist[i][0] = i
    for j in range(m + 1):
        dist[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dist[i][j] = min([dist[i-1][j] + 1, dist[i][j-1] + 1,
                             dist[i-1][j-1] + (source[i-1] != target[j-1])])

    return dist[n][m]


print(levelshtein_distance(source="yu", target="you"))
# 1

print(levelshtein_distance(source="kitten", target="sitting"))
# 3
