#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    while (n != 0){
            if (n > 10){
                answer += n%10;
                n = n/10;
            }
            else if (n < 10){
                answer += n;
                n -= n;
            }
        }
    return answer;
}