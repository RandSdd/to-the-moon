"""
a easy try of data forecasting based on titanic dataset
i am busy these days and i will attempt to keep a learning log
at least every two days
"""

#initial preparatory work
import pandas as pd
import matplotlib.pyplot as plt

n = '\n\n'
train = pd.read_csv('train.csv')  #"import" "by the way" as bw  :)
#i learn what a csv is bw.
print(f'data shape:{train.shape}')  #corrected some misunderstandings of
#f-string,using print(f'{data shape:}train.shape') before
print(n)  #sadly,due to the feature of .info,we can only do so to avoid
#a print like none.i know some pythonic philosophy bw
train.info()
print(f'{n}{train.describe()}')  #i find without (),it will print some thing
#not expected,i take a quick look bw,i don't need to use it now
print(f'{n}{train.head()}')

print(f'{n}---Preliminary investigation results---')
#let's see the total rate
survived_rate = train['Survived'].mean() #i didn't know the average meaning
# of mean before
print(f'{n}the total survived rate:\n{survived_rate}')

#sigh:i am going rewrite all with python standard library
#pause temporarily,i am really tired,sorry for every reader
