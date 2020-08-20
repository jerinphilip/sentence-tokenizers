from argparse import ArgumentParser
import nltk
from .punkt import PunktTrainer, PunktSentenceTokenizer
import pickle

def inspect_tokenizer(tokenizer):
    param_keys = ['abbrev_types', 'collocations', 'sent_starters']
    for key in param_keys:
        print(key, getattr(tokenizer._params, key))
        print()

def _inspect(save_path):
    with open(save_path, 'rb+') as save_file:
        tokenizer = pickle.load(save_file)
        inspect_tokenizer(tokenizer)

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--save-model', type=str, required=True)
    args = parser.parse_args()
    _inspect(args.save_model)

