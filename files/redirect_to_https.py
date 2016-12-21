#!/usr/bin/env python

import sys


def modify_url(new_line):

    get_url = new_line.split(' ')
    # first element of the list is the URL
    old_url = get_url[0]
    new_url = "\n"
    if old_url.startswith('http'):
        old_url_protocol = old_url.split(':')
        new_url = 'https:' + old_url_protocol[1] + "\n"
    return new_url

if __name__ == '__main__':
    new_line = sys.stdin.readline().strip()
    new_url = modify_url(new_line)
    sys.stdout.write(new_url)
    sys.stdout.flush()
