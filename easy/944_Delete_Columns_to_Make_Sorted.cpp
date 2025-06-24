class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int delete_count = 0;
        int n = size(strs);

        for (int i=0; i < size(strs[0]); i++){
            for (int j=0; j < n-1; j++){
                if (strs[j][i] > strs[j+1][i]){
                    delete_count++;
                    break;
                }
            }
        }

        return delete_count;

    }
};