from argparse import ArgumentParser
from nltk.tokenize.punkt import PunktTrainer, PunktSentenceTokenizer
from nltk.tokenize.punkt import PunktLanguageVars
import nltk
import pickle
from .inspection import inspect_tokenizer

def PunktDelimiter(lang):
    delimiters = {
        'hi': '।',
        'bn': '।',
        'ur': '۔'
    }

    lang_delimiters = delimiters.get(lang, '')
    lang_vars_class_name = 'PunktLanguageVars_{}'.format(lang)

    base_end_chars = PunktLanguageVars.sent_end_vars 

    overrides = {
        sent_end_chars: (base_end_chars + lang_delimiters)
    }

    return type(lang_vars_class_name, (PunktLanguageVars,), overrides)


def train(lang, corpus, save_path):
    # Refer:
    # https://github.com/alvations/DLTK/blob/84bb7daeda21c18424518731928aea103c15caa1/dltk/tokenize/tokenizer.py#L37

    with open(corpus) as fp:
        language_vars = PunktDelimiter(lang)
        punkt = PunktTrainer(lang_vars=language_vars)
        contents = fp.read()
        punkt.train(contents, verbose=True, finalize=True)
        punkt.finalize_training(verbose=True)
        model = PunktSentenceTokenizer(punkt.get_params())

        with open(save_path, 'wb+') as save_file:
            pickle.dump(model, save_file, protocol=pickle.HIGHEST_PROTOCOL)

    inspect_tokenizer(model)

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--train-corpus', type=str, required=True)
    parser.add_argument('--save-model', type=str, required=True)
    parser.add_argument('--lang', type=str, required=True)
    args = parser.parse_args()
    train(args.train_corpus, args.save_model)

