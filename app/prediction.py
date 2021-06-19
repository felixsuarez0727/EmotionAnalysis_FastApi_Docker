from pysentimiento import EmotionAnalyzer
from pysentimiento.preprocessing import preprocess_tweet

emotion_analyzer = EmotionAnalyzer(lang="es")

result=emotion_analyzer.predict("Hola")

probas=result.probas
sentence=result.sentence
idx=result.idx

print(type(result.probas))
print(type(result.sentence))

print(result.probas)
print(result.sentence)
