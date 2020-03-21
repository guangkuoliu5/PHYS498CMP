#include<iostream>
#include<fstream>
#include<stdlib.h>
#include<time.h>
#include<math.h>
#include<vector>
#include "input.h"
#include"ising_utils.h"
using namespace std;
int main(){
	srand(time(NULL));
	ifstream params("params"); InputClass input; input.Read(params);
	double beta=input.toDouble(input.GetVariable("beta"));
	int Lx=input.toInteger(input.GetVariable("Lx"));
	int Ly=input.toInteger(input.GetVariable("Ly"));
	string outFileName=(input.GetVariable("outFile"));
	ofstream outFile;
	outFile.open(outFileName);
	//int Lx=3, Ly=3;
	//double beta=0.3;
	int N=Lx*Ly;
	//vector<int> freq(pow(2,N), 0);
	vector<vector<int>> config(Ly, vector<int>(Lx,-1));
	//config=fromString("-1 -1 -1\n-1 -1 1\n-1 -1 1");
	for (int sweep=0;  sweep<5000; sweep++) {
		if (sweep>=0) {
			//outFile<<Energy(config)/N<<" "<<Mag2(config)/pow(N,2)<<endl;
			//vector<vector<int>> config_cg=cg(config);
			//int N_cg=N/9;
			outFile<<Energy(config)/N<<" "<<Mag2(config)/pow(N,2)<<endl;
		}
		for (int flip=0; flip<N; flip++) {
			int i = rand()%Ly;
			int j = rand()%Lx;
			if (exp(-beta*deltaE(config, i,j))>( (double)rand()/RAND_MAX)) {
				config[i][j]=-config[i][j];
			}
		}
		//if (sweep>=10) freq[toInt(config)]+=1;
	}
	outFile.close();
/*
	ofstream outSnapshot; outSnapshot.open("81data/snapshot_"+to_string(beta));
	outSnapshot<<toString(config);
	outSnapshot.close();
	vector<vector<int>> config_cg=cg(config);
	vector<vector<int>> config_cgcg=cg(config_cg);
	ofstream outSnapshot_cg; outSnapshot_cg.open("81data_cg/snapshot_"+to_string(beta));
	outSnapshot_cg<<toString(config_cg);
	outSnapshot_cg.close();

	ofstream outSnapshot_cgcg; outSnapshot_cgcg.open("81data_cgcg/snapshot_"+to_string(beta));
	outSnapshot_cgcg<<toString(config_cgcg);
	outSnapshot_cgcg.close();
	*/
	/*
	ofstream outFile;
	outFile.open(outFileName);
	for (int i=0; i<pow(2,N); i++) {
		outFile<<i<<" "<<freq[i]<<endl;
	}*/
	return 0;
}

