"""
Created at 29/11/16
__author__ = 'Sergio Padilla'

"""
from lxml import etree
from urllib import urlretrieve


class ParseRssNews:

    def __init__(self, term = None):
        self.image_count = 0
        self.news_count = 0
        self.special_term = term
        self.special_term_count = 0
        print ('---- Principio del archivo')
        
    def start(self, tag, attrib):  # Etiquetas de inicio
        print ('< %s>' % tag)
        if tag == 'item':
            self.news_count += 1

        if self.special_term and tag == self.special_term:
            self.special_term_count += 1

        for k in attrib:
            if k == 'url':
                self.image_count += 1
                print (' %s = " %s"' % (k, attrib[k]))
                urlretrieve(attrib[k], 'images/image %d.png' % self.image_count)
        
    def end(self, tag):  # Etiquetas de fin
        if tag == 'img':
            print ('</ %s>' % tag)
        
    # def data(self, data):  # texto
    #     print ('- %s-' % data)
        
    def close(self):
        print ('---- Fin del archivo')
        print ('Numero de imagenes: %d' % self.image_count)
        print ('Numero de noticias: %d' % self.news_count)
        if self.special_term:
            print ('Numero de %s: %d' % (self.special_term, self.special_term_count))


parser = etree.XMLParser(target=ParseRssNews("item"))
etree.parse('rss', parser)
