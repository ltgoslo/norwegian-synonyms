# The Norwegian Synonymy Test Set

This repository holds the Norwegian Synonymy Test Set, defined for evaluating the task of synonym detection. 
The test set was created by extracting words and synonyms from the digital version of 
Kunnskapsforlaget's "Norske synonymer blåordbok" by Dag Gundersen. 

## Terms of use

The Norwegian Synonymy Test Set is distributed under the 
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) licence
for academic research purposes only.

## Format 

`norwegian-synonyms.json` comprises a total of 24,649 headwords and 106,749 synonym tokens 
(and 30,756 synonym types). The test set is distributed as a JSON dictionary of headwords. 
Each headword is associated with a list of synonyms. We do not differentiate between word meaning, 
e.g., the lists are flat:

```json
{
  "kar": [
    "mann",
    "brukar",
    "basis",
    "potte",
    "strippe",
    "så",
    "beholder"
  ]
}
```

## Evaluation

In order for the evaluation scripts to work, [gensim](https://radimrehurek.com/gensim/) must be installed. 
Further, the `model` must be compatible with the original 
[word2vec](https://code.google.com/archive/p/word2vec/) implementation and provided in text format.

`find_most_similar.py` computes the 10-most similar words of each headword 
in `norwegian-synonyms.json`. It computes cosine scores between the headwords 
and the `restriction` most frequent words and outputs the result as a JSON 
dictionary to `most-similar-path`.

`evaluate_most_similar.py` evaluates the computed 1, 5 and 10 most-similar words 
with regards to `norwegian-synonyms.json`. It essentially computes precision and 
recall scores as two variants of accuracy.
  
### Examples 

`python find_most_similar.py <model> <most-similar-path> <restriction>`

```python evaluate_most_similar.py <model> <most-similar-path>```

## Supplement

A supplementary test set, `norwegian-synonyms-grouped.json`, associates each headword 
with a list of lists of synonyms, e.g., synonyms are grouped by meaning. This test set 
may be used for tasks such as word sense induction. Spelling variants are provided 
separately in `spelling-variants.json`.

## Citing

If you publish work that uses or references this resource, please cite the following 
[master's thesis](https://www.duo.uio.no/handle/10852/61756): 

```
@MastersThesis{Stadsnes18,
  author    =     {Stadsnes, Cathrine},
  title     =     {Evaluating Semantic Vectors for Norwegian},
  school    =     {University of Oslo},
  year      =     {2018}
}
```

Or this [NIK article](http://ojs.bibsys.no/index.php/NIK/article/view/490): 

```
Evaluating Semantic Vectors for Norwegian
Cathrine Stadsnes, Lilja Øvrelid, Erik Velldal
2018
http://ojs.bibsys.no/index.php/NIK/article/view/490
```
