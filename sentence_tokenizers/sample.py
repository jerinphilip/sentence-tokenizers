from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktLanguageVars

class BulletPointLangVars(PunktLanguageVars):
    sent_end_chars = ('.', '?', '!', '•')

tokenizer = PunktSentenceTokenizer(lang_vars = BulletPointLangVars())
sentences = tokenizer.tokenize(u"• I am a sentence • I am another sentence")
for sentence in sentences:
    print(sentence)


