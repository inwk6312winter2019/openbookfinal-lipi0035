#Task 1a---1---Print unique words

def unique_words(fin):
  d = {}
  ls = []
  for line in fin:
    line = line.strip()
    words = line.split()
    for word in words:
      word = word.strip('.,:?")!')
      #print(word)
      d[word] = d.get(word,0)+1
  for key in d.keys():
    ls.append(key)
  return ls

fin1_unique_words = open("Book1.txt")
keys1 = unique_words(fin1_unique_words)
print("List of unique words in book1 : ")
print(keys1)

fin2_unique_words = open("Book2.txt")
keys2 = unique_words(fin2_unique_words)
print("List of unique words in book2 : ")
print(keys2)

fin3_unique_words = open("Book3.txt")
keys3 = unique_words(fin3_unique_words)
print("List of unique words in book3 : ")
print(keys3)

#Task 1a---2---Count number of articles

def count_the_articles(fin):
  count = 0
  articles = ["a", "the", "at", "run", "to","and","are","or","for","an","this"]
  for line in fin:
    line = line.strip()
    words = line.split()
    for word in words:
      word = word.strip('.,:?")!')
      if word in articles:
        count = count + 1
  return count

fin1_count_articles = open("Book1.txt")
no_of_articles1 = count_the_articles(fin1_count_articles)
print("Number of articles in book1 : {}".format(str(no_of_articles1)))

fin2_count_articles = open("Book2.txt")
no_of_articles2 = count_the_articles(fin2_count_articles)
print("Number of articles in book2 : {}".format(str(no_of_articles2)))

fin3_count_articles = open("Book3.txt")
no_of_articles3 = count_the_articles(fin3_count_articles)
print("Number of articles in book3 : {}".format(str(no_of_articles3)))

#Task 1a---3---sorted words

def sorted_words(fin):
  d1 = {}
  d2 = {}
  ls = []
  sorted_ls = []
  for line in fin:
    line = line.strip()
    words = line.split()
    for word in words:
      word = word.strip('.,:?")!')
      d1[word] = d1.get(word,0)+1
  for key in d1.keys():
    ls.append(key)
  for word in ls:
    count = 0
    for c in word:
      count += 1 
    d2[word] = d2.get(word,0) + count     
  for key,val in sorted(d2.iteritems(), key = lambda(k,v):(v,k)):
    sorted_ls.append(key)
  return sorted_ls

fin1_sorted_words = open("Book1.txt")
sorted_words1 = sorted_words(fin1_sorted_words)
print("Sorted word list of book1 : " +str(sorted_words1))

fin2_sorted_words = open("Book2.txt")
sorted_words2 = sorted_words(fin2_sorted_words)
print("Sorted word list of book2 : " +str(sorted_words2))

fin3_sorted_words = open("Book3.txt")
sorted_words3 = sorted_words(fin3_sorted_words)
print("Sorted word list of book3 : " +str(sorted_words3))

#Task 1a---4---character_word_count

def character_word_count(fin):
  d1 = {}
  d2 = {}
  ls = []
  for line in fin:
    line = line.strip()
    words = line.split()
    for word in words:
      word = word.strip('.,:?")!')
      d1[word] = d1.get(word,0)+1
  for key in d1.keys():
    ls.append(key)
  for word in ls:
    count = 0
    for c in word:
      count += 1 
    d2[word] = d2.get(word,0) + count
  return d2

fin1_character_word_count = open("Book1.txt")
character_word_count1 = character_word_count(fin1_character_word_count)
print("Dictionary with character_word_count for book1 : " +str(character_word_count1))

fin2_character_word_count = open("Book2.txt")
character_word_count2 = character_word_count(fin2_character_word_count)
print("Dictionary with character_word_count for book2 : " +str(character_word_count2))

fin3_character_word_count = open("Book3.txt")
character_word_count3 = character_word_count(fin3_character_word_count)
print("Dictionary with character_word_count for book3 : " +str(character_word_count3))

#Task 1a---4---starts_with_vow

def starts_with_vow(fin):
  tup = ("a", "e", "i", "o", "u")
  count = 0
  for line in fin:
    line = line.strip()
    words = line.split()
    for word in words:
      if(word[0] in tup):
        #print(word)
        count += 1
  return count

fin1_starts_with_vow = open("Book1.txt")
starts_with_vow1 = starts_with_vow(fin1_starts_with_vow)
print("Number of words starting with a vowel in book1 : " +str(starts_with_vow1))

fin2_starts_with_vow = open("Book2.txt")
starts_with_vow2 = starts_with_vow(fin2_starts_with_vow)
print("Number of words starting with a vowel in book2 : " +str(starts_with_vow2))

fin3_starts_with_vow = open("Book3.txt")
starts_with_vow3 = starts_with_vow(fin3_starts_with_vow)
print("Number of words starting with a vowel in book3 : " +str(starts_with_vow3))






