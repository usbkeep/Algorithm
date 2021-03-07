


문제 설명

H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

​

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

​

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

​

제한사항

과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.

논문별 인용 횟수는 0회 이상 10,000회 이하입니다.

<img src="https://user-images.githubusercontent.com/78432057/109661144-021dd400-7bad-11eb-9a2d-b21158973517.png">


 
문제출처: https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3

​

# 나의 풀이


<pre><code>
def solution(citations):
    answer = 0
    citations.sort()
    
    length = len(citations)

    for index in range(length):

        if length - index <= citations[index]:
            return length - index

    return answer
</code></pre>
​
<img src="https://user-images.githubusercontent.com/78432057/109661142-01853d80-7bad-11eb-95bc-e844ae284eed.png">


H-Index 값을 구할 때

​

예시로 H-Index = 3인 경우

​

배열에서 3이상인 값이 3개 이상이여야 한다.

[0,1,2,3,3,3]   #  sort()를 통해 정렬한 상태.

해당 값을 찾기 위해 아래 if 조건을 구성했다.

총 길이 - 현재의 인덱스값 <= citations[현재의 인덱스]

 ex) 6 - 3 <= 3   True

​
아래와 같이 나타냈을 때 좀 더 이해가 쉬웠다.
<pre><code>
    for index in range(length):

        if length <= citations[index] + index:
            return length - index
            
</pre></code>

​
