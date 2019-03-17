# :moyai: Simple Parts of Speech Tagger

A quick hack to tag single words to their part of speech. Uses [nltk](http://www.nltk.org/) :speech_balloon: under the hood.


### Get started

As a prerequisite, **Python 3** must be installed. Then grab the **nltk** package from **pip** as shown below.

```
pip3 install nltk
```


## Running the program

Keeping things simple, the program takes a single word as input and provides it's part of speech.

```
python3 pos_tag.py cards
```

The output in the above case would be,

```
[('cards', 'NNS')]
```

If you're running this behind a proxy, then just enter these details inside the file **pos_tag.py**.

Have fun! :violin:

## Parts of Speech Tags

Below are the tags that you'll see after running this program.

CC  - coordinating conjunction
CD  - cardinal digit
DT  - determiner
EX  - existential there (like: “there is” … think of it like “there exists”)
FW  - foreign word
IN  - preposition/subordinating conjunction
JJ  - adjective ‘big’
JJR - adjective, comparative ‘bigger’
JJS - adjective, superlative ‘biggest’
LS  - list marker 1)
MD  - modal could, will
NN  - noun, singular ‘desk’
NNS - noun plural ‘desks’
NNP - proper noun, singular ‘Harrison’
NNPS - proper noun, plural ‘Americans’
PDT - predeterminer ‘all the kids’
POS - possessive ending parent’s
PRP - personal pronoun I, he, she
PRP$ - possessive pronoun my, his, hers
RB  - adverb very, silently,
RBR - adverb, comparative better
RBS - adverb, superlative best
RP  - particle give up
TO, - to go ‘to’ the store.
UH  - interjection, errrrrrrrm
VB  - verb, base form take
VBD - verb, past tense took
VBG - verb, gerund/present participle taking
VBN - verb, past participle taken
VBP - verb, sing. present, non-3d take
VBZ - verb, 3rd person sing. present takes
WDT - wh-determiner which
WP  - wh-pronoun who, what
WP$ - possessive wh-pronoun whose
WRB - wh-abverb where, when

## License

Copyright 2019 Aishik Saha

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
