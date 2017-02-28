import os, sys, math;
import pickle;
from os.path import join;

def delchrs(x,chrs):
 x=x.lower().replace("'s","");
 for i in chrs: x=x.replace(i,"");
 return x;

def tf(f): # reads file f and returns dict of words from f with count
 wrds,wc=[],{};
 fh=open(f,"r");
 fc=fh.readlines();
 for i in fc: wrds+=i.replace("\n","").split(" ");
 wrds=[delchrs(i,".?,;:*\"\'()!_") for i in wrds];
 for i in wrds:
  if i not in wc: wc[i]=wrds.count(i)/float(len(wrds));
 return wc;

g=open("txtfiles.txt","w");
f=[];
for root, dirs, files in os.walk("c:\\"):
 for name in files:
  if name[-4:]==".txt" and root.find("gutenberg")>-1:  # used a corpus of project gutenberg novels to test.
   f+=[join(root,name)];
   g.write(f[-1]+"\n");
   print f[-1];
g.close();

# build tf database
tfdict={};
for i in f:
 print "processing "+i+" ...";
 tfdict[i.split("\\")[-1].split("_")[0]]=tf(i);

tfpck=open("tfpickle.pkl","wb");
pickle.dump(tfdict,tfpck);
tfpck.close();

# collect all dict key lists
all_wrds,all_dicts=[],[];
for i in tfdict: 
 all_wrds+=tfdict[i].keys();
 all_dicts+=[tfdict[i].keys()];
all_wrds=list(set(all_wrds));

idf={};
g=open("idf.txt","w");
all_docs=float(len(all_dicts));
for i in all_wrds:
 idf[i]=math.log(all_docs/sum([1 for j in all_dicts if i in j]));
 g.write(i+","+str(idf[i])+"\n");
g.close(); 

idfpck=open("idfpickle.pkl","wb");
pickle.dump(idf,idfpck);
idfpck.close();

tfpck=open("tfpickle.pkl","rb");
x=pickle.load(tfpck);
tfpck.close();

idfpck=open("idfpickle.pkl","rb");
y=pickle.load(idfpck);
idfpck.close();
