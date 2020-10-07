# xml-to-pseudo-yaml

<b>Converts xml files to saltstack format</b>

```
$ ./xml-to-pseudo-yaml.py -h
usage: xml-to-pseudo-yaml.py [-h] [-l] xmlfile

XML to pseudo yaml

positional arguments:
  xmlfile        XML file

optional arguments:
  -h, --help     show this help message and exit
  -l, --as-list  convert as list

```

example input:

```
$ cat example.xml
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>

```

example output:

```
$ xml-to-pseudo-yaml.py example.xml 
note: 
  to: 'Tove'
  from: 'Jani'
  heading: 'Reminder'
  body: 'Don\'t forget me this weekend!'
```

