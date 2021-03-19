import json
import pinyin


def process_row(key, value):
    import pinyin
    out = ''
    for i in value:
        out += i
        out += '\t'
        out += pinyin.get(key, format='strip', delimiter=' ')
        out += '\t1\n'
    return out

for k, v in d.items():
     all_out += process_row(k, v)

all_out = ''
open('rime-output.txt', 'w').write(all_out)
