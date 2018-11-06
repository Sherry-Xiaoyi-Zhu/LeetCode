#Copyright: Xiaoyi (Sherry) Zhu
# Email: zhuxy9474@gmail.com

'''
[LeetCode #38]

Description:
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.
'''

class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return '1'
        elif n == 2:
            return '11'
        else:
            c = Solution()
            s = c.countAndSay(n-1)
            counter = 1
            i = 0
            c = ''
            fl = True
            while i < len(s)-1:
                if s[i] == s[i+1]:
                    if fl:
                        counter += 1
                    elif not fl:
                        counter = 2
                    
                    if i+1 == len(s) - 1:
                        afl = True
                        c = c + '2' + s[i]
                    else:
                        if i != 0 and s[i+1] != s[i+2]:
                            c = c + str(counter)
                    fl = True
                else:          
					if fl and i != 0:
                        c = c + s[i]
                    else:
                        c = c + '1' + s[i]
                    fl = False
                i += 1
        
            tail = s[i]
            counter = '1'
            if fl:
                tail = '' 
                counter = ''
                
            s = c + counter + tail
            return s

'''
Runtime: 24 ms, faster than 90.32% of Python online submissions for Count and Say. (05NOV2018)
'''