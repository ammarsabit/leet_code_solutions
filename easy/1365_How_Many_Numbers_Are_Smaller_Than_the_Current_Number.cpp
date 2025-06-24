class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        int count=0;
        vector<int> less = {};
        for (int i = 0; i < size(nums); i++){
            for (int j = 0; j < size(nums); j++){
                if (nums[j] < nums[i])
                    count++;
            }
            less.push_back(count);
            count = 0;
        }

        return less;
    }
};