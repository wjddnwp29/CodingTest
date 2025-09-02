#include <iostream>
using namespace std;

int main(){
    // 영식이 통화 시간
    int N;
    cin >> N;
    int cost_arr[N];
    for(int n = 0; n < N; n++) cin >> cost_arr[n];


    int y_cost = 0;
    int m_cost = 0;
    for(int n = 0; n < N; n++){
        y_cost += ((cost_arr[n]/30)+1)*10;
        m_cost += ((cost_arr[n]/60)+1)*15;
    }
    if(y_cost == m_cost){
        cout << "Y M " << y_cost;
    }
    if(y_cost > m_cost){
        cout << "M " << m_cost;
    }
    if(y_cost < m_cost){
        cout << "Y " << y_cost;
    }

    
    

    return 0;
}