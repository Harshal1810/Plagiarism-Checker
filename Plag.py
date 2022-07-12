from functools import lru_cache
import string
from nltk.corpus import stopwords

def lev_dist(a, b):
    @lru_cache(None)  # for memorization
    def min_dist(s1, s2):

        if s1 == len(a) or s2 == len(b):
            return len(a) - s1 + len(b) - s2

        # no change required since charactrs are matching
        if a[s1] == b[s2]:
            return min_dist(s1 + 1, s2 + 1)

        return 1 + min(
            min_dist(s1, s2 + 1),      # insert character
            min_dist(s1 + 1, s2),      # delete character
            min_dist(s1 + 1, s2 + 1),  # replace character
        )

    return min_dist(0, 0)

def remove_punctuations(txt, punct = string.punctuation):
    '''
    This function will remove punctuations from the input text
    '''
    return ''.join([c for c in txt if c not in punct])
  
def remove_stopwords(txt, sw = list(stopwords.words('english'))):
    '''
    This function will remove the stopwords from the input txt
    '''
    return ' '.join([w for w in txt.split() if w.lower() not in sw])

def clean_text(txt):
    '''
    This function will clean the text being passed by removing specific line feed characters
    like '\n', '\r', and '\'
    '''
    
    txt = txt.replace('\n', '').replace('\r', '').replace('\'', '')
    txt = remove_punctuations(txt)
    txt = remove_stopwords(txt)
    return txt.lower()
  
def similarity(s1, s2):
    '''
     This function will checck for the plagiarism between two cleaned files
    '''
    
    if (len(s1)>len(s2)):
        length = len(s1)
    else: 
        length = len(s2)
    
    ans = 100 - round((lev_dist(s1,s2)/length)*100,2)
    return ans

with open('file1.txt') as f:
    s1 = f.read()
    print(s1)

with open('file2.txt') as f:
    s2 = f.read()
    print(s2)

s1=clean_text(s1)
s2=clean_text(s2)

print(s1)
print(s2)

print("These two files have",similarity(s1,s2),"% similarity")