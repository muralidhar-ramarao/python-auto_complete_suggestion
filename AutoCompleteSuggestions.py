#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 17:21:25 2016

@author: muralidharramarao
Source words.txt: https://github.com/dwyl/english-words 
"""

from collections import Counter
import re
import os

def words(text):
    '''
    This function will take the text as an input and extract all
    the words from text stripping the newline char.    
    '''
    return re.findall('\w+',text.lower())

def checkWordsFile(fname):
    '''
    This function will check if the helper file words.txt exists.
    if the file is not available in the current directory, it will
    attempt to download. if the 
    
    '''
    if not os.path.exists('/'.join([os.path.abspath('.'),fname])):
        print 'Unable to find the file words.txt. Please visit the '\
              'below website to download the file \'words.txt\'.\n'\
              'https://github.com/dwyl/english-words'
        print
        print 'Note: Remember to place the file in the same folder as '\
              'AutoCompleteSuggestions.py'
    exit()
    

WORDS=Counter(words(open(checkWordsFile('words.txt'),
                         'r').read()))

def checkWordsStartWith(text):
    '''
    This function will get all the words starting with the input 
    value, and passes utmost 7 matching words returned from the
    helper function knwon().
    '''
    gotWords= known(text)
    return list(gotWords)[:7]

def known(text):
    '''
    
    '''
    return (w for w in WORDS if w.startswith(text))
    
def suggest(text):
    wordlist = checkWordsStartWith(text)
    if len(wordlist)==1:
        return wordlist[0]
    elif len(wordlist)>1:
        return ('\n  '.join(wordlist))
    return ''

def printResult(result):
    if result=='':
        print'-----------\n No Match Found.\n-----------'
    else:
        print '-----------'
        print '  {0}'.format(result)
        print '-----------'

def main():
    try:
        text=None
        temp=''
        print 'Start Typing a word. '\
              'If you need Suggestions, then press Enter/Return:\n'\
              'Enter < for backspace of a char.'
        while True:
            if text==None: text=''
            text=raw_input(temp)
            temp+=text
            if text=='':
                print 'Your word is: ',temp
                break
            elif text.strip()=='<':
                temp=temp.replace('<','')[:-1]
                print temp
#            else:
            result= suggest(temp.strip().lower())
            if result==temp:
                print 'Your word is:',temp
                break
            elif '\n' not in result and result != '':
                print 'Were you looking for "{0}"?'.format(result)
                if raw_input().strip().lower()=='y':
                    print 'Your word: {0}'.format(result)
                    break
                else:
                    pass
            else:
                printResult(result)
    except KeyboardInterrupt:
        print '\nQuitting...'
    
if __name__=='__main__':
    main()

                