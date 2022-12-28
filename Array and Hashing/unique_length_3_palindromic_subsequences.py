# -*- coding: utf-8 -*-
"""Unique Length-3 Palindromic Subsequences.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CpQLHG5VuajNd_FnHGTL2h22Zc5sh0NS
"""

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res=set()
        first=set()
        last=collections.Counter(s)
        for i in range(len(s)):
            last[s[i]]-=1
            if last[s[i]]==0:
                last.pop(s[i])
            for j in range(26):
                c=chr(ord('a')+j) 
                if c in first and c in last:
                    res.add((s[i],c))
            first.add(s[i])
        return len(res)