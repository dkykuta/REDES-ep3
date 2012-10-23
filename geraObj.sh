#! /bin/bash

SCRIPTAUX=./script.sh

source .Make.variables

rm -f $MAKEDEP
rm -f $MAKEOBJ

printf "OBJECTS=" > $MAKEOBJ
$SCRIPTAUX src $MAKEDEP $MAKEOBJ
