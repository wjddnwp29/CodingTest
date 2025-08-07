#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    for(int t = 1; t <= n; t ++){
        if(n % t == 0){
            answer += t;
        }
    }
    return answer;
}