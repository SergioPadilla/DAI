"""
Created at 11/12/16
__author__ = 'Sergio Padilla'
"""
from urllib import urlretrieve
from lxml import etree

tree = etree.parse('rss')

image_count = 0
news_count = 0
special_term = 'image'  # change if you want another term
special_term_count = 0

# Root element
rss = tree.getroot()

# Los elementos funcionan como listas
# First child
# channel = rss[0]
for child in rss:
    for e in child:
        if e.tag == 'item':
            news_count += 1
            for childe in e:
                for key in childe.keys():
                    if key == 'url':
                        image_count += 1
                        urlretrieve(childe.get(key), 'images/image %d.png' % image_count)

        if special_term and e.tag == special_term:
            special_term_count += 1

    print ('Numero de imagenes: %d' % image_count)
    print ('Numero de noticias: %d' % news_count)
    if special_term:
        print ('Numero de %s: %d' % (special_term, special_term_count))
