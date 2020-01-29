#include<iostream>
#include<math.h>
#include<random>
#include<stdio.h>
#include<vector>
#include<string>
#include<fstream>
#define N 100
#define numSweeps 10000
using namespace std;
void print_state_cmd(const vector<vector<int>> &state) {
	cout<<"state: "<<endl;
	for (int i=0; i<N; i++) {
		for (int j=0; j<N; j++) {
			cout<<state[i][j]<<" ";
		}
		cout<<endl;
	}
}
void print_state_file(const vector<vector<int>> &state, const string &outname) {
	ofstream outfile;
	outfile.open(outname);
	for (int i=0; i<N; i++) {
		for (int j=0; j<N; j++) {
			outfile<<state[i][j]<<" ";
		}
		outfile<<endl;
	}
	outfile.close();
}
void swap_int(int &i, int&j) {
	int temp=i;
	i=j;
	j=temp;
}
void swap_state(vector<vector<int>> &state, const int &i, const int &j, const int &n) {
	//0:right, 1:down, 2:left, 3:right
	int i1, j1;
	if (n%4==0) {i1=i, j1=j+1;} 
	else if (n%4==1) {i1=i+1, j1=j;}
	else if (n%4==2) {i1=i, j1=j-1;}
	else if (n%4==3) {i1=i-1, j1=j;}
	if (i1<0 || i1>N-1 || j1<0 || j1>N-1) {
		cout<<"ERROR!!!!!!!! "<<" n:"<<n<<" ij:"<<i<<" "<<j<<" i1j1: "<<i1<<" "<<j1<<endl;
	} else {
		swap_int(state[i][j], state[i1][j1]);
	}
}

int main() {
	vector<vector<int>> state;
	//const string logname="randlog.txt";
	//ofstream logfile; logfile.open(logname); 
	// Initializing state
	state.resize(N);
	for (int i=0; i<N; i++) {
		state[i].resize(N/2,1);
		state[i].resize(N,0);
	}
	//evolution
	for (int sweep=0; sweep<=numSweeps; sweep++) {
		char outname[50];
		sprintf(outname, "data/%05d.txt", sweep);
		string outname_s=outname;
		print_state_file(state, outname_s);
		cout<<"generated: "<<outname_s<<endl;
		for (int dummy=0; dummy<N*N; dummy++) {
			random_device rd;
			mt19937 mt(rd());
			uniform_real_distribution<double> dist(0.0, (double)N);
			int i=(int)floor(dist(mt)), j=(int)floor(dist(mt));
			//logfile<<i<<" "<<j<<" ";
			/*
			if ((0<i && i<N-1) && (0<j && j<N-1)){
				uniform_real_distribution<double> dist1(0.0, 4.0);
				int n=(int)floor(dist1(mt))
				swap_state(state, i, j, n);
			} else if(
			*/
			double start=0.0, fin=4.0;
			if (i==N-1 && 0<j && j<N-1) {start=2.0; fin=5.0;}
			if (i==0 && 0<j && j<N-1) {start=0.0; fin=3.0;}
			if (0<i && i<N-1 && j==0) {start=3.0; fin=6.0;}
			if (0<i && i<N-1 && j==N-1) {start=1.0; fin=4.0;}
			if (i==0 && j==0) {start=0.0; fin=2.0;}
			if (i==0 && j==N-1) {start=1.0; fin=3.0;}
			if (i==N-1 && j==N-1) {start=2.0; fin=4.0;}
			if (i==N-1 && j==0) {start=3.0; fin=5.0;}
			uniform_real_distribution<double> dist1(start, fin);
			int n=(int)floor(dist1(mt));
			swap_state(state, i, j, n);
			/* ij=0x 012
			 * ij=Nx 234
			 * ij=x0 345
			 * ij=xN 123
			 * ij=00 01
			 * ij=0N 12
			 * ij=NN 23
			 * ij=N0 34
			 */
		}
	}
	//logfile.close();
	return 0;


}
