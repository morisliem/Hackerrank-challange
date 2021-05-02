#include <deque>
#include <iostream>
using namespace std;

int main(){
    int n;
    deque<int> dq;
    int temp, count = 0;
    
    cin >> n;
    for(int i=0;i<n;i++){
        cin >> temp;
        dq.push_back(temp);
    }
    
    while(dq.size() > 1){
        if(dq.size() >= 3){
            if(dq.at(2) == 0){
                dq.pop_front();
                dq.pop_front();
                count++;
            }
            else if(dq.at(2) == 1){
                dq.pop_front();
                count++;
            }
        }
        else{
            dq.pop_front();
            count++;
        }
    }
    
    cout << count << endl;
    return 0;
}
