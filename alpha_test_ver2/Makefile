CFLAGS = -g -Wall
CFLAGS += -O2

cada044: nmpgen.o
	g++ -o $@ nmpgen.o $(CFLAGS)

nmpgen.o: nmpgen.cpp
	g++ -static -c nmpgen.cpp $(CFLAGS)

clean:
	rm -f cada044 *.o
