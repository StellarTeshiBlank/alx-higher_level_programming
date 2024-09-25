#!/bin/bash
# Script that shows the Content-Length from a HTTP request
curl -s "$1" -w '%{size_download}\n' -o /dev/null
