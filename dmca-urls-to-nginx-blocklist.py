import fileinput
import sys
from urllib.parse import urlparse

for line in fileinput.input():
    line = line.strip()
    if line == '':
        continue

    url = urlparse(line)
    path = url.path.split('/')

    try:
        assert path[0] == ''
        assert path[1] == 'ipfs'
        assert path[2] != ''
    except:
        print("unable to parse: " + line, file=sys.stderr)

    print('location /ipfs/' + path[2] + ' { return 451; }')
