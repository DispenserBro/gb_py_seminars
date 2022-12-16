# Напишите программу, в которой пользователь будет задавать две строки,
# одна из них - буква, а вторая фраза/слово,
# программа должна посчитать сколько раз буква встретилась во второй строке.
# (Не используя встроенные функции)

letter, word = input('Enter the letter to search: '), input('Enter the phrase: ')
counter = 0

for ltr in word:
    if ltr == letter:
        counter += 1

print(f'Found {counter} letters {letter} in phrase "{word}"')