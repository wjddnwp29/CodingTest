#include <iostream>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    

    int N;
    cin >> N;
    int A,B;
    for(int n = 0 ; n < N; n++){
        cin >> A >> B;
        cout << A+B << "\n";
    }
    return 0;
}