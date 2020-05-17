import requests
from bs4 import BeautifulSoup
import json

soup=BeautifulSoup(open("youtubeinfluencers.html"),"lxml")

outfile=open('top_5000_youtube_influencers.json',"a")
for row in soup.findAll("div",attrs={"style":"width: 860px; background: #f8f8f8;; padding: 0px 20px; color:#444; font-size: 10pt; border-bottom: 1px solid #eee; line-height: 30px;"}):
    details=dict()
    item = row.findAll("div")
    details['rank'] = item[0].text
    details['grade'] = item[1].text
    details['username'] = item[2].text
    details['uploads'] = item[3].text
    details['subscribers'] = item[4].text
    details['top_views'] = item[5].text
    json.dump(details,outfile)
    outfile.write(",\n")

for row in soup.findAll("div",attrs={"style":"width: 860px; background: #fafafa; padding: 10px 20px; color:#444; font-size: 10pt; border-bottom: 1px solid #eee; line-height: 40px;"}):
    details=dict()
    item = row.findAll("div")
    details['rank'] = item[0].text
    details['grade'] = item[1].text
    details['username'] = item[2].text
    details['uploads'] = item[3].text
    details['subscribers'] = item[4].text
    details['top_views'] = item[5].text
    json.dump(details,outfile)
    outfile.write(",\n") 

for row in soup.findAll("div",attrs={"style":"width: 860px; background: #fafafa; padding: 0px 20px; color:#444; font-size: 10pt; border-bottom: 1px solid #eee; line-height: 30px;"}):
    details=dict()
    item = row.findAll("div")
    details['rank'] = item[0].text
    details['grade'] = item[1].text
    details['username'] = item[2].text
    details['uploads'] = item[3].text
    details['subscribers'] = item[4].text
    details['top_views'] = item[5].text
    json.dump(details,outfile)
    outfile.write(",\n") 

for row in soup.findAll("div",attrs={"style":"width: 860px; background: #f8f8f8;; padding: 10px 20px; color:#444; font-size: 10pt; border-bottom: 1px solid #eee; line-height: 40px;"}):
    details=dict()
    item = row.findAll("div")
    details['rank'] = item[0].text
    details['grade'] = item[1].text
    details['username'] = item[2].text
    details['uploads'] = item[3].text
    details['subscribers'] = item[4].text
    details['top_views'] = item[5].text
    json.dump(details,outfile)
    outfile.write(",\n") 

outfile.close()

    