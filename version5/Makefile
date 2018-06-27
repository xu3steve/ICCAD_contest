CFLAGS = -g -Wall
CFLAGS += -O2

nmpgen: nmpgen.o
	g++ -o $@ nmpgen.o $(CFLAGS)

nmpgen.o: nmpgen.cpp
	g++ -static -c nmpgen.cpp $(CFLAGS)

clean:
	rm -f nmpgen *.o
