#include <string>
#include <vector>

using namespace std;
int func(vector<int>& numbers, int target,int n,int i,int sum){
    int count=0;
    if(n==i && sum == target){
        return 1;
    }
    if(n==i) return 0;
    
    
    count+=func(numbers,target,n,i+1,sum+numbers[i+1]);
    count+=func(numbers,target,n,i+1,sum+(numbers[i+1]*(-1)));
    
    return count;
}
int solution(vector<int> numbers, int target) {
    int answer = 0;
    int n=(int)numbers.size();
    answer=func(numbers,target,n-1,-1,0);    

    return answer;
}
