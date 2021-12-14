// 완주하지 못한 선수
// https://programmers.co.kr/learn/courses/30/lessons/42576

/*
    입출력 예)
        participant = ["leo", "kiki", "eden"]
        completion = ["eden", "kiki"]
        return = "leo"

    print(solution(participant, completion))
*/


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
