# Copyright: Xiaoyi (Sherry) Zhu

'''
[LeetCode #70]
Description:
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.
'''

class Solution(object):
    def climbStairs(self, n):
        f = math.factorial
        c = 0
        if n%2==0:
            for i in range(1,n/2):
                c += f(n-i)/f(i)/f(n-i-i)
            return c+2
        else:
            for i in range(1,(n+1)/2):
                c += f(n-i)/f(i)/f(n-i-i)
            return c+1

'''
Runtime: 20 ms, faster than 96.64% of Python online submissions for Count and Say. (18NOV2018)
'''