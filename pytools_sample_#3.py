import os, sys;
from datetime import *;

def s2(x): # returns "03" if x==3, or "10" if x==10
 if x<10: return "0"+str(x); # i.e. adds leading zeroes as needed
 else: return str(x);

class dt(object):
 # creates a dt object and provides means to view it in different ways

 def __init__(self,x): # constructor
  if type(x)==str and x.count('/')==2: # covers XL and XL0 types
   m,d,y=x.split("/");
   self.m,self.d,self.y=int(m),int(d),int(y);
  if type(x)==str and x.count('-')==2: # covers DB and DB0 forms
   m,d,y=x.split("-");
   self.m,self.d,self.y=int(m),int(d),int(y);
  if type(x)==date: self.y,self.m,self.d=x.year,x.month,x.day;
   # covers the date object format
  
 def __del__(self): # destructor
  pass;

 def OBJ(self): # returns the date object
  return date(self.y,self.m,self.d);

 def TXT(self): # returns the text representation
  m,d=s2(self.m),s2(self.d);  
  return str(self.y)+m+d;

 def XL(self): # returns the Excel date type
  return "/".join([str(self.m),str(self.d),str(self.y)]);

 def XL0(self): # returns Excel date type with leading 0s
  return "/".join([s2(self.m),s2(self.d),str(self.y)]);

 def DB(self): # returns the MySQL DB date type
  return "-".join([str(self.y),str(self.m),str(self.d)]);

 def DB0(self): # returns the MySQL DB date type with LZs
  return "-".join([str(self.y),s2(self.m),s2(self.d)]);

# sample output generated as below
# >>> execfile("dt.py");
# >>> a=dt("4/10/2012");
# >>> a.OBJ();
# datetime.date(2012, 4, 10)
# >>> a.TXT();
# '20120410'
# >>> a.DB();
# '2012-4-10'
# >>> a.DB0();
# '2012-04-10'
# >>> a.XL0();
# '04/10/2012'
# >>> a=dt(date(2012,4,10));
# >>> a.OBJ()
# datetime.date(2012, 4, 10)
# >>> a.TXT()
# '20120410'
# >>> a.XL0();
# '04/10/2012'
# >>> a.XL();
# '4/10/2012'
# >>> a.DB();
# '2012-4-10'
# >>> a.DB0();
# '2012-04-10'
# >>>