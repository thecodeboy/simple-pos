import sys
import nltk

# nltk.set_proxy('http://proxy.example.com:3128', ('USERNAME', 'PASSWORD'))

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
try:
    nltk.data.find('taggers/averaged_perceptron_tagger')
except LookupError:
    nltk.download('averaged_perceptron_tagger')


number_of_arguments = len(sys.argv)

if(number_of_arguments == 1):
    sys.exit("No word entered.")
elif(number_of_arguments > 2):
    sys.exit("Multiple words entered.")
else:
    text = nltk.word_tokenize(sys.argv[1])
    result = nltk.pos_tag(text)
    print(result)
