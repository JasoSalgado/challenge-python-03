# Resolve the problem!!
# -*- coding: utf-8 -*-
import re

def run():
    with open('encoded.txt', 'r') as f:
        hidden_text = f.read()
    
    regex = re.compile('[a-z]')
    show_message = re.findall(regex, hidden_text)

    join_message = ''.join(show_message)
    print(join_message)


if __name__ == '__main__':
    run()
