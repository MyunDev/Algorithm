### 문제 1번

[예산 구하기 level1](https://programmers.co.kr/learn/courses/30/lessons/12982)

나의 풀이 코드 수정

```java
//Arrays로 정렬하기 위한 import문
import java.util.Arrays;

class Solution {
    public int solution(int[] d, int budget) {
        int answer = 0;
        int result = 0;
        //배열 정렬 
        Arrays.sort(d);
        
        for(int i=0; i<d.length; i++){
            result += d[i];
            //예산보다 값을 더한 값이 작다면
            if(budget < result ){
                answer = i;
                break;
            } else {
                //예산이 result보다 같거나 크다면
                answer = d.length;
            }
        }
        return answer;
    }
}
```

***

### 문제 2번

[x만큼 간격이 있는 n개의 숫자](https://programmers.co.kr/learn/courses/30/lessons/12954)

```java
class Solution {
    public long[] solution(int x, int n) {
        //n개의 숫자만큼 들어갈 answer 배열 선언 
        long[] answer = new long[n];
        long temp = x;
        
        for(int i=0; i<n; i++){
            answer[i] = temp * (i+1);
        }
        return answer;
    }
}
```



### 문제 3번

[핸드폰 번호 가리기](https://programmers.co.kr/learn/courses/30/lessons/12948)

```java
class Solution {
  public String solution(String phone_number) {
      String answer = "";
      //phone_number를 ""단위(한글자씩) split 해서 arr 배열에 저장한다
      String []arr=phone_number.split("");
      //끝에서 4자리수까지 *로 바꿔줌
      for(int i=0;i<arr.length-4;i++){
          arr[i]="*";
      }
      //answer String에다가 차례대로 넣어준다.
      for(int j=0;j<phone_number.length();j++){
          answer+=arr[j];
      }
      return answer;
  }
}
```



