
<b>문제 설명</b>

​

수많은 마라톤 선수들이 마라톤에 참여하였습니다. 

단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant, 완주한 선수들의 이름이 담긴 배열 completion 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

​

<b>제한사항</b>

​

마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.

completion의 길이는 participant의 길이보다 1 작습니다.

참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.

참가자 중에는 동명이인이 있을 수 있습니다.

​

 
https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3

​

# 나의 풀이

<pre><code>
import collections 

def solution(participant, completion):

    result = collections.Counter(participant) - collections.Counter(completion)
    result = list(result.keys())

    return result.pop(-1)
</pre></code>

#효율성 테스트

![효율성테스트1](https://user-images.githubusercontent.com/78432057/107147781-3a0d6f00-6993-11eb-91af-99354b7b87d0.png)

나의 다른 풀이
<pre><code>
def solution(participant, completion):
    participant_dict = dict()

    for p in participant:
        participant_dict[p] = participant_dict.get(p, 0) + 1

    for c in completion:
        value = participant_dict[c] -1

        if value == 0:
            del participant_dict[c]
        else:
            participant_dict[c] = value

    return list(participant_dict.keys()).pop(-1)
</pre></code>
해당 알고리즘 문제를 java로 풀던 중 위와 같은 방식을 알게되었다.

적용후 미세하지만 약간의 성능 향상이 있었다.

(모든 case에서 차이가 존재하는 것으로 보아 더 효율적이라고 볼 수 있을 것 같다.)
#효율성 테스트
![효율성테스트2](https://user-images.githubusercontent.com/78432057/107147786-3bd73280-6993-11eb-991b-cd5324b99893.png)


# 과정

map key : value

![dict구성](https://user-images.githubusercontent.com/78432057/107147789-3ed22300-6993-11eb-8ece-b2bc83d93687.png)

먼저 위와 같이 key : value 쌍을 구성하고자 했다.

​

 step 1.

 - 현재 존재하는지 if, else 를 사용하여 탐색 후 값 적용하는 방식.

 - collections 등 라이브러리에 대한 정보를 알지 못했다.

 - python dictionary 활용

    participant_dict = {}  # participant_dict = dict()
    completion_dict = {}

    for p in participant:
        if p in participant_dict:
            participant_dict[p] += 1
        else:
            participant_dict[p] = 1
    for c in completion:
        if c in completion_dict:
            completion_dict[c] += 1
        else:
            completion_dict[c] = 1
 step 2.

 - get() 활용

 카운트하는 방법에 있어 더 효율적인 방식이 있을거라고 생각했다.

 아래 링크에서 get()을 이용해 키가 없는 경우 기본값 지정 및 내가 하고자하는 "+= 1" 모두 충족되는 방법을 찾았다.

(프로그래밍 관련 모든 질문에 대한 답은 Stackoverflow에 존재하는 것 같다..)

<b>".get allows you to specify a default value if the key does not exist."</b>

https://stackoverflow.com/questions/3496518/using-a-dictionary-to-count-the-items-in-a-list


    for p in participant:
        participant_dict[p] = participant_dict.get(p, 0) + 1
    for c in completion:
        completion_dict[c] = completion_dict.get(c, 0) + 1
python dict - dict 관련 정보 학습 및 고민 중에 collections 라이브러리를 알게되었고 이를 활용하여 문제를 해결했다.

# 
https://blog.naver.com/usbeen/222233801051
