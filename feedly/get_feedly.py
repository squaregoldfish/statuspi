#!/usr/bin/python

# Requires python-feedly package

from feedly import client
from datetime import datetime, timedelta

USER_ID="39fdf31c-5f4d-4d0b-bb17-17cb41b77429"
ACCESS_TOKEN="A3_sWr8atp9sfNlnDMTE-r-Cnm8cRW5x-lgkziBkZ9BNLoykuVJVl3adSov13vCy8V28tNcbvU0BjUEVWirASZDNsBEbYNmO7GPUwzW6SXmXdQzClfxN402s1EmVXURl12kE8YnJU47XkCD2Mnc5mYXdZ7RJZZ1EOk1U0X5Qkxb1ygkPtavU6B3LLNlqznUBcEtI_8vf8PnApC6OVSsTzdxqLFCvmg:feedlydev"

feedly = client.FeedlyClient(sandbox=False)

sfl = feedly.get_feed_content(ACCESS_TOKEN, 'user/' + USER_ID + '/tag/global.saved', ranked="oldest", count=10000)
count = len(sfl["items"])

ms = sfl["items"][1]["crawled"]
item_time = datetime.fromtimestamp(ms/1000)

age = datetime.now() - item_time

f = open("../feedly_count.txt", "w")
f.write(str(count))
f.close()

f = open("../feedly_oldest.txt", "w")
f.write(str(age.days))
f.close()

