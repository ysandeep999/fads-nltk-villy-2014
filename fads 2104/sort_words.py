

def cmp_len(word1,word2):
    if cmp(word1,word2) == 1:
        return 1
    elif cmp(word1,word2) == 0 :
        return 0
    elif cmp(word1,word2) == -1:
        return -1


def main():
    lst = ['abaa','aba','ab','a']

    ls1 = sorted(lst,cmp=cmp_len)

    print(ls1)

main()
