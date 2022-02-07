import re

def remove_sign(sentence):
    return re.sub('[,/./?/:]', '', sentence)


def split_sentence(sentence):
    return sentence.split()


if __name__ == "__main__":
    sentence = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
    sign_removed_sentence = remove_sign(sentence)
    print([len(word) for word in split_sentence(sign_removed_sentence)])
