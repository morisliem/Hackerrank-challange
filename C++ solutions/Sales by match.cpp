#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    int temp;
    int pairs = 0;
    vector<int> v;
    vector<int> :: iterator it;
    cin >> n;
    for(int i=0;i<n;i++){
        cin >> temp;
        it = find(v.begin(), v.end(), temp);
        if(it == v.end()){
            v.push_back(temp);
        }
        else{
            pairs++;
            it = find(v.begin(), v.end(), temp);
            v.erase(it);
        }
    }

    cout << pairs << endl;
    
    return 0;
}
