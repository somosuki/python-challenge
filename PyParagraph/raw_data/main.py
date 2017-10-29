# coding: utf-8

f = open("paragraph_1.txt", "r")

data = f.read()

words = data.split(" ") 

num_words = len(words)

lines = data.split(".")

average_sentence=float(len(words))/float(len(lines))

average_words=sum(map(len, words))/len(words)

print("Paragrah Analysis")
print("----------------")
print("Approximate Word Count:", num_words)
print("Approximate Sentence Count:", len(lines))
print("Average Letter Count:", average_words)
print("Average Sentence Length:", average_sentence)



f = open("paragraph_2.txt", "r")

data = f.read()

words = data.split(" ") 

num_words = len(words)

lines = data.split(".")

average_sentence=float(len(words))/float(len(lines))

average_words=sum(map(len, words))/len(words)

print("Paragrah Analysis")
print("----------------")
print("Approximate Word Count:", num_words)
print("Approximate Sentence Count:", len(lines))
print("Average Letter Count:", average_words)
print("Average Sentence Length:", average_sentence)
