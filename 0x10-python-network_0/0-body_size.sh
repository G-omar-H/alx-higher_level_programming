#!/bin/bash
# Bash script to send a URL requests and displays body size of the respond
curl -v "$1" 2>&1 | sed -En  "s/<\s*Content-Length:\s+([0-9]+)/\1/p";
