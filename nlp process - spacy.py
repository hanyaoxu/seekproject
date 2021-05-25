import spacy
import re

def generate_ngrams(s, n):
    # Convert to lowercases
    s = s.lower()
    
    # Replace all none alphanumeric characters with spaces
    s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)
    
    # Break sentence in the token, remove empty tokens
    tokens = [token for token in s.replace("\u202f",' ').replace("\xa0",' ').replace("\n",' ').split(" ") if token != ""]
    
    # Use the zip function to help us generate n-grams
    # Concatentate the tokens into ngrams and return
    ngrams = zip(*[tokens[i:] for i in range(n)])
    return [" ".join(ngram) for ngram in ngrams]
def write_file(file_name, content):
    with open(file_name,'w') as f:
        f.write(content)

# custom_stop_words = set(['datum','data','experience','work','skill','business','team','development','solution','analysis','design','project','technical','year',
# 'platform','technology','model','science','knowledge','tool','environment','include','ability','require'])

nlp = spacy.load('en_core_web_trf')
all_stopwords = nlp.Defaults.stop_words
# all_stopwords |= {'datum','data','experience','work','skill','business','team','development','solution','analysis','design','project','technical','year',
# 'platform','technology','model','science','knowledge','tool','environment','include','ability','require',}
# # print(all_stopwords)

# def get_token_words(source_file, export_file):

# 2 words
token_words_list = []

with open ('data/da_duties.txt' , 'r' )  as f:
    for item in f:
        for gram in generate_ngrams(item,2):
            tokens = nlp(gram) 
            token_words = [token.text.lower() for token in tokens ]
            token_words_list.append(' '.join(token_words))
                # print(tokens)
                # for i in token_words:
                #     token_words_list.append(i)   
write_file('data/nlp data/da_token_words_2_words.csv','\n'.join(token_words_list))


# 1 words
token_words_list = []

with open ('data/da_duties.txt' , 'r' )  as f:
    for item in f:
        tokens = nlp(item) 
        token_words = [token.lemma_.lower() for token in tokens if not token.lemma_.lower() in all_stopwords and token.is_alpha]
        for i in token_words:
            token_words_list.append(i)   
write_file('data/nlp data/da_token_words_1_word.csv','\n'.join(token_words_list))
      
# if not token.lemma_.lower() in all_stopwords and token.is_alpha

# get_token_words('data/ds_duties.txt','data/nlp data/ds_token_words.csv')

# get_token_words('data/da_duties.txt','data/nlp data/da_token_words.csv')

# get_token_words('data/de_duties.txt','data/nlp data/de_token_words.csv')
