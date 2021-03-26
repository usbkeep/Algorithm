# 문제 설명

​

수많은 마라톤 선수들이 마라톤에 참여하였습니다. 

단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant, 완주한 선수들의 이름이 담긴 배열 completion 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

​

# 제한사항

​

마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.

completion의 길이는 participant의 길이보다 1 작습니다.

참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.

참가자 중에는 동명이인이 있을 수 있습니다.


https://programmers.co.kr/learn/courses/30/lessons/42576?language=java

# 나의 풀이

<pre><code>
public String solution(String[] participant, String[] completion) {
        Map<String, Integer> map = new HashMap<>();
        
        for(String p : participant) {
        	map.put(p, map.getOrDefault(p, 0) +1);
        }
        
        for(String c : completion) {
        	if(map.get(c) == 1) {
        		map.remove(c);
        	}
        	else {
        		map.put(c, map.get(c) - 1);
        	}
        }
        return map.keySet().iterator().next();
    }
</pre></code>

 방식

 - 참가자 목록을 Hashmap에 저장.

 - 참가자 Hashmap에서 완주자 목록을 검색

   => 해당 값이 1인 경우 삭제, 아닌경우 update

 - 이후 참가자 Hashmap에 남은 Key값(들)은 완주하지 못한 사람

 효율성 검사
 
 <img src="https://user-images.githubusercontent.com/78432057/107291090-f3129d00-6aaa-11eb-92bd-58ee4aa7c55f.png"></img>

사실 이 문제의 경우 Hashmap을 사용하는것보다 단순히 배열 두개를 가지고 비교하는 방식으로 하는것이 

더 빠른 실행결과를 얻을 수 있다. (추가 업로드 예정) - code -

비밀) 처음 이 문제를 접했을 때 바로 배열만을 활용하여 풀었다.

, 해시 문제이지만 다양한 풀이법이 당연하게도 존재하고 모두 시도해보는것이 좋다고 생각한다.

​

문제의 취지에 맞게 해쉬로 풀고자 하였고, 다른사람의 풀이를 참조 했을 때 sort()를 사용하여 푸는 경우도 많았다.

마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.

하지만 문제의 제한사항을 살펴보면 참가 선수의 수가 1~ 100,000명이다.

해당 문제에서는 sort()를 사용하여 풀어도 빠른 실행결과값을 얻을 수 있다. 

그러나 sort()하는 방식은 비효율적이라고 생각한다. (해시를 이용해 풀어보자.)

​

python으로 해당 문제를 같은 방식으로 풀었을 때는 효율성 관련한 문제가 없었다.

java의 경우 나의 풀이가 다른것인지 예상보다 많이 비효율적인 결과인 것 같다.

​

현재 확인된 사실.

get(key) 는 비효율 적이다.

모든 해답은 stackoverflow ..!

 - Reference.
 https://stackoverflow.com/questions/3870064/performance-considerations-for-keyset-and-entryset-of-map
 
좀 더 효율적이고 가독성이 좋은 코드를 구성하고자 한다. 좀 더 다양한 방법을 시도해볼 필요가 있어 보인다.
 



