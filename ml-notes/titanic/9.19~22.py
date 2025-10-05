"""
an easy try of data forecasting based on titanic dataset
i am busy these days and i will attempt to maintain a learning log
at least every two days
"""

#initial preparatory work
import pandas as pd
import matplotlib.pyplot as plt

n = '\n\n'
train = pd.read_csv('train.csv')  #"import" "by the way" as bw  :)
#i learn what a csv is bw.
print(f'data shape: {train.shape}')  #corrected some misunderstandings of
#f-string,using print(f'{data shape:}train.shape') before
print(f'{n}this is info')  #sadly,due to the feature of .info,we can only do so
print('\n')  #to avoid a print like None.i know some pythonic philosophy bw
train.info()
print('\n' + f'this is describe{n}{train.describe()}')  #i find without (),it
# will print some thing not expected
#i take a quick look bw,i don't need to use it now
print('\n' + f'this is head{n}{train.head()}')

print(f'{n}---Preliminary investigation results---')
#let's see the total rate
survived_rate = train['Survived'].mean  #i didn't know the average meaning
# of mean before
print(f'{n}the total survived rate:\n{survived_rate}')

#sigh:i am going rewrite all with python standard library
#pause temporarily,i am really tired,sorry for every reader

#i am back, let's go on

test = train.groupby('Sex')
#print(f'{n}{test}')
#we try to write like this first and get a print like<pandas.core.groupby.gene
# ric.DataFrameGroupBy object at 0x000002042FC7DBD0>,which is unexpected
#let's see what it is. AI told me it's a memory address.
#let's try to get the data

print(n)
for name, group in test:
    print(f'Group: {name}')
    print(group)  #interesting. we can use any variable name
    print(f'{n}-------------{n}')
#Male = test.get_group('male')
#print(n)
#print(Male) #I guess we has been too far off track my bro :(
#the same output
#a final round of in-depth exploration
print(n)

#——————————————————————————————————————————————————————————————————————
#test = train.groupby('Sex')
#LET US HAVE AN INTERESTING COMPARE
#——————————————————————————————————————————————————————————————————————

#the best one
#print(train.groupby('Sex')['Survived'].mean())
#or df.groupby('Sex').mean()['Survived'],but the latter is much better
#for there is some possible order problem
#or print(test['Survived'].mean())

#——————————————————————————————————————————————————————————————————————

#a thought extension
#print(n)
#for name, group in test:
#    print(f'Group: {name}')
#    print(group)  #interesting. we can use any variable name
#    print(f'{n}-------------{n}')

#——————————————————————————————————————————————————————————————————————

#an evil version

# print(f'this is an error message: {n}')
# for a,b in test.groups.items():
#    print(f'Group: {a}' + '\n')  #why it cannot work!!? to check it tomorrow
#    print(f'{b}' + '\n') #sigh: an index,so "good",emm,let's try something
#    print(f'{train.loc[b].to_string(index=False)}' + '\n') # it prints
# all the list,jump it

# good,i like this compare

#——————————————————————————————————————————————————————————————————————


print(f'this is group{n}{test.groups}{n}')  #ehhh,how to wrap a line when displaying the
#next type of data? pprint or traversal.
print(f'this is size {n}{test.size()}{n}')
#of course a memory address again when not including () inside

#we are on the track again now

#mean = test.mean()
#print(f'{n}{mean}')
#dang: what's wrong? it cannot run
#eghh,we have text type in. get it.

Sex_mean = test['Survived'].mean()  #just like dict type
print(n)
print(f'this is Sex_mean{n}{Sex_mean}')
Pclass_mean = train.groupby('Pclass')['Survived'].mean()
print(n)
print(f'this is Pclass_mean{n}{Pclass_mean}')
print(n)
print(f'the missing value of Pclass: {train["Pclass"].isnull().sum()}{n}')

#a test
#print(f'mean test:{n}')
#print(test.mean)
#of course a memory address


fig, axes = plt.subplots(1, 2, figsize=(6, 4))  #that's fun,fig means figure
#and axes means axis.
#interesting,if I change the row or col it won't work,now I know that's
#because there is an additional dimensionality.and we must
#modify the axe match like[0,0]
Sex_mean.plot(kind='bar', ax=axes[0], title='Survival Rate by Sex')  #strange,
#'ax' seemed to be repeated.but now probably know why we need to assign axe[n]
#and what if without assigning
Pclass_mean.plot(kind='bar', ax=axes[1], title='Survival Rate by Pclass')
plt.show(block=False)  #if within print(),also output none as .info()

# now let's process the data

# 1. dealing with the gender data
train['Sex_encoded'] = train['Sex'].map({'female': 1, 'male': 0})

#——————————————————————Handle unspecified values——————————————————————————————

#final_s = train['Sex'].map({'female': 1, 'male': 0}).fillna(-1)
#print(final_s)

# should we learn Categorical? to think.

# I am going to learn loc, and iloc

#——————————————————————————————————————————————————————————————————————


#pclass_dummies = pd.get_dummies(train['Pclass'], prefix='Pclass')
#train = pd.concat([train, pclass_dummies], axis=1)

# i will learn one-hot bw.

#
#age_median = train['Age'].median()
#train['Age_filled'] = train['Age'].fillna(age_median)

#
#features = ['Sex_encoded', 'Pclass_1', 'Pclass_2', 'Pclass_3', 'Age_filled', 'SibSp', 'Parch', 'Fare']
#X = train[features]  #
#y = train['Survived']  # 

#plt.close()

#print("features: ")
#print(X.head())
