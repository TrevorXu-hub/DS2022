#!/bin/bash


curl -O https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz
tar -xzf lab3-bundle.tar.gz
awk '!/^[[:space:]]*$/' lab3-bundle.tsv > lab4bundle.tsv
awk 'BEGIN { FS="\t"; OFS="," } {$1=$1; print}' lab4-bundle.tsv > lab4-bundle.csv
lines=$(($(wc -l < lab4-bundle.csv)-1))
echo "$lines"
tar -czf converted-archive.ta.gz lab4-bundle.csv

