from .punkt import PunktSentenceTokenizer, PunktLanguageVars

class BulletPointLangVars(PunktLanguageVars):
    sent_end_chars = ('.', '?', '!', '•')

tokenizer = PunktSentenceTokenizer(lang_vars = BulletPointLangVars())
# sentences = tokenizer.tokenize(u"• I am a sentence• I am another sentence? Am I not!")
sentences = tokenizer.tokenize("""You know what I've noticed? Nobody panics when things go "according to plan"... even if the plan is horrifying. If, tomorrow, I tell the press that, like, a gang-banger will get shot, or a truckload of soldiers will be blowing up, nobody panics, because "it's all part of the plan". But I say that one little old mayor will die... well then everyone loses their minds! Introduce a little anarchy. Upset the established order, and everything becomes chaos. I'm an agent of chaos. Oh, and you know the thing about chaos?  It's fair.""")

for sentence in sentences:
    print(sentence)


