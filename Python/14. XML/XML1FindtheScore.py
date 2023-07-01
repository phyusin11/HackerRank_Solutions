import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    val =0
    # your code goes here
    for child in node.iter():
        #print(child)
        #print(child.attrib)
        val += len(child.attrib)
    return val

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))