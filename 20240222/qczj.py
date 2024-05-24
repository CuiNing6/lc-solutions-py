from collections import Counter

def fs(s, words):
    if s == '' or words == []:
        return []

    n = len(s)
    res = []

    all_len = sum(map(len, words))
    one_len = len(words[0])

    words =  Counter(words)

    for i in range(0, n-all_len+1):
        tmp = s[i:i+all_len]
        tmp_words = []

        for j in range(0, all_len, one_len):
            if tmp[j:j+one_len] in words:
                if tmp[j:j+one_len] not in tmp_words:
                    tmp_words.append(tmp[j:j+one_len])
        tmp_words = Counter(tmp_words)

        if tmp_words == words:
            res.append(i)

        return res

s = "barfoomathebarfoomatn"
words = ["foo","bar","mat"]

r = fs(s,words)
print(r)