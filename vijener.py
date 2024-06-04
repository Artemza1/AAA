import spy
import re


style = input("Выберите вариант работы(напишите [з] для шифровки, букву [р] для расшифровки: ").upper()
if style not in ['З','Р', 'з', 'р']:
	print("Только зашифровать или расшифровать!!!!"); raise SystemExit    #завершение работы
Message = input("Сообщение для шифра: ").upper()
Key = input("Шифр-ключ: ").upper()
Message1 = re.sub("[^А-Яа-я]", "", Message)
Key1 = re.sub("[^А-Яа-я]", "", Key)
def specify(mode, message, key):
	key *= len(message) // len(key) + 1
	chipher_mes = ""

	for a, b in enumerate(message):
		if mode in ['З','з','зашифровать', 'Зашифровать']:
			chipher = ord(b) + ord(key[a])
		else:
			chipher = ord(b) - ord(key[a])

		chipher_mes += chr(chipher % 32 + ord('А'))       #если необходимо зашифровать на англ то вместо 32 ставим 26
	return chipher_mes
print("Зашифрованное сообщение:",specify(style, Message1, Key1))





# chr - целое число, представляющее символ в таблице Unicode
# ord - символ, для которого нужно получить числовое значение Unicode
# enumerate - разбивает сообщение на символы (ключ-значение)
# re.sub - находит все символы не входящие в указанный диапазон и заменяет их на то что укажем, в моем случае все символы кроме букв русского алфавита заменит на ничего
