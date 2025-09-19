"""
below are today's practice,including several versions attaching my thought process.
"""

#this feat outputs ordinal numerals

#for n in range(1,10):
#  if any(n != a for a in [1,2,3]):
#    print(f{n} + "th")
#  elif n == 1:
#    print(n + "st")
#  elif n == 2:
#    print(n + "nd")
#  elif n == 3:
#    print(n + "rd")

#this one's foolish,i write it with my phone so i cannot see any  error
#reminder until the ai i used as a python tell me.
#it shows that i know little about performance overhead,which is as
#proven in the next versions.in this one,any() is not necessary at all :(
#it use more performance.and sadly,my understanding about the f-string's not
#all right.now i probably know how to use it and it could process types
#automatically most of the cases.

for n in range(1,10):
    if n not in [1, 2, 3]:
        print(f"{n}th")
    elif n == 1:
        print(f"{n}st")
    elif n == 2:
        print(f"{n}nd")
    elif n == 3:
        print(f"{n}rd")
#a revision,not much to say.'not in' is more efficient.

#let's see another feat functions store some casual understandings

#words = {
#"join" : "add"
#"print" : "output"
#"if" : "judge"
#}
#while:
#  n = 1
#  print(words[n])
#  n = n + 1
#  if n = 3:
#    break
#print("thats all")

#a disater at all!! also written on phone
#we forget to python is not "clever" enough to add commas
#we don't give while a condition
#we don't know that cannot use index at the whole dict and
#.keys() and .values()
#we use a unnecessary break
#so "good",right? i must learn more
#by the way,this is as a base for a section of loooong dict
#so i don't use 'for'

#a recision

words = {
    "join": "add",
    "print": "output",
    "if": "judge"
}

n = 0
while n < 3:
    print(list(words.values())[n])
    n = n + 1

print("thats all")

#i am not satisfied about it,but let's jump it this time
#i schedule to optimize my old codes in practice sooner or later


#to be a PYTHONIC MAN!!