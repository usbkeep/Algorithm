# 그룹 단어 체커
# https://www.acmicpc.net/problem/1316

"""
    N은 100보다 작거나 같은 자연수
    단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.
"""


# 문제푸는애
import sys

# solution
def isGroup(word : str):  ### 문제 풀 친구
    # checkList = [0 for _ in range(ord('z') - ord('a') + 1)]
    checkSet = set()
    pre = ''
    for c in word:
        if c not in checkSet:  # 처음 출현하면 셋에 저장
            checkSet.add(c)
        elif pre != c:  # 값이 바뀌면, 셋에 이미 있는지 체크
            if c in checkSet:
                return 0
        pre = c
    return 1


# 메인함수
N = int(sys.stdin.readline())
result = 0
for i in range(N):
    word = sys.stdin.readline().strip()
    result += isGroup(word)
print(result)


