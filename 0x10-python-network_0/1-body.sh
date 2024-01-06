#!/bin/bash
# Bash script to displays onlybody of the response of 200 status
status=$(curl -o /dev/null -s -w "%{http_code}" "$1");
if [ "$status" -eq "200" ]
then 
	curl -LX GET "$1";
fi
