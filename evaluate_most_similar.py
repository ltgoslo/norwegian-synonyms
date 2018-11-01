# -*- coding: utf-8 -*-

import sys
import logging
import json
from gensim.models.keyedvectors import KeyedVectors

def evaluate(model, synonym_dict, most_similar, n):
	""" Compute precision and recall. """
	
	# Headwords with at least one correctly predicted synonym
	num_correct = 0 
	# Headwords for which we have predicted synonyms
	num_predicted = 0
	# Headwords in synonym dictionary
	num_headwords = len(synonym_dict) 

	precision = 0 
	recall = 0

	for headword, synonyms in sorted(synonym_dict.items()):
		# Headword for which we have predicted synonyms
		if headword in most_similar:
			num_predicted += 1
			# Headwords with at least one correctly predicted synonym
			if any(s == p[0] for p in most_similar[headword][:n] for s in synonyms):
				num_correct += 1

	precision = num_correct/num_predicted
	recall = num_correct/num_headwords

	print("k={}:".format(n))
	print("Precision: %.4f" % precision)
	print("Recall: %.4f" % recall)

def main():
	logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
	
	synonyms = 'norwegian-synonyms.json'
	model_path = sys.argv[1]
	most_similar_path = sys.argv[2]

	model = KeyedVectors.load_word2vec_format(model_path, binary=False)
	with open(synonyms, 'rt', encoding='utf-8') as s:
		with open(most_similar_path, 'rt', encoding='utf-8') as p:
			syn_dict = json.load(s)
			most_similar = json.load(p)
			for i in [1, 5, 10]: 
				evaluate(model, syn_dict, most_similar, i)

if __name__ == '__main__':
    main()
