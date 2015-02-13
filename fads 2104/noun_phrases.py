# Sandeep Yalamanchili
# plural noun phrases


import nltk,re

def noun():
    grammar = "NP: {<NNS>}"

    cp = nltk.RegexpParser(grammar)
    sentence = [("Rapunzel", "NNP"), ("let", "VBD"), ("down", "RP"),
                ("her", "PP$"), ("long", "JJ"), ("golden", "JJ"), ("hair", "NN")]
    sentence2 = [("many","JJ"), ("researchers","NNS"), ("two","CD"),
                 ("weeks","NNS"), ("both","DT"), ("new","DT"), ("new","JJ"),
                 ("posotions","NNS")]

    print(cp.parse(sentence2))

noun()


