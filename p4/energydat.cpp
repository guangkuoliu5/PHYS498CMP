#include<iostream>
#include "Net.h"
#include<stdlib.h>
#include<time.h>
#include<fstream>
using namespace std;
int main() {
	srand(time(NULL));
	Net net(100);
	ofstream outfile; outfile.open("energy.dat");
	for (int run=0; run<10; run++) {
		vector<int> in_s(net.size, 0);
		for (int &x: in_s) x=rand()%2*2-1;
		net.set_s(in_s);
		outfile<<net.getEnergy()<<" ";
		for (int sweep=0; sweep<17; sweep++) {
			for (int step=0; step<net.size; step++) {
				net.step();
			}
			outfile<<net.getEnergy()<<" ";
		}
		outfile<<endl;
	}
	outfile.close();
	return 0;
}
