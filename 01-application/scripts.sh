#!/bin/bash

# get_ip_regex() {
#     ip addr show scope global | sed -n 's/.*inet \([0-9]\{1,3\}\(\.[0-9]\{1,3\}\)\{3\}\)\/.*/\1/p' | head -1
# }
get_ip_awk() {
    ip addr show scope global | grep inet | head -1 | awk '{ print $2 }' | awk -F / '{ print $1 }'
}
# function: Get the hostname of the container
get_hostname() {
    hostnamectl | grep "Static hostname:" | awk '{ print $3 }'
}

docker run \
    -e SERVER_HOSTNAME=$(get_hostname) \
    -e SERVER_IP=$(get_ip_awk) \
    -p 8000:8000 \
    echost-server:1

