import re
#
# str1 = "2016 was amazing"
#
# stre = re.split(r'\s+(?=\d)|(?<=\d)\s+',str1)
# #print(stre)
#
#
seq = "indiaYOU123"
# SEQ1 = "127363HARISH9292"
num1 = sum(int(x) for x in re.findall(r'[0-9]' ,seq))
#
num2 = " ".join(re.split('[^a-zA-Z]' , seq))
#
# NUM3 = re.sub("[^a-zA-Z]","",seq)
#
# NUM4 = re.sub("[^0-9]","",seq)
#
print(num1)
print(num2)
# print(NUM3)
# print(NUM4)
# NUM5 = sum(int(x) for x in (re.sub("[^0-9]","",SEQ1)))
# print(NUM5)
sentence = "monday is today "
#print(sentence.replace("is" ,"was"))
#print(sentence.split())
words = sentence.split()

sentence_rev = " ".join(reversed(words))
# #####################################################################
#
# print("*#")
print (sentence_rev)
#
# s = "mystring"
# l = list(s)
# print (l)
#
#
# daysstring = "batman was hero"
# superhero = daysstring.split()
# gear = " ".join(reversed(superhero))
# print(gear)
#
# ########################################
#
# mylist = [1,23,4]
# mylist[2] = 3
# print(mylist)
# mytuple  = (3,45,55)
# print(mytuple)
#
# mydict = {"dg":2, "ha" : 445, "jh":"harihs"}
# print(mydict)

# l=[]
# for i in range(2000,3201):
#
#     if(i%7==0) and (i%5!=0):
#         l.append(str(i))
#
#     print(','.join(l))
from pip._vendor.distlib.compat import raw_input


def fact(x):
    if x==0:
        return 1
    return x*fact(x-1)

x = input(raw_input())
print(x)