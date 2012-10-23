CFLAGS = -Wall -ansi -pedantic -g -pthread -lpthread -D_GNU_SOURCE
SRCDIR=src
BINDIR=bin
RELATORIODIR=doc

EXEC=ep2

EXEC_CLIENT=$(EXEC)_client
EXEC_SERVER=$(EXEC)_server

FOLDERENTREGA=$(EXEC)-diogo-e-fernando
PACOTENAME=$(FOLDERENTREGA).tar.gz

CC = g++

include Make.objects

$(EXEC): $(EXEC_CLIENT) $(EXEC_SERVER)

$(EXEC_CLIENT): $(BINDIR) $(OBJECTS) $(BINDIR)/main_client.o
	$(CC) $(CFLAGS) $(OBJECTS) $(BINDIR)/main_client.o -o $(EXEC_CLIENT)

$(EXEC_SERVER): $(BINDIR) $(OBJECTS) $(BINDIR)/main_server.o
	$(CC) $(CFLAGS) $(OBJECTS) $(BINDIR)/main_server.o -o $(EXEC_SERVER)

# OBJECTS

include Make.dependencies


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

deps:
	./geraObj.sh

entrega: clean $(EXEC) pdf
	rm -f $(PACOTENAME)
	rm -rf $(FOLDERENTREGA)
	mkdir $(FOLDERENTREGA)
	cp -r src $(FOLDERENTREGA)
	cp README $(FOLDERENTREGA)
	cp relatorio.pdf $(FOLDERENTREGA)
	cp Makefile $(FOLDERENTREGA)
	cp Make.dependencies $(FOLDERENTREGA)
	cp Make.objects $(FOLDERENTREGA)
	tar -czf $(PACOTENAME) $(FOLDERENTREGA)
	rm -rf $(FOLDERENTREGA)
	echo "Vamos entregar entao"

.PHONY: clean
clean:
	rm -f $(BINDIR)/*
	rm -f *~
	rm -f $(SRCDIR)/*~
	rm -f $(EXEC_CLIENT)
	rm -f $(EXEC_SERVER)
	rm -f $(PACOTENAME)
	cd $(RELATORIODIR); make clean
