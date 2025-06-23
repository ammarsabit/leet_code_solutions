class Solution {
public:
    void reverseString(vector<char>& s) {
        for (int i; i < size(s)/2; i++){
            char tmp[1];
            tmp[0] = s[i];
            s[i] = s[size(s) - (i+1)];
            s[size(s) - (i+1)] = tmp[0];
        }
    }
};