from argparse import ArgumentParser
from nltk.tokenize.punkt import PunktTrainer, PunktSentenceTokenizer
import nltk
import pickle

def test(test_corpus_path, model):
    with open(test_corpus_path, 'rb+') as save_file:
        tokenizer = pickle.load(save_file)
        with open(test_corpus_path) as test_file:
            contents = test_file.read()
            contents = contents.replace('\n', ' ')
            sentences = tokenizer.tokenize(contents)
            for sentence in sentences:
                print(sentence)



if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--test-corpus', type=str, required=True)
    parser.add_argument('--save-model', type=str, required=True)
    args = parser.parse_args()
    test(args.test_corpus, args.save_model)
