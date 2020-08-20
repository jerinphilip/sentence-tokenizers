from argparse import ArgumentParser
import nltk
from nltk.tokenize.punkt import PunktTrainer, PunktSentenceTokenizer
import pickle

def inspect_tokenizer(tokenizer):
    param_keys = ['abbrev_types', 'collocations', 'sent_starters']
    for key in param_keys:
        print(key, getattr(tokenizer._params, key))
        print()

def _inspect(save_path):
    formatted_path = 'file:{}'.format(save_path)
    tokenizer = nltk.data.load(formatted_path)
    inspect_tokenizer

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--save-model', type=str, required=True)
    args = parser.parse_args()
    _inspect(args.save_model)

