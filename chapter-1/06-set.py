from typing import Set, Iterable


def ngram(iterable: Iterable, n=2) -> Set:
    return set(zip(*[iterable[i:] for i in range(n)]))


if __name__ == "__main__":
    word1 = "paraparaparadise"
    word2 = "paragraph"
    ngram1 = ngram(word1)
    ngram2 = ngram(word2)

    print(ngram1 | ngram2)
    print(ngram1 & ngram2)
    print(ngram1 - ngram2)    
    print(f'Xにseが含まれているか: {ngram1 >= {("s", "e")}}')
    print(f'Yにseが含まれているか: {ngram2 >= {("s", "e")}}')
