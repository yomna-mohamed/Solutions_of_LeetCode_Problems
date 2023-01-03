# -*- coding: utf-8 -*-
"""Reverse String.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f2k2eZvg1Z3uL9Bb1iMoxGlvvWQrtvve
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        L=0
        R=len(s)-1
        while(L<R):
            tmp=s[L]
            s[L]=s[R]
            s[R]=tmp
            L+=1
            R-=1