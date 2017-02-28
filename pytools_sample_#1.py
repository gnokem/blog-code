import os, sys;
from datetime import *;

import os, sys;
from datetime import *;

def dtConv(x,s="OBJ"): # converts dates from one form to another
 def s2(n): # nested helper function. returns str form of n if >10 else "0"+str(n)
  if n<10: return "0"+str(n);
  return str(n);

 # first, parse the input depending on type, collecting year, month, day as int
 # styles (s) supported: 
 # s="OBJ" return type is a date object. the default return type
 # s="TXT" return type is of the form "yyyymmdd" e.g. "20120131"
 # s="XL"  return type is of the form "m/d/yyyy" e.g. "2/3/2012"
 # s="XL0" return type is of the form "mm/dd/yyyy" e.g. "02/03/2012"
 # s="DB"  return type is of the form "yyyy-m-d" e.g. "2012-2-3"
 # s="DB0" return type is of the form "yyyy-mm-dd" e.g. "2012-02-03"
 if type(x)==date: y,m,d=x.year,x.month,x.day;
 else: 
  if x.count("/")==2: y,m,d=int(x.split("/")[2]),int(x.split("/")[0]),int(x.split("/")[1]);
  if x.count("-")==2: y,m,d=int(x.split("/")[0]),int(x.split("/")[1]),int(x.split("/")[2]);
  if x.count("/")==0 and x.count("-")==0 and len(x)==8: y,m,d=int(x[:4]),int(x[4:6]),int(x[6:]);
  
 # next, we generate output in the form requested
 if s=="OBJ": return date(y,m,d);
 if s=="XL": return "/".join([str(m),str(d),str(y)]);
 if s=="DB": return "-".join([str(y),str(m),str(d)]);
 if s=="XL0": return "/".join([s2(m),s2(d),s2(y)]);
 if s=="DB0": return "-".join([s2(y),s2(m),s2(d)]);
 if s=="TXT": return s2(y)+s2(m)+s2(d);
 return -1;



#Examples of use:
#dtConv("1/2/2012") gives datetime.date(2012,1,2)
#dtConv("1/2/2012","DB0") gives "2012-01-02"
#dtConv("1/2/2012","TXT") gives "20120102"
#dtConv("20120102") gives datetime.date(2012,1,2)
