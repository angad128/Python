import requests
from bs4 import BeautifulSoup
import operator


def all_words(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)
    for post_text in soup.find_all("a", {"class": "title text-semibold"}):
        content = post_text.string
        words = content.lower().split()
        for each_word in words:
           # print(each_word)
            word_list.append(each_word)
    clean_up_list(word_list)

def clean_up_list(wordlist):
    clean_word_list = []
    for word in wordlist:
        symbloms = "!@#$%^`~&*''\/()_-+=[]{}|:;,.<>?"
        for i in range(0, len(symbloms)):
            wrod = word.replace(symbloms[i], "")
        if len(word) > 0:
            clean_word_list.append(word)
    create_dictonary(clean_word_list)

def create_dictonary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] =1
    # for key&value in word_count dictonary sort items by operator of dictonary (0:key),(1:value)
    for  k, v in sorted(word_count.items(), key = operator.itemgettter(1) ):
        print(k,v)

all_words('https://thenewboston.com/forum')



