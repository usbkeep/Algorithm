# 문제 설명



스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

속한 노래가 많이 재생된 장르를 먼저 수록합니다.

장르 내에서 많이 재생된 노래를 먼저 수록합니다.

장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.



노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.



# 제한사항



genres[i]는 고유번호가 i인 노래의 장르입니다.

plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.

genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.

장르 종류는 100개 미만입니다.

장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.

모든 장르는 재생된 횟수가 다릅니다.


https://programmers.co.kr/learn/courses/30/lessons/42579?language=python3

# 풀이

<pre><code>
def solution(genres, plays):
    answer = []

    g_dict = dict()
    p_dict = dict()

    for index, (g, p) in enumerate(zip(genres, plays)):
        if g not in g_dict:
            g_dict[g] = [(index, p)]
        else:
            g_dict[g].append((index, p))

        if g not in p_dict:
            p_dict[g] = p
        else:
            p_dict[g] += p

    for (k, v) in sorted(p_dict.items(), key=lambda x: x[1], reverse=True):
        for (i, p) in sorted(g_dict[k], key=lambda x: x[1], reverse=True)[:2]:
            answer.append(i)

    return answer
</code></pre>
<img src="https://user-images.githubusercontent.com/78432057/107646177-ff6e4400-6cbc-11eb-9176-9694f3ad8d8d.png">



  정리 : https://blog.naver.com/usbeen/222237427449
    
    
