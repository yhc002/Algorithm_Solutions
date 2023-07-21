#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int N;

int calc(vector<int> a, vector<int> p) {
    int total=a[0];
    for(int i=0; i<N-1; i++) {
        switch(p[i]){
            case 0: total+=a[i+1]; break;
            case 1: total-=a[i+1]; break;
            case 2: total*=a[i+1]; break;
            case 3: total=total/a[i+1]; break;
        }
    }
    return total;
}

int main(){
    int max;
    int min;

    cin >> N;
    vector<int> A(N);
    vector<int> permutation(N-1); // permutation
    int tmp;

    for(int i=0; i<N; i++) {
        cin >> A[i];
    }
    
    int start=0;
    for(int i=0; i<4; i++) {
        cin >> tmp;
        for(int j=start; j<start+tmp; j++) {
            permutation[j] = i;
        }
        start+=tmp;
    }
    sort(permutation.begin(), permutation.end());

    max=calc(A,permutation);
    min=max;
    int cur;
    while(next_permutation(permutation.begin(),permutation.end())){
        cur=calc(A,permutation);
        if(max<cur)
            max=cur;
        if(min>cur)
            min=cur;
    }


    cout << max << endl;
    cout << min << endl;
    return 0;
}
