#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    // 1 ~ 7 1
    // 8 ~ 14 2
    // ...
    if (n <= 7){
        answer += 1;
    }
    else if (n > 7 && n % 7 == 0)
    {
        answer += (n/7);
    }
    else{
        answer += (n/7) + 1;
    }
    
    return answer;
}