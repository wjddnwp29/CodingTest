#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> v) {
    int answer = 0;
    sort(v.begin(),v.end());
    if (v[2]< v[0]+v[1]){
        answer += 1;
    }
    else{
        answer += 2;
    }
    
    return answer;
}