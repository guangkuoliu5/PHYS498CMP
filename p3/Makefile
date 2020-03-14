CC=g++
CFLAGS=-g -Wall -std=c++11
default: main

main: main.cpp ising_utils.h input.h
	$(CC) $(CFLAGS) -o main main.cpp

clean:
	$(RM) -r main main.dSYM
