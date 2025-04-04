import re
file = open('text.txt', 'r').read()  #
emails = re.findall(r'\b[^!#$%&*+-/=?^_`{|}~]+[a-zA-Z0-9._-]+@[a-zA-Z]+\.+[a-zA-Z]+', file)
print(emails)
phones = re.findall(r'\+7+-+\d{3}-+\d{3}-+\d{2}-+\d{2}', file)
print(phones)
capital_words = re.findall(r'\b[A-ZА-ЯЁ][a-zа-яё]*\b', file)
print(capital_words)
result1 = open('emails.txt','w')
for i in emails:
    result1.write(i + '\n')
result2 = open('phones.txt','w')
for j in phones:
    result2.write(j + '\n')
result3 = open('capital_words.txt','w')
for k in capital_words:
    result3.write(k + '\n')
result1.close()
result2.close()
result3.close()


