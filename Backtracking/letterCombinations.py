# -*- coding:UTF-8 -*-
'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
Example:
给定一串2-9的数字，返回其在手机按钮上可能的组合。
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

思路：经典的回溯组合问题，可以先把数字对应的字母序列做一个mapping字典，循环或递归加入每个字符，需要一个list保存当前正在加入的字符串。
'''

def letterCombinations(digits):
    if digits is None:
        return []

    d = {
        '2' : "abc",
        '3' : "def",
        '4' : "ghi",
        '5' : "jkl",
        '6' : "mno",
        '7' : "pqrs",
        '8' : "tuv",
        '9' : "wxyz"
    }

    result = [""]
    for i in digits:
        tmp = []
        for res in result:
            for letter in d[i]:
                tmp.append(res+letter)

        result = tmp

    return result

digits = str(23)
res =  letterCombinations(digits)
print (res)