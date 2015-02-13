#Sujitha kamineni
import nltk
from nltk.corpus import state_union as stu
import matplotlib

def main():
     cfd = nltk.ConditionalFreqDist(
           (target, fileid)
           for fileid in stu.fileids()
           for w in stu.words(fileid)
           for target in ['men', 'women',"people"]
            if w.lower().startswith(target))
cfd.plot()

main()
