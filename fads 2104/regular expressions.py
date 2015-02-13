# Sandeep Yalamanchili

# class of strings matched by the following regular expressions.
import re
import nltk
def main():

    sentence = '''Textron is an American industrial conglomerate.
            Textron includes Bell Helicopter, Cessna Aircraft,
            and other components. It was founded by Royal Little
            in 1923 as the Special Yarns Company, and is now
            headquartered in Providence, Rhode Island 19333.''' 

    

    print('''It contains a set of strings which has atleast one small or
                    capital letter alphabets but does not contain nunbers\n\n''')

    nltk.re_show('[a-zA-Z]+',sentence)



    print('''\n It contains a set of strings which stars with a upper case letter
              and folowed by any number of small case letters and
              this doest not contain any numbers in between them\n''')

    nltk.re_show('[A-Z][a-z]*',sentence)



    

    print('''\nThe words that starts with p and ends with t and can have atmost
          ovels in between p and t\n''')

    nltk.re_show('p[aeiou]{,2}t',sentence)



    print('''\n Set of strings starts with a digit and may have a dot and
             folowed by digits or nothing\n''') 

    nltk.re_show('\d+(\.\d+)?',sentence)

    

    print(''' \n The words which doesn't start with lower case ovels folowed by
          small case ovel and third character which isn't ovel,
          And these structure can be repeated any number of times\n''')

    nltk.re_show('([^aeiou][aeiou][^aeiou])*',sentence)

    

    print('''\n Contains any number of alphanumeric characters including underscore or
                string contains non alphanumeric and non whitespace characters\n''')

    nltk.re_show('\w+|[^\w\s]+',sentence)

    

main()


    

