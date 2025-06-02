#include<iostream>
#include<algorithm>

using namespace std;

define MAX 500;

int multiply(int x, int res[], int res_size);

void factorial(int n) {
    int res[MAX];

}

int main() {
    int N;
    cin >> N;
    
    long long answer = 1;
    
    if (N == 0) {
        answer = 1;
    } else {
        for (int i=1; i <= N; i++) {
            answer *= i;
        }
    }
    cout << answer;
    return 0;
}