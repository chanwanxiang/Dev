## Python正则表达式
#     正则表达式是一个特殊的字符序列,他能帮助你检查一个字符串是否与某种模式匹配

## 方法 re.match
#     re.match 尝试从字符串的起始位置匹配一个模式,如果不是起始位置匹配成功的话,match()就返回none
#     re.match(pattern,string,flags=0)
#     pattern 匹配的正则表达式
#     string 要匹配的字符串
#     flags 标志位,用于控制正则表达式的匹配方式,如是否区分大小写
#     匹配成功re.match方法返回一个匹配的对象,否则返回None

import re

print(re.match('www','www.baidu.com'))  #<re.Match object; span=(0, 3), match='www'>
print(re.match('com','www.baidu.com'))  #None

## 方法 re.search
#     re.search 扫描整个字符串并返回第一个成功的匹配
#     re.search(pattern,string,flags=0)
#     pattern 匹配的正则表达式
#     string 要匹配的字符串
#     flags 标志位,用于控制正则表达式的匹配方式,如是否区分大小写
#     匹配成功re.search方法返回一个匹配的对象,否则返回None

import re

print(re.search('www','www.baidu.com'))  #<re.Match object; span=(0, 3), match='www'>
print(re.search('com','www.baidu.com'))  #<re.Match object; span=(10, 13), match='com'>

## TODO: re.match只匹配字符串的开始,如果字符串开始不符合正则表达式,则匹配失败,函数返回None.而re.search匹配整个字符串,直到找到一个匹配

## 方法 re.sub
#     re.sub用于替换字符串中的匹配项
#     re.sub(pattern, repl, string, count=0, flags=0)
#     pattern 正则中的模式字符串
#     repl 替换的字符串,也可为一个函数
#     string 要被查找替换的原始字符串
#     count 模式匹配后替换的最大次数,默认0表示替换所有的匹配

import re

print(re.sub('#.+$','','mm is a cute cat # mm是一直可爱的猫咪'))  #mm is a cute cat

## 方法 re.compile
#     compile 函数用于编译正则表达式,生成一个正则表达式(Pattern)对象,供match()和search()这两个函数使用
#     re.compile(pattern[, flags])
#     pattern 一个字符串形式的正则表达式
#     flags 可选,表示匹配模式,比如忽略大小写,多行模式等,具体参数为
#         re.I 忽略大小写
#         re.X 为了增加可读性，忽略空格和 # 后面的注释

import re

pattern = re.compile(r'[a-z]+ [a-z]+',re.I)  #中键有空格
print(pattern)  #re.compile('[a-z]+ [a-z]+', re.IGNORECASE)

s = pattern.match('Hello World Wide Web')
print(s)  #<re.Match object; span=(0, 11), match='Hello World'>

## 方法 re.findall
#     在字符串中找到正则表达式所匹配的所有子串,并返回一个列表,如果没有找到匹配的,则返回空列表
#     re.findall(patter,string[,pos[,endpos]])
#     pattern 匹配的正则表达式
#     string 要匹配的字符串
#     pos 可选参数,指定字符串的起始位置,默认为0
#     endpos 可选参数,指定字符串的结束位置,默认为字符串的长度

import re

print(re.findall('[0-9]+','1岁,2岁,3岁,4岁'))  #['1', '2', '3', '4']

## re.split
#     split方法按照能够匹配的子串将字符串分割后返回列表
#     re.split(pattern, string[, maxsplit=0, flags=0])
#     pattern 匹配的正则表达式
#     string 要匹配的字符串
#     maxsplit 分隔次数,maxsplit=1分隔一次,默认为0,不限制次数

# \W 匹配字母数字下划线
import re

print(re.split('\W+','i-am-a-pythonic'))  #['i', 'am', 'a', 'pythonic']