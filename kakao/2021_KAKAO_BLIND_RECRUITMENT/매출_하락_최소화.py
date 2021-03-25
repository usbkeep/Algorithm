"""
테스트 중
"""
adj = [[] for i in range(300005)]
INF = 0x7fffffff7fffffff
d = [[0] * 2 for i in range(300005)]
s = []


def dfs(cur):
    if not adj[cur]:
        d[cur][0], d[cur][1] = s[cur], 0
        return None
    mingap = INF
    d[cur][0] = s[cur]
    for x in adj[cur]:
        dfs(x)
        d[cur][0] += min(d[x])
        mingap = min(mingap, d[x][0] - d[x][1])
    if mingap < 0:
        mingap = 0
    d[cur][1] = d[cur][0] + mingap - s[cur]


def solution(sales, links):
    global s
    s = [0] + sales
    for x in links:
        adj[x[0]].append(x[1])
    dfs(1)
    return min(d[1])


if __name__ == '__main__':
    sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
    links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
    print(solution(sales,links),'\n---------')
    #print(solution([10, 10, 1, 1],[[3,2], [4,3], [1,4]]))
