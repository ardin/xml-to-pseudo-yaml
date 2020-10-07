#!/usr/bin/python

""" 
xml to pseudo yaml (convert xml to saltstack format)
"""

import xml.etree.ElementTree as ET
import argparse
import sys

indent = 0
ignoreElems = ['']
args = argparse.ArgumentParser

def printRecur(root):
    if root.tag in ignoreElems:
        return

    name_raw = root.attrib.get('name', root.text)
    if name_raw is None:
        name = ''
    else:
        name = '' if name_raw.strip() == '' else '\'' + name_raw.strip().replace('\'','\\\'') + '\''

    global indent
    if args.as_list == True:
      print(' ' *indent + '- %s: %s' % (root.tag.title().lower(), name))
    else:
      print(' ' *indent + '%s: %s' % (root.tag.title().lower(), name))
    indent += 2
    for elem in list(root):
        printRecur(elem)
    indent -= 2


def main(arguments):
    global args
    parser = argparse.ArgumentParser(description='XML to pseudo yaml')
    parser.add_argument('xmlfile', help='XML file ')
    parser.add_argument('-l', '--as-list', action='store_true', help='convert as list', required=False)
    args = parser.parse_args()
    try:
        tree = ET.parse(args.xmlfile)
    except Exception as e:
        sys.exit(e)

    root = tree.getroot()
    printRecur(root)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

