class node(object): # the class that creates every node object
 allNodes=[]; # static class variable to store all nodes created

 def __init__(self,val=-1): # constructor that creates node with specified tag
  self.val=val;
  self.parent=[];
  self.child=[];
  node.allNodes+=[self];

 def getVal(self): # accessor function that returns the tag value of a node
  return self.val;

 def addChild(self,n): # mutator function that connects a node to a child
  if self.getVal()!=n.getVal():
   self.child+=[n];

 def addParent(self,n): # mutator function that connects a node to a parent
  self.parent+=[n];

 def getChildren(self): # returns a list of child nodes for a node
  return self.child;

 def getChildVals(self): # returns a list of child node values for a node
  t=self.getChildren();
  r=[i.getVal() for i in t];
  return r;

 def getChildByVal(self,val): # returns a particular child node of a node by value
  p=self.getChildren();
  q=self.getChildVals();
  if val not in q: return None;
  else: return p[q.index(val)];

# Example usage

a=node(2);
b=node(3);
c=node(4);
d=node(5);
e=node(6);
f=node(7);
g=node(8);

a.addChild(b);
a.addChild(c);
b.addChild(g);
c.addChild(d);
c.addChild(e);
e.addChild(f);

b.addParent(a);
c.addParent(a);
d.addParent(c);
e.addParent(c);
f.addParent(e);
g.addParent(b);


def getDFSChain(n): # get the depth first search chain of nodes and values
 if type(n)!=node: return -1;
 r=[n];
 c=n;
 for i in r: r+=i.getChildren();
 for i in r: print i.getVal(),;

getDFSChain(a);

# output follows:
# 2 3 4 8 5 6 7