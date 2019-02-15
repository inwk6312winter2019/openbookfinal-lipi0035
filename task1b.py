#Task 1---b---
from collections import OrderedDict

def dic_of_unique_words(fin):
  d = {}
  sorted_d = {}
  sorted_ls = []
  for line in fin:
    line = line.strip()
    words = line.split()
    for word in words:
      word = word.strip('.,:?")!\'')
      #print(word)
      d[word] = d.get(word,0)+1
  return d

def common_words(d1,d2,d3):
  d = {}
  count = 0
  for item in d1.keys():
    if (item in d2.keys()) and (item in d3.keys()):
      count += 1
      d[item] = count
  return d

fin1 = open("Book1.txt")
dic1 = dic_of_unique_words(fin1)
#print("Dictionary of unique words in book1 : ")
#print(dic1)

fin2 = open("Book2.txt")
dic2 = dic_of_unique_words(fin2)
#print("Dictionary of unique words in book2 : ")
#print(dic2)

fin3 = open("Book3.txt")
dic3 = dic_of_unique_words(fin3)
#print("Dictionary of unique words in book3 : ")
#print(dic3)

d_common = common_words(dic1,dic2,dic3)
listname = [] 
for key, value in sorted(d_common.iteritems(), key=lambda (k,v): (v,k),reverse=True):  
  diction= {"value":value, "key":key}  
  listname.append(diction)
print("List of top 20 common words:")
for i in range(20):
  print listname[i]

