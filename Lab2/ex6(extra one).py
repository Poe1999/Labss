import re
file = open('text1.txt').read()
dates = re.findall(r'\d{2}\.\d{2}\.\d{4}', file)
new2 = re.sub('\.', '-', str(dates))
r = str(dates)
def change_date_format(r):
    return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', r)
print(change_date_format(r))