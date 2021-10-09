#!/bin/bash
rm facit
while read -r line ; do
  python3 script.py $line >/tmp/res
  tail -2 /tmp/res | head -1
done < test-file
