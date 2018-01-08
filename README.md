# The Norwegian Synonymy Test Set

This repository holds the Norwegian Synonymy Test Set, created for the purpose of evaluating 
distributional semantic models. 

## Terms of use

The Norwegian Synonymy Test Set is derived from Kunnskapsforlaget's "Norske synonymer blåordbok" 
by Dag Gundersen and has been created for the evaluation of distributional models of semantic word similarity. 
The resource is distributed under the [Creative Commons Attribution-NonCommercial-ShareAlike license (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/) for academic research purposes only.

## Format 

The test set ```norwegian-synonyms.json``` contains 27,601 
headwords and 111,111 synonym tokens (and 32,303 syonym types). The test set is distributed as a 
JSON dictionary with headwords as entries. Each headword is associated with a list of its synonyms. 
We do not differentiate between word meaning, e.g., the lists are flat:

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
with regards to ```norwegian-synonyms.json``` or some cut-off created in ```cutoff.py```.
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
we provide them in a separate dictionary ```spelling-variants.json```. 
