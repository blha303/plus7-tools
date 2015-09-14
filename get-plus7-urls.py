#!/usr/bin/env python2
import urllib2,bs4,sys
slug = sys.argv[1] if len(sys.argv) > 1 else "harrys-practice"

def add_urls(soup, urls):
    oldlen = len(urls)
    urls += ["http:" + a["href"] for a in soup.findAll('a', {'class': 'collection-title-link'}) if "episode" in a["href"] and slug in a["href"]]
    sys.stderr.write("Added " + str(len(urls) - oldlen) + " URLs\n")
    return urls, len(urls) - oldlen

def main():
    soup = bs4.BeautifulSoup(urllib2.urlopen("https://au.tv.yahoo.com/plus7/{}/".format(slug)).read(), "html.parser")
    urls = []
    #1
    urls, count = add_urls(soup, urls)
    if count == 0:
        return urls
    #2
    soup = bs4.BeautifulSoup(urllib2.urlopen("https://au.tv.yahoo.com" + soup.find('a', {'class': 'paginate'})["data-url"]).read(), "html.parser")
    urls, count = add_urls(soup, urls)
    if count == 0:
        return urls
    while count != 0:
        soup = bs4.BeautifulSoup(urllib2.urlopen("https://au.tv.yahoo.com" + soup.find('a', {'class': 'load-location'})["data-next-url"]).read(), "html.parser")
        urls, count = add_urls(soup, urls)
    return urls

print "\n".join(main())
