# -*- coding: utf-8 -*-

import sys
import json
import gzip

class Sentences(object):
    def __init__(self, filename):
        self.filename = filename
 
    def __iter__(self):
        for line in gzip.open(self.filename, 'rb'):
            yield line.decode('utf-8').split()

def dump(data, filename):
    """ Dump data to json output file. """
    
    with open(filename, 'wt', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2, sort_keys=True)

def freq_dict(synonyms, sentences):
    """ Return frequency dictionary of words present in synonym resource and corpus. """

    fd = {}

    with open(synonyms, 'rt', encoding='utf-8') as s:
        syn_dict = json.load(s)

        # Initialize frequency dictionary
        for headword, synonyms in sorted(syn_dict.items()):
            if headword not in fd:
                fd[headword] = 0
            for s in synonyms:
                if s not in fd:
                    fd[s] = 0

        # Add frequencies of words present in both synonym resource and corpus
        for words in sentences:
            for word in words:
                if word in fd:
                    fd[word] += 1
                    
    return fd

def cutoff(freq_dict, synonyms, n):
    """ Return dictionary of words occurring n or more times in corpus. """
    
    cutoff_n = {}

    with open(synonyms, 'rt', encoding='utf-8') as d: 
        syn_dict = json.load(d)
        for headword, synonyms in sorted(syn_dict.items()):
            if headword in freq_dict and freq_dict[headword] >= n:
                if any(s in freq_dict and freq_dict[s] >= n for s in synonyms):
                    cutoff_n[headword] = synonyms

    return cutoff_n

def main():
    synonyms = 'synonym-dictionary.json'
    corpus = sys.argv[1]
    sentences = Sentences(corpus)
    
    freq_dict = synonym_freq_dict(synonyms, sentences)    
    cutoff_5 = cutoff(freq_dict, synonyms, 5)
    dump(cutoff_5, 'synonym-dictionary-cutoff-5.json')

if __name__ == '__main__':
    main()