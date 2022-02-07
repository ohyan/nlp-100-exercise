# -*- coding: utf-8 -*-


def cipher(str):
    processed_characters = [chr(219 - ord(x)) if x.islower() else x for x in str]
    return ''.join(processed_characters)

if __name__ == "__main__":
    sentence = "the quick brown fox jumps over the lazy dog"
    print(cipher(sentence))
    print(cipher(cipher(sentence)))