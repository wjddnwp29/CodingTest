#include <string>
#include <vector>

using namespace std;

vector<int> solution(long long n) {
    vector<int> answer;
    //12345
    while (n!=0){
        if (n < 10){
            answer.insert(answer.end(),n);
            n = n-n;
        }
        else{
            answer.insert(answer.end(),n%10);
            n = n / 10;
        }
    }
    return answer;
}