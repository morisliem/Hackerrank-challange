#include <iostream>
#include <map>
using namespace std;

int main(){
    map<char, int> mp1;
    map<int, int> mp2;
    
    string s;
    cin >> s;
    int s_length = s.length();
    
    for(int i=0;i<s_length;i++){
        mp1[s[i]]++;
    }
    
    for(auto x : mp1){
        mp2[x.second]++;
    }
    
    if(mp2.size() == 1){
        cout << "YES" << endl;
    }
    else if(mp2.size() == 2){
        bool con = false;
        int count = 0;
        int smallNum, smallValue;
        int bigNum, bigValue;
        for (auto x : mp2){
            if (count == 0){
                smallNum = x.first;
                smallValue = x.second;
                count++;
            }
            else{
                bigNum = x.first;
                bigValue = x.second;
            }
        }
        
        if(bigValue == 1){
            if(bigNum - 1 == smallNum){
                con = true;
            }
            else{
                con = false;
            }
        }
        else if(smallValue == 1){
            if(smallNum - 1 == 0){
                con = true;
            }
            else{
                con = false;
            }
        }
        else{
            con = false;
        }

        if(con){
            cout << "YES" << endl;
        }
        else{
            cout << "NO" << endl;
        }
        
        cout << smallNum << " " << smallValue << endl;
        cout << bigNum << " " << bigValue << endl;
    }
    else{
        cout << "NO" << endl;
    }
    
}
