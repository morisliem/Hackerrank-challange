#include <iostream>
using namespace std;

int main(){
    int n;
    int start = 0;
    int count = 0;
    cin >> n;
    char arr[n];
    int temp[n];
    for(int i=0;i<n;i++){
        cin >> arr[i];
    }
    
    for(int i=0;i<n;i++){
        if(arr[i] == 'U'){
            start += 1;
            temp[i] = start;
        }
        else{
            start -= 1;
            temp[i] = start;
        }
        if(start == 0 && temp[i-1] == -1){
            count++;
        }
    }
    
    cout << count << endl;
    return 0;
}
