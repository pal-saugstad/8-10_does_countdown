#!/bin/bash

function do_test {
  echo $'\n'"$2 (result should be $3 away). Trying same input again if more that $3 away"$'\n'
  while read -r line ; do
    while : ; do
      failed=''
      python3 ../script.py $line >/tmp/res
      show=$(tail -2 /tmp/res | head -1)
      if [ $3 -eq 0 ] ; then
        [ "$(echo "$show" | grep 'away')" ] && failed=' FAILED '
      else
        want=$(echo $show | grep " $3 away")
        [ "$want" ] || failed=' FAILED '
      fi
      printf "%-25s|%s%s\n" "$line" "$failed" "$show"
      [ "$failed" ] || break
    done
  done < $1
}

do_test test-file "These have a solution" 0
do_test test-one-away "These haven't got a solution" 1
