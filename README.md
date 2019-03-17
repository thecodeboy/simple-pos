# :moyai: Simple Parts of Speech Tagger

A quick hack to tag single words to their parts of speech. Uses [nltk](http://www.nltk.org/) :speech_balloon: under the hood.


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


## License

Copyright 2019 Aishik Saha

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
