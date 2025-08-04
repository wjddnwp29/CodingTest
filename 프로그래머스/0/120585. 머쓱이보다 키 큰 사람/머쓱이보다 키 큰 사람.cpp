#include <string>
#include <vector>

using namespace std;

int solution(vector<int> array, int height) {
    // array 키들어있는거, height 머쓱이 키
    int answer = 0;
    for (int i = 0; i < array.size(); i ++){
        if(array[i] > height){
            answer += 1;
        }
    }
    
    return answer;
}