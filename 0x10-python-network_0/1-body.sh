#!/bin/bash
# Bash script to displays onlybody of the response of 200 status
if [ $(($(curl -o /dev/null -L -s -w "%{http_code}" "$1"))) -eq 200 ]; then curl  -LX GET "$1"; fi
