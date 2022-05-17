import requests
import lxml.html
from lxml import etree
# html = ''' <html>
#  <head> <title> Some title </title> </head>
#  <body>
#   <tag1> some text
#      <tag2> MY TEXT </tag2>
#    </tag1>
#  </body>
# </html>
# '''
tree = etree.parse('18.4.4.html', lxml.html.HTMLParser())
#tree = lxml.html.document_fromstring(html)

text = tree.xpath('/html/body/tag1/tag2/text()')

print(text)