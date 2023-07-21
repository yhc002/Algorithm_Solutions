#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int N;
int S[20][20];

int getDiff(vector<int> per) {
    int start=0;
    int link=0;
    for(int i=0; i<N; i++) {
        for(int j=0; j<N; j++) {
            if(per[i] && per[j])
                start += S[i][j];
            else if(!per[i] && !per[j])
                link += S[i][j];
        }
    }
    return abs(start - link); 
}

int main(){
    cin >> N;
    vector<int> per; //팀 나눌 조합
    for(int i=0; i<N; i++) {
        if(i<N/2)
            per.push_back(0);
        else
            per.push_back(1);
        for(int j=0; j<N; j++)
            cin >> S[i][j];
    }
    int diff = getDiff(per);
    while(next_permutation(per.begin(),per.end())) {
        diff = min(diff,getDiff(per));
    }
    cout << diff;
    return 0;
}
