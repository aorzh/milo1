#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
from datetime import datetime


def main():
    abc = sys.argv[1]
    date_list = []
    for x in abc.split('/'):
        date_list.append(int(x))
    # Reverse and prepare year
    for x in date_list:
        if x == 0 or 00:
            date_list[x] = 2000
            break

    date_list.sort()
    if len(str(date_list[0])) < 4:
        date_list[0] += 2000
    elif date_list[0] < 2000 or date_list[0] > 2999:
        print("Is illegal: " + abc)
        return

    # Lets check day and month
    try:
        final_value = datetime(*date_list)
    except ValueError:
        # Lets try to switch d[1] and d[2] and try same
        date_list[1], date_list[2] = date_list[2], date_list[1]
        try:
            final_value = datetime(*date_list)
        except ValueError:
            print("Is illegal: " + abc)
            return

    print(final_value.strftime("%Y-%m-%d"))


if __name__ == '__main__':
    main()
