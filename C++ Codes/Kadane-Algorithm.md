# Kadane’s Algorithm in C++  
Here, we will discuss the program for Kadane’s Algorithm in C++ programming language.
We are given with an array and we need to find the largest contiguous subarray sum which can be done
using Kadane’s algorithm efficiently. Kadane’s Algorithm can be viewed both as a greedy and DP. As we can see that 
we are keeping a running sum of integers and when it becomes less than 0, we reset it to 0 (Greedy Part). 
This is because continuing with a negative sum is way more worse than restarting with a new range. Now it can also be viewed as a DP, 
at each stage we have 2 choices: Either take the current element and continue with previous sum OR restart a new range.  

## Sample problem
Input : N = 8  
arr[] = {-2, -3, 4, -1, -2, 1, 5, -3}  
Output : 7  
Explanation : The sub-array {4, -1, -2, 1, 5} will gives the maximum sum of 7 as (4+(-1)+(-2)+1+5).  

## Algorithm :  
1. Take the size of the array from the user and store it in a variable say n.  
 
2. Declare an array of size n.  
 
3. Take n elements of the array from the user.  
  
4. Now, create variable say max_sum that hold the required maximum sum of subarray and curr_sum and initialize max_sum with INT_MIN and curr_sum with 0.  
 
5. Now, iterate over the array, and for every ith value of the array, add it to curr_sum, and comapre it with max_sum like,  
 
6. if(max_sum < curr_sum)
   max_sum = curr_sum.  
   
7. Now, check if curr_sum <0 then set curr_sum to 0.  
 
8. After complete iteration we will get the result that store in max_sum variable.  

## Code Implementation in C++  
~~~
#include <bits/stdc++.h>
using namespace std;

int main()
{
  int n;
  cin>>n;

  int arr[n];

  for(int i=0; i<n; i++)
    cin>>arr[i];

  int max_sum = INT_MIN, curr_sum =0;

  for(int i=0; i<n; i++){

   curr_sum += arr[i];

   if(max_sum < curr_sum)
     max_sum = curr_sum;

   if(curr_sum < 0)
     curr_sum = 0;

  }

  cout<<max_sum;

  return 0;
}
~~~  


