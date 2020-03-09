#include<iostream>
#include<fstream>
#include<stdlib.h>
#include<time.h>
#include<math.h>
#include<vector>
//#include "input.h"
#include"ising_utils.h"
using namespace std;
int main(){
	srand(time(NULL));
	vector<vector<int>> config;
	//ifstream params("params"); InputClass input; input.Read(params);
	//double beta=input.toDouble(input.GetVariable("beta"));
	//int Lx=input.toInteger(input.GetVariable("Lx"));
	//int Ly=input.toInteger(input.GetVariable("Ly"));
	//string outFile=(input.GetVariable("outFile"));
	int Lx=3, Ly=3;
	double beta=0.3;
	int N=Lx*Ly;
	vector<int> freq(pow(2,N), 0);
	config=fromString("-1 -1 -1\n-1 -1 1\n-1 -1 1");
	cout<<Energy(config)<<endl;
	for (int sweep=0;  sweep<5000; sweep++) {
		for (int flip=0; flip<N; flip++) {
			int i = rand()%Ly;
			int j = rand()%Lx;
			if (exp(-beta*deltaE(config, i,j))>( (double)rand()/RAND_MAX)) {
				config[i][j]=-config[i][j];
			}
		}
		if (sweep>=10) freq[toInt(config)]+=1;
	}
	ofstream outFile;
	outFile.open("3x3.out");
	for (int i=0; i<pow(2,N); i++) {
		outFile<<i<<" "<<freq[i]<<endl;
	}
	return 0;
}
