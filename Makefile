CFLAGS = -Wall -ansi -pedantic -g -lpthread
SRCDIR=src
BINDIR=bin
RELATORIODIR=doc

EXEC=ep1

OBJECTS = $(BINDIR)/graph.o $(BINDIR)/utils.o $(BINDIR)/main.o
CC = g++

$(EXEC): $(BINDIR) $(OBJECTS)
	$(CC) $(CFLAGS) $(OBJECTS) -o $(EXEC)


# OBJECTS

$(BINDIR)/graph.o: $(BINDIR) $(SRCDIR)/graph.cc $(SRCDIR)/graph.h $(SRCDIR)/utils.h
	$(CC) $(CFLAGS) -c $(SRCDIR)/graph.cc -o $(BINDIR)/graph.o

$(BINDIR)/main.o: $(BINDIR) $(SRCDIR)/main.cc $(SRCDIR)/utils.h
	$(CC) $(CFLAGS) -c $(SRCDIR)/main.cc -o $(BINDIR)/main.o



#
##
# Parte padrao
##
#



$(BINDIR):
	if [ ! -d $(BINDIR) ]; then mkdir $(BINDIR); fi

$(RELATORIODIR):
	if [ ! -d $(RELATORIODIR) ]; then mkdir $(RELATORIODIR); fi

pdf: $(RELATORIODIR)
	cd $(RELATORIODIR); make folderup

entrega: $(EXEC) pdf
	echo "vamos entregar entao"

.PHONY: clean
clean:
	rm -f $(BINDIR)/*
	rm -f *~
	rm -f $(SRCDIR)/*~
	rm -f $(EXEC)
	cd $(RELATORIODIR); make clean
