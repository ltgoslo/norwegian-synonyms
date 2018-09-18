# The Norwegian Synonymy Test Set

This repository holds the Norwegian Synonymy Test Set, defined for evaluating the task of synonym detection. 
The test set was created by extracting words and associated synonyms from the digital version of 
Kunnskapsforlaget's "Norske synonymer blåordbok" by Dag Gundersen. 

## Terms of use

The Norwegian Synonymy Test Set is distributed under the 
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) licence
for academic research purposes only.

## Format 

`norwegian-synonyms.json` comprises 24,649 headwords and 106,749 synonym tokens (30,756 synonym types). 
The test set is distributed as a JSON dictionary with headwords as entries. Each headword is associated 
with a list of synonyms. We do not differentiate between word meaning, e.g., the lists are flat:

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

This repository also provides evaluation scripts. In order for the scripts to work, 
[gensim](https://radimrehurek.com/gensim/) must be installed. Further, the `<model>` 
must be compatible with the original [word2vec](https://code.google.com/archive/p/word2vec/)
implementation and provided in text format (or one can modify the script).

```find_most_similar.py``` computes the 10-most similar words of headwords 
in ```norwegian-synonyms.json```. It computes cosine scores between the headwords 
and the <restriction> most frequent words and outputs the result as a JSON dictionary 
to <most-similar-path>.
  
### Example 
```python find_most_similar.py <model> <most-similar-path> <restriction>```

```evaluate_most_similar.py``` evaluates the computed 1, 5 and 10 most-similar words 
with regards to ```norwegian-synonyms.json```.
It essentially computes precision and recall scores as two variants of accuracy.

### Example
```python evaluate_most_similar.py <model> <most-similar-path>```

## Supplement

A supplementary test set ```norwegian-synonyms-grouped.json```, also distributed as a JSON 
dictionary with headwords as entries, associates each headword with a list of lists of its 
synonyms. The synonyms are grouped by meaning and the lists are nested:

```json
{
  "kar": [
    [
      "mann"
    ],
    [
      "brukar",
      "basis"
    ],
    [
      "potte",
      "strippe",
      "så",
      "beholder"
    ]
  ]
}
```

This test set may be used for tasks such as word sense induction. 
To avoid incorrectly adding spelling variants to synonym groups, 
we provide them separately in ```spelling-variants.json```. 
