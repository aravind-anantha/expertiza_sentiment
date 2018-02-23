# Sentiment Analysis to Improve Peer Reviews in Expertiza

## Objective of the project

**Expertiza** is a platform to create reusable learning objects through peer review. One of the ways to improve the peer reviews given by other students is by sentiment analysis on the reviews before submission. We can then give feedback to the reviewer if the tone of the review is too harsh such that it is not taken seriously by the student receiving it. The main objective of the work done was to add features into Expertiza to identify the tone of a peer review before submission and present the results in a manner that the reviewer can easily understand.

## Dataset

The dataset used for this project was obtained from the peerlogic warehouse and contains about 200000 peer reviews from different courses across different domains. 

## Model

Semantic Orientation Calculator (SO-CAL) [Lexicon-Based Methods for Sentiment Analysis, Taboada et al., 2011](http://www.aclweb.org/anthology/J11-2001) is a lexicon based method for extracting sentiment. It uses dictionaries of words annotated with their orientation, and incorporates intensifiers and negation. The main reason for using SO-CAL is that its performance is consistent across domains and on completely unseen data. Semantic orientation is a measure of subjectivity and and opinion in text. The assumptions that SO-CAL makes is that individual words have a prior polarity that is independent of context and that the said semantic orientation can be expressed as a numeric value. 
A basic outline of how the method is as follows. 
1. Stem the word.
2. Look for intensifiers.
3. Look for negation.
4. Look for negation external intensifiers.
5. Apply intensification and negation, if necessary. 
6. Apply other types of modifiers, such as those relevant for capitalization, punctuation, repetition etc.
7. Return output.

For Expertiza after a lot of trial and error, it was found that using only adjectives gives the best results. Also, the adjective dictionary has been modified to suit our requirements. Some of the commonly used adjectives with a negative orientation do not really carry a negative opinion in the case of technical writing. The dictionary has been modified to satisfy these conditions. 
The entire model was built in python and the working model was wrapped up as a web service in python using Flask.
