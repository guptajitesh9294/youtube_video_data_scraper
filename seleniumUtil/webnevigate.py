# from seleniumUtil.chromdriver import drivers
import time
from seleniumUtil.get_videos1 import getAllVideoTags
import pandas as pd
import csv
class webNevigation:

    def DataSegregation(data):
        print("----------------")
        with open('output_file.csv','w',newline = '', encoding  = "utf-8") as f:
            line = csv.writer(f)
            i = 1
            line.writerow(["title","views","date_published","description","duration","tags","likes","dislikes","channel_name","channel_url","subscribers"])
            for ylink in data['url']:
                data = getAllVideoTags.getVideoTags(ylink)
                line.writerow([data["title"],data["views"],data["date_published"],data["description"],data["duration"],data["tags"],data["likes"],data["dislikes"],data["channel_name"],data["channel_url"],data["subscribers"]])
                print("{} Videos Data Saving....".format(i))
                i=i+1