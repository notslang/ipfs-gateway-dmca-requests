#!/bin/sh
cat *.md | grep "ipfs.slang.cx/ipfs/" | python dmca-urls-to-nginx-blocklist.py | sort -u
