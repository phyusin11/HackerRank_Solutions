# Enter your code here. Read input from STDIN. Print output to STDOUT 

from html.parser import HTMLParser

class CustomHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print (tag)
        for ele in attrs:
            print(f'-> {ele[0]} > {ele[1]}')

    def handle_startendtag(self, tag, attrs):
        print (tag)
        for ele in attrs:
            print(f'-> {ele[0]} > {ele[1]}')
            
parser = CustomHTMLParser()
N = int(input())
for i in range(N):
    parser.feed(input())