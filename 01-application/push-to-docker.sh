#!/bin/bash

docker build -t akonow/echost-server:1 .
docker login
docker push akonow/echost-server:1