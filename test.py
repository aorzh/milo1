#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys
from datetime import datetime

def main():
    abc = sys.argv[1]
    date_list = []
    final_value = abc
    for x in abc.split('/'):
        date_list.append(int(x))
    # Reverce and prepare year
    date_list.sort(reverse=True)
    if len(str(date_list[0])) < 4:
        date_list[0] += 2000  
    elif date_list[0] < 2000 or date_list[0] > 2999:
        pass
    
    # Lets check day and month    
    day_index = date_list.index(max(date_list[1], date_list[2]))
    try:
        final_value = datetime(*date_list)
    except ValueError:
        # Lets try to switch d[1] and d[2] and try same
        date_list[1], date_list[2] = date_list[2], date_list[1]
        try:
            final_value = datetime(*date_list)
        except ValueError:
            pass
        
    print(final_value)			
    
if __name__ == '__main__':
    main()
