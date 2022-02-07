# -*- coding: utf-8 -*-


def split_sentence(sentence):
    return sentence.split()

if __name__ == "__main__":
    sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    splited_sentence = split_sentence(sentence)

    first_character_index = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    mapping_dict = {}
    for i, word in enumerate(splited_sentence):
        if i + 1 in first_character_index:
            mapping_dict[word[:1]] = i + 1
        else:
            mapping_dict[word[:2]] = i + 1
    print(mapping_dict)
