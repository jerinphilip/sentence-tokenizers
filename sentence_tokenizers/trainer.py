from argparse import ArgumentParser
from nltk.tokenize.punkt import PunktTrainer, PunktSentenceTokenizer
import nltk

def train(corpus):
    with open(corpus) as fp:
        contents = fp.read()
        # print(contents)
        tokenizer = PunktSentenceTokenizer()
        tokenizer = nltk.data.load('tokenizers/punkt/malayalam.pickle')
        # contents = contents.replace('\n', ' ')
        #params = tokenizer.train(contents, verbose=True)
        print(tokenizer.tokenize("Hello world. This is a car, Dr. Einstein. BUt does it work very well, Mr. Hyde?"))
        keys = ['abbrev_types', 'collocations', 'sent_starters']
        for key in keys:
            print(key, getattr(params, key))

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--train-corpus', type=str, required=True)
    parser.add_argument('--save-model', type=str, required=True)
    args = parser.parse_args()
    train(args.train_corpus)

