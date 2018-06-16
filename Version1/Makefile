CFLAGS = -g -Wall

nmpgen: nmpgen.o
	g++ -o $@ nmpgen.o $(CFLAGS)

nmpgen.o: nmpgen.cpp
	g++ -c nmpgen.cpp $(CFLAGS)

clean:
	rm -f nmpgen *.o
