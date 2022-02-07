# -*- coding: utf-8 -*-

def concat_letters_alternative(word1, word2):
    return ''.join([i+j for (i, j) in zip(word1, word2)])


if __name__ == '__main__':
    print(concat_letters_alternative('パトカー', 'タクシー'))
