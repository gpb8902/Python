from base64 import *
print("Hello")

from bs4 import BeautilfulSoup
soup = BeautilfulSoup("<p>some<b>bad<i>HTML")
print(soup.prettify)