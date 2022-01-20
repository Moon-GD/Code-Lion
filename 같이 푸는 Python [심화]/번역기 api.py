# pip uninstall googletrans
# pip install googletrans==4.0.0-rc1

from googletrans import Translator

translator = Translator()

print('영어와 불어로 번역합니다.')
sentence = input('번역할 문장을 입력해주세요. ')

detected = translator.detect(sentence)

en_result = translator.translate(sentence, 'en', src=detected.lang)
fr_result = translator.translate(sentence, 'fr', src=detected.lang)

print(f'기존 문장 : {sentence}')
print('-----------------------------')
print(f'en : {en_result.text}')
print(f'fr : {fr_result.text}')
print('-----------------------------')
