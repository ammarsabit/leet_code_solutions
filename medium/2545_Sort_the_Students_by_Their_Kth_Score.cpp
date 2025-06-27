class Solution {
public:
    vector<vector<int>> sortTheStudents(vector<vector<int>>& score, int k) {
        for (int x = 0; x < size(score); x++){
            for (int i = 0; i < size(score)-1; i++){
                if (score[i][k] < score[i+1][k]){
                    vector<int> tmp = score[i];
                    score[i] = score[i+1]; 
                    score[i+1] = tmp;
                }
            }
        }
        return score;
        
    }
};