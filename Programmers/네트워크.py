#include <string>
#include <vector>

using namespace std;
int dfs(int n , int i, vector<vector<int>>& computers, int * visited){
    if(visited[i]){
        return 0;
    }
    visited[i] =1;
    for(int j=0;j<n;j++){
        if(computers[i][j]){
            dfs(n,j,computers,visited);
        }
    }
    return 1;
}


int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    int visited[200]={0,};
    for(int i =0;i<n;i++){
        answer+=dfs(n,i,computers,visited);
    }
    return answer;
}


