# -*- coding: utf-8 -*-

import sys
import logging
import json
from gensim.models.keyedvectors import KeyedVectors

def dump_json(data, filename):
    """ Dump data to json output file. """
    
    with open(filename, 'wt', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2, sort_keys=True)

def find_most_similar(model, syn_dict, restriction):
	""" Return dictionary of headwords and their n most similar words. """ 

	most_similar = {}
	for headword, synonyms in sorted(syn_dict.items()):
		# Headword with embeddings and with at least one synonym with embeddings
		if headword in model.vocab and any(s in model.vocab for s in synonyms):
			if headword not in most_similar:
				most_similar[headword] = []
				# Find 10 most similar words of headword
				if restriction == "None":
					for i in model.similar_by_word(headword, topn=10, restrict_vocab=None):
						most_similar[headword].append(i)  
				else:
					for i in model.similar_by_word(headword, topn=10, restrict_vocab=int(restriction)):
						most_similar[headword].append(i) 

	return most_similar

def main():
	logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
	
	synonyms = 'synonym-dictionary.json'
	model_path = sys.argv[1]
	most_similar_path = sys.argv[2] 
	restriction = sys.argv[3] # Only compute cosine between headword and the 'restriction' most frequent words

	model = KeyedVectors.load_word2vec_format(model_path, binary=False)
	with open(synonyms, 'rt', encoding='utf-8') as s:
		syn_dict = json.load(s)
		most_similar = find_most_similar(model, syn_dict, restriction)
		dump_json(most_similar, most_similar_path)

if __name__ == '__main__':
    main()