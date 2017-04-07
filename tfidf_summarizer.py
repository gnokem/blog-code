# 2nd step of the process - constructing the index
import os, sys, math;
import pickle, glob, re;
from operator import itemgetter;
from os.path import join;


# read the tf and idf objects
# tff contains the tf dictionaries for each file as index
tfpck=open("tfpickle.pkl","rb");
tff=pickle.load(tfpck);
tfpck.close();


# idfs contains the idf dictionary for each unique word in the corpus
idfpck=open("idfpickle.pkl","rb");
idfs=pickle.load(idfpck);
idfpck.close();


tfidf={};
for i in tff: 
 r={};
 for j in tff[i]: 
  r[j]=tff[i][j]*idfs[j];
 tfidf[i]=r;


def clnSentence(x):
 # keep only characters 32 to 126 after splitting
 x2=[i for i in x if ord(i)>=32 and ord(i)<=126];
 return "".join(x2).strip();


def getSentences(x): # split the story into constituent sentences
 r=[];
 f=open(x,"r");
 fc=f.read();
 fc1=fc.split("\n");
 for i in fc1: r+=[clnSentence(i)];
 return r;


x=glob.glob("*.txt");
x=[i for i in x if len(i)==36]; 
# we save stories to summarize with filenames composed of their MD5 hash
# makes it easy to locate documents to be processed, and explains "36" in check above.
g=open("summaries.txt","w");
dcts={};
for i in x:
 g.write("original story follows: \n");
 p=getSentences(i);
 for j in p: g.write(j);
 g.write("\n\n summary follows: \n");
 svals=[];
 # for each sentence, 
 #  break into words, 
 #  then compute total tfidf for each sentence... 
 #  divide each sentence tfidf by the number of words in the sentence
 #  create a dictionary with the sentence as key and average tfidf as value.
 #  sort sentences on value, pick top 30% of sentences in summary
 for j in p: 
  wrds=j.split(" ");
  line_tfidf=sum([tff[i][k] for k in wrds if k in tff[i]]);
  avg_line_tfidf=line_tfidf/float(len(wrds));
  svals+=[(j,avg_line_tfidf)];
 svals=sorted(svals, key=itemgetter(1), reverse=True); # descending sort
 svals=[j[0] for j in svals[:len(p)/3]][:-1];
 g.write(p[0]+" "); # always include first sentence for context
 for j in p[1:]: 
  if j in svals: g.write(j+" ");
 g.write("\n\n\n");


g.close();
