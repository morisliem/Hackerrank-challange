#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

int main(){
    map <int, int> mp1, mp2;
    int n;
    int a,b;
    cin >> n;
    for(int i=0;i<n;i++){
        cin >> a >> b;
        if (a == 1){
            int temp = mp1[b];
            if (temp > 0){
                mp2[temp]--;
            }
            mp1[b]++;
            mp2[temp + 1]++;
        }
        else if(a == 2){
            int temp = mp1[b];
            if (temp > 0){
                mp1[b]--;
                mp2[temp]--;
                if(temp - 1 > 0){
                    mp2[temp-1]++;
                }
            }
        }
        else{
            if(mp2[b] > 0){
                cout << 1 << endl;
            }
            else{
                cout << 0 << endl;
            }
        }
    }
    return 0;
}

