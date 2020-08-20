from nltk.tokenize.punkt import PunktLanguageVars

def debug_cls(cls):
    _d = {key:value for key, value in cls.__dict__.items() if not key.startswith('__') and not callable(key)}
    from pprint import pprint
    pprint(_d)

delimiters = {
    'hi': '\u0964',
    'bn': '\u0964',
    'ur': '\u06D4'
}

def PunktDelimiter(lang):
    # The symbols are obtainable here.
    # https://apps.timwhitlock.info/unicode/inspect?

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

def PostFixHack(lines, lang):
    if lang in delimiters:
        delim = delimiters.get(lang)
        fixed_lines = []
        if lang in lang_delimiters:
            for line in lines:
                segments = line.split(delim)


