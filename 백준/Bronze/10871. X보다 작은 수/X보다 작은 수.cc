#include <bits/stdc++.h>
using namespace std;
int main(){
    int N, X;
    int arr[10005];
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N >> X;
    for (int i = 0; i < N; i++){
        cin >> arr[i];
    }
    for (int i = 0; i < N; i++){
        if (X > arr[i]){
            cout << arr[i] << ' ';
        }
    }
    
    return 0;
}