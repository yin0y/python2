from googletrans import Translator

translator = Translator()

sentence = input("책을 읽으며 인상깊었던 구절을 적어주세요 : ")


result1 = translator.translate(sentence,"en")
result2 = translator.translate(sentence,"ja")
detected = translator.detect(sentence)

print("===========번역 결과=============")
print("입력어-",detected.lang,":",sentence)
print("번역어1-",result1.dest,":",result1.text)
print("번역어2-",result2.dest,":",result2.text)
print("=================================")