프로그래머스_주식가격_python

<b>문제 설명</b>

​

초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

​

<b>제한사항</b>

​

prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.

prices의 길이는 2 이상 100,000 이하입니다.


https://programmers.co.kr/learn/courses/30/lessons/42584?language=python3

# 최종 풀이

<pre><code>
def solution(prices):

    answer = [0] * len(prices)
    stack = []

    for index, p in enumerate(prices):

        while stack and prices[stack[-1]] > p:
            temp = stack.pop()
            answer[temp] = index - temp
        stack.append(index)

    for s in stack:
        answer[s] = len(prices)-1 - s

    return answer
</pre></code>

<img src="https://user-images.githubusercontent.com/78432057/108080107-de3d9700-70b2-11eb-8cb6-6ab2a03f7d66.png">

# 과정.

내가 생각한 규칙은 다음과 같다.

  다른 것 상관없이. 해당 주식의 값이 낮아지는 순간

    (현재의 index 값) - (비교한 주식의 index) = 떨어지지 않은 기간

​

방식

 - 스택안에 값을 하나씩 넣을 것이다.

 - 스택에는 index 값을 넣는다. (이유는 위에 내가 생각한 규칙을 기반으로 계산하기 위해)

​

step0. 

  스택에 push하기 전에 prices[기존 stack값]이 현재 넣고자하는 값 p 보다 크다면 주식이 떨어진 것이다.

  그렇기에 stack.append(index)하기 전에 

    "while stack and​ prices[stack[-1]] > p" 를 먼저 실행하도록 했다.

​

 step1.

  스택안에 값이 있다면 현재의 price와 비교한다.

  비교했을 때 스택안에 값이 클 경우 주식이 하락한 것이기에 pop() 한다.

  pop()한 값은 temp에 저장.

​

 step 2.

  temp : 떨어진 주식의 인덱스, step1에서 설명

  answer[temp] 는 (현재의 인덱스) - (temp)

​

 step 3.

   stack에 남은 값들은 끝까지 가격이 떨어지지 않은 경우의 값들이다.

   그렇기에 (마지막 index) - (해당 index) 를 계산해주면 된다.

      배열의 길이 len(prices) 에 - 1 한다면 마지막 인덱스 값이 된다.

 결국 " answer[s] = len(prices) -1 - s" 해주면 된다.

​

# 
https://blog.naver.com/usbeen/222246036972
