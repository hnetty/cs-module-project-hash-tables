import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
word_list = words.split()


# TODO: analyze which words can follow other words
# Your code here
following = {}
for i, value in enumerate(word_list):
    if value not in following:
        following[value] = []
    if i < len(word_list) - 1:
        following[value].append(word_list[i+1])


# TODO: construct 5 random sentences
# Your code here

def write_sentence():
    start_word = random.choice([x.strip('"') for x in word_list if x[0].isupper()])

    sentence = start_word

    next_word = random.choice(following[start_word])

    while not next_word.endswith(tuple('.?!')):
        next_word = random.choice(following[next_word])
        sentence += f" {next_word}"
    return sentence