import feedparser
newsfeed=feedparser.parse("https://timesofindia.indiatimes.com/rssfeedstopstories.cms")
print("number of rss" ,len(newsfeed.entries))
entry=newsfeed.entries[1]
print(entry.title)
print(entry.published)
print(entry.summary)
print(entry.link)