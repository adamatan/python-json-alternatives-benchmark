#!/bin/bash

set -o xtrace
while true; do
    fswatch -1 .
    clear
    date
    make benchmark-local
    make lint
    sleep 0.1
done
