# -r	--reverse	逆順で並べ替える
# -n	--numeric-sort	文字列を数値と見なして並べ替える
# -k 指定	--key=指定	場所と並べ替え種別を指定する

cat ./data/popular-names.txt | sort -rnk 3