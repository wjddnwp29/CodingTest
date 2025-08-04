#include <string>
#include <vector>

using namespace std;

int solution(int n, int t) {
    int answer = 0;
    for (int i = 0; i < t+1; i++){
        if (i == 0){
            answer += n; 
        }
        else{
            answer *= 2;
        }
    }
    return answer;
}