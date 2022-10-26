#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    
    int m=INT_MIN;
    
    int maxSum(TreeNode * root){
        if(root==NULL){
            return 0;
        }
        int lh=max(0,maxSum(root->left));
        int rh=max(0,maxSum(root->right));
        m=max(m,lh+rh+root->val);
        
        return root->val + max(lh,rh);
        
        
        
    }
    int maxPathSum(TreeNode* root) {
        
        maxSum(root);
        return m;
        
        
        
        
    }
};