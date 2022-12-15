files = {}
with open('text/txt1.txt', 'rt', encoding='utf-8') as f1, open('text/txt2.txt', encoding='utf-8') as f2, open('text/txt3.txt',
                                                                                                          encoding='utf-8') as f3:
    files['txt1.txt'] = f1.readlines()
    files['txt2.txt'] = f2.readlines()
    files['txt3.txt'] = f3.readlines()

d1 = (sorted(files.items(), key=lambda item: len(item[1])))

with open('text.txt', 'w', encoding='utf-8') as f:
    for el in d1:
        f.write('\n')
        f.write(str(el[0]))
        f.write('\n')
        f.write(str(len(el[1])))
        f.write('\n')
        f.write(str(el[1]))







