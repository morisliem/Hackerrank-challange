#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

int main(){
    int n,m;
    map <string, int> map;
    cin >> n >> m;
    bool con = true;
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
    
    for(int i=0;i<m;i++){
        string temp;
        cin >> temp;
        if(map.find(temp) == map.end() || map[temp] == 0){
            con = false;
            break;
        }
        else{
            map[temp] -= 1;
        }
    }
    
    if(con) {
        cout << "Yes" << endl;
    }
    else{
        cout << "No" << endl;
    }
    
    return 0;
}

