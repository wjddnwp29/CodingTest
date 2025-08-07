#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 1;
    while (answer != 0){
        if(n % answer == 1){
            break;
        }
        else{
            answer++;
        }
    }
    return answer;
}