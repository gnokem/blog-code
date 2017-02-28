# 2nd step of the process - constructing the index
import os, sys, math;
import pickle;
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

g=open("imp-words.txt","w");
# print 
dcts={};
for i in tff:
 dct={};
 x=tfidf[i].values();
 y=tfidf[i].keys();
 for j in zip(x,y): 
  if j[0] in dct: dct[j[0]]+=[j[1]];
  else: dct[j[0]]=[j[1]];
 x=list(set(x));
 x.sort();
 x.reverse();
 g.write("=> "+i+"\n");
 #print "=> ",i;
 for j in x[:25]:
  #print "   ",j,dct[j];
  g.write("    "+str(round(j,3))+" "+str(dct[j])+"\n");
 dcts[i]=dct;
g.close();