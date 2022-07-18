#UCSC SIP 2020
This repository contains code for the project CSE-08: Question Answering Data Collection and Analysis" conducted for SIP 2020 at UC Santa Cruz, undertaken under the mentorship of Geetanjali Rakshit.

The primary contributors are:
Rupali Batta, Daniel Fields, Jasmine Tostado

Input: 
Consists of a block for each sentence in The Little Prince Corpus. Each block also contains a file id for the sentence, information about the annotation of the sentence(annotator name, date), as well as the AMR for the sentence.

Output:
Consists of a dictionary with the sentence id, sentence, the AMR, and a list of all the question answer pairs.  

Dependencies: nltk, csv, tensorflow, re, json
