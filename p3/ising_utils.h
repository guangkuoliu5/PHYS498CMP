#include<vector>
#include<iostream>
#include<sstream>
#include<string>
using namespace std;
//Computing energy. Time complexity: O(N)
double Energy(vector<vector<int>> &config){
	double J=1;
	int w=config[0].size();
	int h=config.size();
	double energy=0;
	for (int i=0; i<h; i++) {
		for (int j=0; j<w; j++) {
			int cur=config[i][j];
			int left=config[i][(j-1+w) % w];
			int top=config[(i-1+h) %h][j];
			energy-=J*left*cur;
			energy-=J*top*cur;
		}
	}
	return energy;
}
//Computing energy difference by flipping a spin. Time complexity: O(1)
double deltaE(vector<vector<int>> &config, int i, int j){
	int w=config[0].size();
	int h=config.size();
	int cur= config[i][j];
	double dE=0;
	for (int di: {-1,1}){
		int ud=config[(i+di+h)%h][j];
		int lr=config[i][(j+di+w)%w];
		dE+=2*cur*ud;
		dE+=2*cur*lr;
	}
	return dE;
}
vector<vector<int>>  fromString(string str) {
	vector<vector<int>> config;
	stringstream ss(str);
	string line;
	while(getline(ss,line,'\n')) {
		stringstream ss1(line);
		string word;
		config.push_back({});
		while(getline(ss1,word,' ')) {
			config[config.size()-1].push_back(stoi(word));
		}
	}
	return config;
}


string toString(vector<vector<int>> &config) {
	string ret="";
	int h=config.size();
	for (int i=0; i<h; i++) {
		int w=config[i].size();
		for (int j=0; j<w; j++) {
			ret+=to_string(config[i][j])+" ";
		}
		ret+="\n";
	}
	return ret;
}
int toInt(vector<vector<int>> &config) {
	string bi="";
	int h=config.size();
	for (int i=0; i<h; i++) {
		int w=config[i].size();
		for (int j=0; j<w; j++) {
			if (config[i][j]==-1) {
				bi+="0";
			} else {
				bi+="1";
			}
		}
	}
	cout<<bi<<endl;
	return stoi(bi,0,2);
}
