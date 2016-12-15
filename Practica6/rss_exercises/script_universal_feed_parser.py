"""
Created at 11/12/16
__author__ = 'Sergio Padilla'
"""
from urllib import urlretrieve

import feedparser

python_wiki_rss_url = "http://ep00.epimg.net/rss/elpais/portada.xml"
feed = feedparser.parse(python_wiki_rss_url)

image_count = 0

for e in feed.entries:
    if 'media_thumbnail' in e.keys():
        for image in e.media_thumbnail:
            image_count += 1
            urlretrieve(image['url'], 'images/image %d.png' % image_count)

print ('Numero de imagenes: %d' % image_count)
print ('Numero de noticias: %d' % len(feed.entries))

def get_news():
    python_wiki_rss_url = "http://ep00.epimg.net/rss/elpais/portada.xml"
    feed = feedparser.parse(python_wiki_rss_url)
    titles = []
    for entry in feed.entries:
        titles.append(entry.title)
    return titles