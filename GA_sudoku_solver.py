import os, sys, operator;
from itertools import *;
from random import *;

def getCol(x,n): # get column n from grid x
 r=[];
 r+=[i[n] for i in x];
 return r;

def mkInt(c): # convert all numbers into ints in a list
 r=[];
 for i in c: r+=[[int(j) if j!='x' else j for j in i]];
 return r;

def genConstraints(x):
 # collect the constraints now
 constraints=[i for i in x]; # horizontal constraints
 for i in range(9): constraints+=[getCol(x,i)]; # vertical constraints
 # finally, the block constraints
 b=[[0,1,2],[3,4,5],[6,7,8]];
 for i in product([0,1,2],repeat=2):
  p,q=i;
  #print "p,q => ",p,q;
  c=[];
  for i in b[p]:
   t=[];
   for j in b[q]: t+=[x[i][j]];
   #print t;
   c+=t;
  constraints+=[c];
 # now we have all 27 constraints: 9 horizontal, 9 vertical, 9 block
 return mkInt(constraints);

def mkGrid(s): # convert a puzzle string to a grid
 r=[];
 for i in range(9): r+=[s.split(",")[i*9:(i+1)*9]];
 return r;

def grabDigit(x): # get a random digit from a list of digits
 shuffle(x);
 return x[0];

def genChr(x): # generate a chromosome
 r=[];
 for j in range(9):
  nums=[int(k) for k in x[j] if k!='x'];
  missing_nums=list(set(range(1,10)).difference(set(nums)));
  t=[];
  for i in range(9): 
   if x[j][i]!='x': t+=[int(x[j][i])]
   else:
    m=list(set(fx[(j,i)]).intersection(set(missing_nums)));
    if len(m)==0: m=fx[(j,i)];
    a=grabDigit(m); 
    t+=[a];
    if a in missing_nums: missing_nums.remove(a);
  r+=[t];
 return r;

def validChr(x): # is it a valid chromosome? not used for efficiency
 #for i in range(9): 
 # p=getCol(x,i);
 # if sum(p)!=45: return False;
 # if list(set(p))!=9: return False;
 return True;

def scoreChr(x): # score the chromosome
 t=genConstraints(x);
 score=0;
 for i in t: 
  if len(list(set(i)))==9: score+=1;
  #if sum(i)==45: score+=1;
 return score;
  
def printGrid(x): # print the grid 
 for i in x: 
   print " ".join(map(str,i));
 return;

def xover(a,b): # cross-over two chromosomes, get two descendants
 splice_loc=randint(1,7);
 ta=a[:splice_loc]+b[splice_loc:];
 tb=b[:splice_loc]+a[splice_loc:];
 return (ta,tb);

def xover2(a,b): # another method for cross-over
 speed=randint(1,6);
 ta,tb=a[:],b[:];
 for j in range(speed):
  x_loc=randint(1,7);
  t=ta[x_loc]; 
  ta[x_loc]=tb[x_loc];
  tb[x_loc]=t;
 return (ta,tb);

def mutate(a): # mutation
 speed=randint(1,6); # how many mutations in one go
 for i in range(speed):
  gene_seg=randint(0,8); # which gene segment to change
  x=genChr(g);
  a[gene_seg]=x[gene_seg];
 return a;   

p=open("s4.txt","r"); # open the puzzle file
pc=p.readlines(); # read it
pc=[i.replace("\n","") for i in pc];
pstr=",".join([i for i in pc]);
g=mkGrid(pstr);
mx=genConstraints(g);

# collect all the constraints by cell... 
# find which numbers might fit in each cell. use it for
b=[[0,1,2],[3,4,5],[6,7,8]];
cx,fx={},{};
for i in range(0,9):
 for j in range(0,9):
  for k in range(0,3):
   if i in b[k]: x=k;
   if j in b[k]: y=k;
   block_id=x*3+y;
   cx[(i,j)]=(i,9+j,18+block_id);
   fx[(i,j)]=list(set(range(1,10)).difference(set(mx[i]).union(set(mx[9+j])).union(set(mx[18+block_id]))));
# now fx is a dict that contains all possible values for each empty cell
t=fx.values();
for i in range(len(t)):
 if len(t[i])==1: 
  posx,posy=fx.keys()[i];
  if g[posx][posy]=='x': g[posx][posy]=t[i][0];

# all constraint strings must have all digits from 1 to 9 just once
# all constraint strings must add up to 9*10/2=45 
poolsz=5000; # size of gene pool
gene_pool=[];
while len(gene_pool)!=poolsz: # generate chromosomes to fill pool
 seed();
 t=genChr(g);
 while not validChr(t): t=genChr(g);
 if t not in gene_pool: gene_pool+=[t];

seen=gene_pool[:]; # keeps track of all seen chromosomes

# set the parameters for new generations
retain_pct=0.05;
mutate_pct=0.35;
xover_pct=0.55;
new_dna=1-retain_pct-mutate_pct-xover_pct;
generation,solved=0,0;
scores=[]; # store best scores in each generation

# solve the puzzle
while solved==0:
 genes=[];
 for i in gene_pool: genes+=[(i,scoreChr(i))];
 genes=sorted(genes,key=operator.itemgetter(1),reverse=True);
 if genes[0][1]==27: 
  print "puzzle solved";
  printGrid(genes[0][0]);
  solved=1;
 else:
  if len(scores)>3 and len(list(set(scores[-3:])))==1: 
   seed(); 
   jumpahead(randint(1,100000));
   poolsz=randint(poolsz,poolsz+500);
   retain_pct=0.1;
   mutate_pct=round(uniform(0.25,0.3),2);
   xover_pct=0.95-mutate_pct;
   new_dna=1-retain_pct-mutate_pct-xover_pct;
  print "generation: ",generation,"pool size: ",len(genes)," max score: ",genes[0][1];
  #printGrid(genes[0][0]);
  scores+=[genes[0][1]];
  generation+=1;
  seed();
  chr_retained=int(poolsz*retain_pct);
  new_pool=[j[0] for j in genes[:chr_retained]]; # 250 genes to retain
  for k in range(int(xover_pct*poolsz/2.)): # generate 450 cross-over genes
   seed();
   a,b=new_pool[randint(0,len(new_pool)-1)][:],new_pool[randint(0,len(new_pool)-1)][:];
   toss=randint(0,1);
   if toss==0: ta,tb=xover(a,b);
   else: ta,tb=xover2(a,b);
   if ta not in seen: new_pool+=[ta];
   if tb not in seen: new_pool+=[tb];
  for k in range(int(mutate_pct*poolsz)): # generate 150 mutated genes
   seed();
   a=new_pool[randint(0,len(new_pool)-1)][:];
   ta=mutate(a);
   if ta not in seen: new_pool+=[ta];
  while len(new_pool)<poolsz: # new genetic material
   seed();
   ta=genChr(g);
   if ta not in seen: new_pool+=[ta];
  gene_pool=new_pool[:];
  seen+=gene_pool[:];

sys.exit(0);
