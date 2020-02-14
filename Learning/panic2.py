phrase = "Don`t panic!"
plist = list(phrase) # Преобразовывает из строки в список символов
print(phrase)
print(plist)

new_phrase = ''.join(plist[1:3]) # Вставляем 'on'
new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[7], plist[6]]) # Вставляем ' tap'
plist = list(new_phrase) # Перезаписываем переменную plist

print(plist)
print(new_phrase)
        
