# -*- coding: utf-8 -*-


import random

def shuffle_word(word):
    # 単語の先頭と末尾の文字は残し、それ以外の文字の順序をランダムに並び替える
    # 長さが４以下の単語は並び替えない
    if len(word) <= 4:
        return word
    else:
        return word[0] \
            + ''.join(random.sample(word[1:-1], len(word)- 2 ))\
            + word[1]

if __name__ == "__main__":
    sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind."
    print(" " .join(shuffle_word(word) for word in sentence.split()))
