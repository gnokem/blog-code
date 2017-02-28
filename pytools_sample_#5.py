import os, sys;

def F(x): # this function factors a number x into its prime factors
 r=[];
 i=2;
 while x>1:
  while (x % i)==0: 
   r+=[i];
   x/=i;
  i+=1;
 return r;

print "prime factors of 100 are: ",F(100);
print "prime factors of 1024 are: ",F(1024);
print "prime factors of 1789 are: ",F(1789);
print "prime factors of 2013 are: ",F(2013);
print "prime factors of 11204243 are: ",F(11204243);
print "prime factors of 112042431 are: ",F(112042431);
print "prime factors of 1120424311 are: ",F(1120424311);

# output follows:
# prime factors of 100 are:  [2, 2, 5, 5]
# prime factors of 1024 are:  [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# prime factors of 1789 are:  [1789]
# prime factors of 2013 are:  [3, 11, 61]
# prime factors of 11204243 are:  [19, 23, 25639]

# prime factors of 112042431 are:  [3, 3, 101, 123259]
# prime factors of 1120424311 are:  [1120424311]
