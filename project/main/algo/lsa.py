# -*- coding: utf-8 -*-
"""LSA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18CzmkqwlE1U8d-c54SIB2q0rHogziNaS
"""

import sumy
import numpy
import os

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer

import nltk
nltk.download('punkt')


def execute(document_text , isText ) : 

    directory  = "/home/atharva007/Documents/GitHub/Automatic-Text-Summarizer/project/main/documents/one.txt"
    # opening the file 
    file1 = open(directory , "r")

    # reading the file 
    document = file1.read()

    # printing the document 
    print(document)


    parser = PlaintextParser.from_string(document_text,Tokenizer("english"))



    summarizer_lsa = LsaSummarizer()

    # number of words inthe document 
    numberOfSentences = len(document_text.split('.'))/2

    summary =summarizer_lsa(parser.document ,numberOfSentences)
    for sentence in summary:
        print(sentence)


    print()
    print()
    print("The output of the Algorithm is : ")

    output_text = ""

    print("Sumary : " , summary)
    print("summary type : " , type(summary))

    file = "output3.txt"

    directory = os.getcwd()
    print("current working drectory : " , directory)

    output_text = ""

    """
    with open(os.path.join(directory , file) ,  'w') as file2 : 
        for sentence in summary:
            print(sentence)

            output_text = output_text + sentence

            # writing into the file2
            file2.write(str(sentence))

    """


    for sentence in summary : 
        print(sentence )

        output_text = output_text + str(sentence)

    return output_text
