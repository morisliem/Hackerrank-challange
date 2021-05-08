#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

int main(){
    int n,m;
    map <string, int> map;
    cin >> n;
    for(int i=0;i<n;i++){
        string temp;
        cin >> temp;
        if(map.find(temp) == map.end()){
            map[temp] = 1;
        }
        else{
            map[temp] += 1;
        }
    }
    
    cin >> m;
    for(int i=0;i<m;i++){
        string temp;
        cin >> temp;
        if(map.find(temp) == map.end()){
            cout << 0 << endl;
        }
        else{
            cout << map[temp] << endl;
        }
    }
    
    return 0;
}

