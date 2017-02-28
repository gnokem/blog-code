class clist(object):
# creates a circular list object
 num_inst=0; # enforces singleton pattern

 def __init__(self,arg1=[]): # constructor
  if clist.num_inst==0: 
   clist.num_inst+=1;
   self.L=arg1;
  else: 
   print "cannot have more than one instance of class clist";
   self.__del__();

 def __del__(self): # object destructor
  pass;

 def __len__(self): # get length of clist
  return len(self.L);

 def __getitem__(self,key): # get an item of clist
  pos=key%len(self.L);
  return self.L[pos];

 def __contains__(self,key):
  if key in self.L: return True;
  return False;

 def __reversed__(self): # reverse clist contents
  self.L.reverse();
  
 def content(self): # accessor for clist contents
  return self.L;

 def redef(self,L): # reset clist contents
  self.L=L;

# sample use:
# >>> execfile("clist.py");
# >>> b=clist([1,2,3,4,'a','b','c']);
# >>> len(b)
# 7
# >>> reversed(b)
# >>> b.content();
# ['c', 'b', 'a', 4, 3, 2, 1]
# >>> b.redef([1,2,3,4,5,6,7]);
# >>> b.content();
# [1, 2, 3, 4, 5, 6, 7]
# >>> len(b);
# 7
# >>> b[1]
# 2
# >>> b.content()
# [1, 2, 3, 4, 5, 6, 7]
# >>> 'a' in b
# False
# >>> 1 in b
# True
# >>> c=clist([1,2,3]);
#
# cannot have more than one instance of class clist
# >>> b[-13]
# 2
# >>> b[13]
# 7
# >>>
