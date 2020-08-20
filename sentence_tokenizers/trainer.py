from argparse import ArgumentParser
from nltk.tokenize.punkt import PunktTrainer, PunktSentenceTokenizer
import nltk
import pickle

def train(corpus, save_path):
    with open(corpus) as fp:
        contents = fp.read()
        # print(contents)
        tokenizer = PunktSentenceTokenizer()
        ## contents = contents.replace('\n', ' ')
        params = tokenizer.train(contents, verbose=True)
        # print(tokenizer.tokenize("Hello world. This is a car, Dr. Einstein. But does it work very well, Mr. Hyde?"))
        with open(save_path, 'wb+') as save_file:
            pickle.dump(tokenizer, save_file)

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--train-corpus', type=str, required=True)
    parser.add_argument('--save-model', type=str, required=True)
    args = parser.parse_args()
    train(args.train_corpus, args.save_model)

