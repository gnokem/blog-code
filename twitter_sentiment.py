# twitter sentiment analysis 
# (c) Phantom Phoenix, The Medusa's Cave Blog 2012
# Description: This file performs simple sentiment analysis on global twitter feeds
#              Later versions may improve on the sentiment analysis algorithm

import os, sys, time; # import standard libraries
from twython import Twython; # import the Twitter Twython module
twitter = Twython(); # initialize it

f=open("neg.txt","r"); # open the file with keywords for sentiment analysis
fc=f.readlines(); # read it
wrds=[i.replace("\n","") for i in fc]; # save it for use
g=open("twit.txt","w"); # open the output file
g.write("@time, #tweets, sentiment index: % positive, % negative\n"); # write header to it
while True: # forever...
 search_results = twitter.searchTwitter(q=sys.argv[1], rpp="500");
 # search twitter feeds for the specified topic of interest with 
 # max results per page of 500.
 x=search_results["results"]; # grab results from search
 r=[]; # create placeholder to hold tweets
 for i in x: 
  t=i["text"];
  txt="".join([j for j in t if ord(j)<128]);
  # parse tweets and gather those not directed to particular users
  if txt.find("@")==-1: r+=[txt]; 

 neg=0; # set counter for negative tweets
 for i in r:
  for j in wrds: # check against word list, calculate how many negatives
   if i.lower().find(j)>-1:
    break;
  if j=="": 
   #print "pos,",i; # treating non-negatives as positives in this iteration
   pass;            # this may change later as we evolve to support three categories
  else: 
   #print "neg,",i;
   neg+=1;

 #print "number of negatives: ",neg;
 #print "sentiment index: positive: %5.2f%% negative: %5.2f%%" %((len(r)-neg)/float(len(r))*100,neg/float(len(r))*100);
 #print ",".join([time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),str(len(r)),str((len(r)-neg)/float(len(r))*100)[:5]+"%",str(neg/float(len(r))*100)[:5]+"%"]);
 g.write(",".join([time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),str(len(r)),str((len(r)-neg)/float(len(r))*100)[:5]+"%",str(neg/float(len(r))*100)[:5]+"%"])+"\n");
 g.flush(); # write output to file, flush it, then sync it to disk immediately.
 os.fsync(g.fileno());
 time.sleep(180); # sleep for 3 mins then try again

g.close(); # close file after forever and exit program
sys.exit(0); # these two lines never reached but kept for completeness