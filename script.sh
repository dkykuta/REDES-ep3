#! /bin/bash

source .Make.variables

if [ -d $1 ]; then
    ls $1 | xargs -I {} $0 "$1/{}"
else
    if [ "`echo $1 | rev | cut -d"." -f1 | rev`" == "cc" ]; then
        EXEC="\$(BINDIR)/`echo $1 | rev | cut -d"/" -f1 | rev | sed 's/.cc/.o/g'`"
            printf "$EXEC " >> $MAKEOBJ
            gcc -MM -MG -MT "$EXEC" $1 | sed 's/src/$(SRCDIR)/g' >>$MAKEDEP
            printf "\t" >>$MAKEDEP
            echo "\$(CC) \$(CFLAGS) -c \$(SRCDIR)/`echo $1 | cut -d"/" -f2-` -o $EXEC" >>$MAKEDEP

            echo "" >> $MAKEDEP


        echo "" >>$MAKEDEP
    fi
fi
