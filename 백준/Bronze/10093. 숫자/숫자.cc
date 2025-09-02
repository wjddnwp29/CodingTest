#include <iostream>
using namespace std;
int main(){
    long long A, B;
    cin >> A >> B;
    
    int num = 0;
    if (A < B){
            for(int n = A+1; n < B; n++){
            num++;
        }
            cout << num << "\n";
            for(int n = A+1; n < B; n++){
                num++;
                cout << n << " ";
        }
    }
    else if (A > B){
        for(int n = B+1; n < A; n++){
        num++;
    }
    cout << num << "\n";
    for(int n = B+1; n < A; n++){
        num++;
        cout << n << " ";
    }
}   
    else if(A==B){
        cout << 0;
    }
    return 0;
}