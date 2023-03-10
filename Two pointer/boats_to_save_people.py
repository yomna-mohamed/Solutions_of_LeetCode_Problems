# -*- coding: utf-8 -*-
"""Boats to Save People.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d3Enn20rZ53U14UVhJyn0RPw_8jT7tCH
"""

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people=sorted(people)
        L=0
        R=len(people)-1
        count=0
        while L<=R:
            if people[L]+people[R]>limit:
                count+=1
                R-=1
            elif people[L]+people[R]<=limit: 
                count+=1
                R-=1
                L+=1
        return count