from bs4 import BeautifulSoup 
import urllib





# proxy = ""

# proxies = {"http":"http://%s" % proxy}
# url = ""
# headers={'User-agent' : 'Mozilla/5.0'}

# proxy_support = urllib2.ProxyHandler(proxies)
# opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler(debuglevel=1))
# urllib2.install_opener(opener)

# req = urllib2.Request(url, None, headers)
# html = urllib2.urlopen(req).read()




html = urllib.urlopen('https://help.instagram.com/155833707900388').read()
soup = BeautifulSoup(html, "html.parser")
print(soup.get_text())

#soup.find('div',{'id':'ctl00_PlaceHolderMain_RichHtmlField1__ControlWrapper_RichHtmlField'})
#print soup.prettify()
