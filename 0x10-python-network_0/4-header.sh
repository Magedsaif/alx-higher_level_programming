#!/bin/bash
#  a Bash script that sends a GET request to the URL passed as the first argument and displays the body of the response
curl -sL -X GET "$1" -H "X-School-User-Id: 98"
