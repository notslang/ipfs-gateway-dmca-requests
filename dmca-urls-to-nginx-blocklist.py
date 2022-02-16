import fileinput
from urllib.parse import urlparse

for line in fileinput.input():
    line = line.strip()
    if line == '':
        continue

    url = urlparse(line)
    path = url.path.split('/')

    assert path[0] == ''
    assert path[1] == 'ipfs'

    print('location /ipfs/' + path[2] + ' { return 451; }')
