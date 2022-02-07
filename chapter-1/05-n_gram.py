from typing import List, Iterable


def ngram(n: int, iterable: Iterable) -> List:
    return list(zip(*[iterable[i:] for i in range(n)]))


if __name__ == "__main__":
    sentence = "I am an NLPer"
    print(ngram(2, sentence))
    print(ngram(2, sentence.split()))