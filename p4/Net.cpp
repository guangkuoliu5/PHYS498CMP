#include "Net.h"
#include<stdlib.h>
#include<time.h>
#include<iostream>
using namespace std;
Net::Net(int in_size): size(in_size),s(size, 0), b(size,0), W(size,vector<double>(size,0)) {
	srand(time(NULL));
	for (int i=0; i<size; i++) {
		s[i]=rand()%2*2-1;
		b[i]=((double)rand()/RAND_MAX)*2-1;
		for (int j=0; j<=i; j++) {
			W[i][j]=((double)rand()/RAND_MAX)*2-1;
			W[j][i]=W[i][j];
		}
	}
}
Net::Net(int in_size,
	       	vector<int>  in_s, 
		vector<vector<double>>  in_W): 
	size(in_size),
	s(in_s), b(size,0), W(in_W) {
}

Net::Net(): Net(10) {
}
	
string Net::get_str() {
	string ret(s.size(), '0');
	for (int i=0; i<s.size(); i++) {
		if (s[i]==1) ret[i]='1';
	}
	return ret;
}
void Net::set_s(vector<int> & in_s) {
	s=in_s;
}
void Net::set_W(vector<vector<double>> & in_W) {
	W=in_W;
}
void Net::step() {
	//srand(time(NULL));
	int i=rand()%size;
	double T=0;
	for(int j=0; j<size; j++) {
		if (i==j) continue;
		T+=s[j]*W[i][j];
	}
	if (T>b[i]) s[i]=1; else s[i]=-1;
	//cout<<endl<<i<<" "<<T<<" "<<b[i]<<endl;
}
double Net::getEnergy() {
	double ret=0;
	for (int i=0; i<size; i++) {
		ret+=b[i]*s[i];
		ret-=W[i][i]*s[i]*s[i]/2;
		for (int j=0; j<i; j++) {
			ret-=W[i][j]*s[i]*s[j];
		}
	}
	return ret;
}

			

