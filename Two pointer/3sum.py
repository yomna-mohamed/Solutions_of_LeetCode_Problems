# -*- coding: utf-8 -*-
"""3Sum.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u0I6bdiX857saxE_h0SYxUrx0B587cB7
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        my_list=[]
        for i in range(0,len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            n=nums[i]
            p1=i+1
            p2=len(nums)-1
            while p1<p2:
                sum=n+nums[p1]+nums[p2]
                if sum==0:
                    my_list.append([nums[i],nums[p1],nums[p2]])
                    vp1=nums[p1]
                    vp2=nums[p2]
                    while p1<p2 and nums[p1]==vp1:
                        p1+=1
                    while p1<p2 and nums[p2]==vp2:
                        p2-=1 
                elif sum>0:
                    p2-=1
                else :
                    p1+=1
        return my_list