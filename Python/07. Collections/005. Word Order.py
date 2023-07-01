# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter,OrderedDict
class OrderedCounter(Counter,OrderedDict):
    pass
n= int(input())
words= []
count = {}
for i in range(n):
   word = input().strip()
   words.append(word)
word_counter = OrderedCounter(words)

print(len(word_counter))

for j in word_counter:
    print(word_counter[j],end=' ')

