#include<vector>
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
		void set_s(vector<int> & in_s);
		void step();
		double getEnergy();
};

