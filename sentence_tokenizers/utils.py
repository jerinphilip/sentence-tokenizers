from nltk.tokenize.punkt import PunktLanguageVars

def debug_cls(cls):
    _d = {key:value for key, value in cls.__dict__.items() if not key.startswith('__') and not callable(key)}
    from pprint import pprint
    pprint(_d)

def PunktDelimiter(lang):
    # The symbols are obtainable here.
    # https://apps.timwhitlock.info/unicode/inspect?
    delimiters = {
        'hi': '\u0964',
        'bn': '\u0964',
        'ur': '\u06D4'
    }

    lang_delimiters = delimiters.get(lang, '')
    lang_vars_class_name = 'PunktLanguageVars_{}'.format(lang)

    base_end_chars = PunktLanguageVars.sent_end_chars
    sent_end_chars = tuple(list(base_end_chars) + list(lang_delimiters))
    print(lang, sent_end_chars)

    overrides = {
        'sent_end_chars': sent_end_chars
    }

    cls = type(lang_vars_class_name, (PunktLanguageVars,), overrides)
    return cls
