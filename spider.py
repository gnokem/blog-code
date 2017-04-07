import os, sys, urllib2, re; 


u=sys.argv[1]; # the url to start with
lynx=[u]; # store the start url into the download set
for u in lynx: #process each link in turn
 r=urllib2.urlopen(u); # get the requested object
 x=r.read(); # read the document from the website
 xlines=x.split(" "); # split and process the lines
 c=[i for i in xlines if i.lower().find("http://")>-1]; # collect all hyperlinks
 for i in c: # process each hyperlink, ignoring some words
  if i.find("CALLOUT|")>-1: continue;
  stpos=i.index("http://");
  if i.find(".html")==-1: continue;
  if i.find("\n")>-1: continue;
  enpos=[]; # code segment that follows parses the retrieved document
  enpos+=[k.start() for k in re.finditer(".html",i)];
  #print stpos,enpos;
  enpos=[j for j in enpos if j>stpos+13];
  if len(enpos)==0: continue;
  enpos=min(enpos);
  candidate=i[stpos:enpos]+".html"; # store retrieved urls
  if candidate not in lynx: lynx+=[candidate];
 if len(lynx)>100: break; # hobble the spider so it doesn't go haywire


g=open("t.txt","w"); # write crawled urls to file
for i in lynx: g.write(i+"\n");
g.close();
