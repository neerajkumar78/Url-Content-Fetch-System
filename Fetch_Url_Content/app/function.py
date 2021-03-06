from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)

def get_content(url):
    try:
        webUrl = urllib.request.urlopen(url)
        if(webUrl.getcode()==200):
            data=text_from_html(webUrl)
            return data
        else:
            return None
    except Exception:
        return None

