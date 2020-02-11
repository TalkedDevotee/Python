phrase = "Don`t panic!"
plist = list(phrase) # Преобразовывает из строки в список символов
print(phrase)
print(plist)

for i in range(4): # Извлекает 4 последних элемента
    plist.pop()

plist.pop(0) # Излвекает первый элемент
plist.remove('`') # Удаляет апостроф
plist.extend([plist.pop(), plist.pop()]) # Извлекает a, p и вставляет 'ap'
# в том же месте
plist.insert(2, plist.pop(3)) # Извлекает третий элемент и вставляет
# на вторую позицию, смещая третий элемент вправо

new_phrase = ''.join(plist) # Преобразовывает из списка в строку
print(plist)
print(new_phrase)
        
