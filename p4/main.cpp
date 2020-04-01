#include<iostream>
#include "Net.h"
#include<stdlib.h>
#include<time.h>
#include<fstream>
#include<string>
using namespace std;
vector<int> str_to_s(string & str) {
	vector<int> ret(str.length(), -1);
	for (int i=0; i<str.length(); i++) {
		if (str[i]=='1') ret[i]=1;
	}
	return ret;
}
vector<vector<double>> str_to_w(vector<string>  strvec) {
	int m=strvec.size();
	vector<vector<double>> ret(strvec[0].length(), vector<double>(strvec[0].length(), 0));
	for (string & str: strvec) {
		for (size_t i=0; i<str.length(); i++) {
			for (size_t j=0; j<str.length(); j++) {
				ret[i][j]+=((str[i]-'0')*2-1)*((str[j]-'0')*2-1)*1.0/m;
			}
		}
	}
	return ret;

}
int main() {
	string face="0000000000000100010000000000000000000000000010000000000000000001110000001000100001000001101000000001";
	string tree="0001111000000111100000001100000000110000001111111000001100100000110000000011000000001100000000110000";
	string halfface=face;
	for (int i=0; i<100; i++) {
		if (i%10<5) halfface[i]='0';
	}

	Net net((int)face.length(), str_to_s(halfface), str_to_w(vector<string>{face, tree}));
	cout<<net.get_str()<<endl;
	for (int sweep=0; sweep<1; sweep++) {
		for (int step=0; step<net.size; step++) {
			net.step();
			cout<<net.get_str()<<endl;
		}
	}
	cout<<net.get_str()<<endl;
	return 0;
}
