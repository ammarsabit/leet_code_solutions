class Solution {
public:
    int countPairs(vector<int>& nums, int k) {
        int count = 0;

        for (int i = 0; i < size(nums); i++){
            for (int j = i+1; j < size(nums); j++){
                if (nums[i] == nums[j] and (i*j)%k == 0)
                    count++;
            }
        }
        
        return count;
    }
};