import requests
import os
file=os.environ['S3_CNAME']
fh=open(file,"r")
websites = []
for each in fh.readlines():
    websites.append(each.strip("\n"))
print "<---------------s3 bucket security testcases--------------->"
for i in websites:
    r=requests.get(i)
    if "NoSuchBucket" in r.content:
        print "Subdomain takeover possible:"+" "+i
    elif "Generated by cloudfront" in r.content:
        print "CloudFront takeover possible:"+" "+i
    elif "ListBucketResult" in r.content:
        print "Directory Listing found:"+" "+i
    else:
        print "Access Denied:"+" "+i
fh.close()
