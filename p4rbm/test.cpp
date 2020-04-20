#include <iostream>
#include <stdlib.h>
#include<time.h>
#include<math.h>
#include <Eigen/Dense>

using namespace Eigen;
using namespace std;
using std::round;

int main() {
	srand(time(NULL));
	MatrixXd m=2*round((1+ArrayXXd::Random(3,4))/2)-1;
	VectorXd v=ArrayXd::Random(3);
	cout<<v<<endl<<endl;
	return 0;
}

