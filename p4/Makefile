CC=g++
CFLAGS=-g -Wall -std=c++11
default: main

main: main.cpp Net.h Net.cpp
	$(CC) $(CFLAGS) -o main main.cpp Net.cpp

clean:
	$(RM) -r main main.dSYM
