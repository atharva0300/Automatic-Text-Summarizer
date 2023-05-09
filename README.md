# Automatic-Text-Summarizer
Automatic Text Summarizer with various approaches in NLP and Django


### Approahces used 
 - [x] LexRank
 - [x] LSA (Latent semantic analysis)
 - [x] KL-Sum
 - [ ] Summarization with T5 Transformers
 - [ ] Summarization with BART Transformers
 - [ ] Summarization with GPT-2 Transformers
 - [ ] Summarization with XLM Transformers
 - [ ] Luhn

### Technologies 
 - [x] Django Framework
 - [x] NLTK library for NLP
 - [ ] Postgresql ( currently using Sqlite )
 - [ ] Django REST Framework 

### Improvements for the future 
 - [ ] Inputs not taken for the document text 
 - [ ] Integrating with Postgresql
 - [ ] API creation with DRF
 - [ ] Analysing the performance of the results of all the algos
 - [ ] Manually **Hypertuning** the algos to increase performance
 - [ ] Adding animations and proper styling
 - [ ] A Dashboard to compare the results of all the algos
 - [ ] ( optional ) *Analysis of the text data using elasticsearch ?* 


### Issues 
 - [ ] Output file is not automatically created ( might use callback, asynchronous ? )
 - [ ] The form field of the input algo and text area is not styled properly 
 - [ ] About Page is blank
 - [ ] Slow loading of the algo's ( add Redis for caching ? )

### New Ideas 
 - [ ] Uploading PDF file, extracting text from the file and summarizing it
 - [ ] Uploading Image file, extracting text from the file and summarizing it ( optional )
 - [ ] Obtaining Abbreviation from the document
 - [ ] Knowledge Graphs ( https://www.analyticsvidhya.com/blog/2019/10/how-to-build-knowledge-graph-text-using-spacy/ )
 - [ ] Words Cloud 
 - [ ] Text Evaluation ( metrics )
