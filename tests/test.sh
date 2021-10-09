#!/bin/bash
echo $'\n'"These have a solution"$'\n'
while read -r line ; do
  python3 ../script.py $line >/tmp/res
  tail -2 /tmp/res | head -1
done < test-file
echo $'\n'"These haven't got a solution, but are 1 away"$'\n'
while read -r line ; do
  python3 ../script.py $line >/tmp/res
  tail -2 /tmp/res | head -1
done < test-one-away
