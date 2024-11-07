# 나는야 포켓몬 마스터 이다솜
# https://www.acmicpc.net/problem/1620

"""
    포켓몬의 개수 N
    맞춰야 하는 문제의 개수 M
    1 <= N, M <= 100,000

    포켓몬의 번호가 1번인 포켓몬부터 N번에 해당하는 포켓몬까지 한 줄에 하나씩 입력
    첫 글자만 대문자이고, 나머지 문자는 소문자로만 이루어져 있어.
    아참! 일부 포켓몬은 "마지막 문자만 대문자"일 수도 있어


"""
import sys

pokemonDict = dict()
pokemonNum = 0
N, M = map(int, sys.stdin.readline().split())

for _ in range(N):
    pokemonName = sys.stdin.readline().strip()
    pokemonNum += 1
    pokemonDict[pokemonName] = pokemonNum
    pokemonDict[str(pokemonNum)] = pokemonName

for _ in range(M):
    pokemonInfo = sys.stdin.readline().strip()
    print(pokemonDict.get(pokemonInfo))


