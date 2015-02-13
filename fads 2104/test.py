def achr(sents):

                      x = ""

                      for word in sents:
                             x = x + "".join(word[-1])
                      return x.lower()

def main():

                txt = ["RANDOM", "ACESS", "MEMORY"]

                outp =  achr(txt).lower()

                print(outp)

main()
