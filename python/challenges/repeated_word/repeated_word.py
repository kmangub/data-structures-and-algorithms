from hashtable import HashTable

from linked_list import LinkedList, Node
import re

def repeated_word(long_string):
    split_string = long_string.split()
    hashy = HashTable()
    for word in split_string:
        reg = re.sub(r'[^\w\s]','',word)
        lower = reg.lower()
        if hashy.contains(lower):  
            return lower
        else:
            hashy.set(lower, lower)
    return "No matches"