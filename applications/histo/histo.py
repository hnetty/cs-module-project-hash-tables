# Your code here

import re

def histogram(filename):
    with open(filename) as f:
        words = f.read()

    collect = re.sub('":;,.-+=/\[|]\{\}()*^&', "", words.replace("\n", " "))
    word_list = collect.split()

    longest_word = ""
    word_counts = {}
    for word in word_list:

        if len(word) > len(longest_word):
            longest_word = word
        
        if word not in word_counts:
            word_counts[word] = ""
        word_counts[word] += "#"

    num_left_chars = len(longest_word) + 2

    count_list = list(word_counts.items())
    count_list.sort()
    count_list.sort(key=lambda x: x[1], reverse=True)
    
    for w, c in count_list:
        print(w, " " * (num_left_chars - len(w)), c)

print(histogram("robin.txt"))