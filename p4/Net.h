#include<vector>
#include<string>
using namespace std;
class Net{
//	private:
	public:
		int size;
		vector<int> s;
		vector<double> b;
		vector<vector<double>> W;
//	public:
		Net();
		Net(int in_size);
		Net(int in_size,
			vector<int>  in_s,
			vector<vector<double>>  in_W);
		string get_str();
		void set_s(vector<int> & in_s);
		void set_W(vector<vector<double>> & in_W);
		void step();
		double getEnergy();
};

