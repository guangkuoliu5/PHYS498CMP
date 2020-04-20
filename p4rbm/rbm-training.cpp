#include <iostream>
#include <random>
#include <fstream>
#include <stdlib.h>
#include<time.h>
#include<math.h>
#include <Eigen/Dense>

using namespace Eigen;
using namespace std;

class RBM {
	public:
		int Nv, Nh;
		MatrixXd W;
		VectorXd v,h,a,b;
		RBM(int in_Nv, int in_Nh): Nv(in_Nv), 
					Nh(in_Nh), 
					W(Nv,Nh),
					v(Nv), 
					h(Nh), 
					a(Nv), 
					b(Nh){
		}
		int v2int() {
			int x=1;
			int ret=0;
			for(int i=Nv-1; i>=0; i--) {
				if (v(i)==1) ret+=x;
				x=x*2;
			}
			return ret;
		}
		int h2int() {
			int x=1;
			int ret=0;
			for(int i=Nh-1; i>=0; i--) {
				if (h(i)==1) ret+=x;
				x=x*2;
			}
			return ret;
		}

		double E() {
			return -v.dot(W*h)-h.dot(b)-v.dot(a);//
		}
		void sample_h() {
			for (int j=0; j<Nh; j++) {
				double r=((double) rand() / RAND_MAX);
				double mj=(v.transpose()*W)(j)+b(j);
				if (r<=(exp(mj)/(exp(mj)+exp(-mj)))) {
					h(j)=1;
				} else {
					h(j)=-1;
				}
			}
		}
		void sample_v() {
			for (int i=0; i<Nv; i++) {
				double r=((double) rand() / RAND_MAX);
				double mi=(W*h)(i)+a(i);
				if (r<=exp(mi)/(exp(mi)+exp(-mi))) {
					v(i)=1;
				} else {
					v(i)=-1;
				}
			}
		}
};

ArrayXd int2state(int n, int l) {
	int i=l-1;
	ArrayXd ret=ArrayXd::Zero(l)-1;
	while(n>0) {
		ret(i)=(n%2)*2-1;
		n/=2;
		i--;
	}
	return ret;
}



void run_hv(RBM & rbm) {
	ofstream outfile;
	ArrayXd vcount=ArrayXd::Zero((int)pow(2,rbm.Nv));
	ArrayXd hcount=ArrayXd::Zero((int)pow(2,rbm.Nh));
	ArrayXd vhcount=ArrayXd::Zero((int)pow(2,rbm.Nv+rbm.Nh));
	int ct;
	for (ct=1; ct<=100000; ct++) {
		for (int k=0; k<10; k++) {
			rbm.sample_h();
			rbm.sample_v();
		}
		int vi=rbm.v2int();
		int hi=rbm.h2int();
		vcount(vi)++;
		//hcount(hi)++;
		//vhcount(vi*(int)pow(2,rbm.Nh)+hi)++;
	}
	/*
	vcount/=ct;
	hcount/=ct;
	vhcount/=ct;
	*/
	outfile.open("pv_qc.dat");
	for (int i=0; i<vcount.size(); i++) outfile<<vcount(i)<<endl;
	outfile.close();
	/*
	outfile.open("h.dat");
	for (int i=0; i<hcount.size(); i++) outfile<<hcount(i)<<endl;
	outfile.close();
	outfile.open("vh.dat");
	for (int i=0; i<vhcount.size(); i++) outfile<<vhcount(i)<<endl;
	outfile.close();
	*/
}



int main() {
	int Nv=3, Nh=5;
	int Niter=100000;
	int Niter_deriv=100;
	double eta=0.0001;
	int k=1;
	srand(time(NULL));
	RBM rbm(Nv,Nh);
	rbm.W=ArrayXXd::Random(Nv,Nh);
	rbm.a=ArrayXd::Random(Nv);
	rbm.b=ArrayXd::Random(Nh);

	random_device rd;
	mt19937 mt(time(NULL));
	vector<int> q((int)pow(2,Nv),0);
	/*
	uniform_int_distribution<> ran_int(0,100);
	for (int i=0;i<q.size();i++) {
		q[i]=(ran_int(mt));
	}*/
	q={315, 192,   0,   0,   0,   0, 183, 310};
	discrete_distribution<> gen_v_q(q.begin(), q.end());
	//training
	for (int iter=0; iter<Niter; iter++) {
		MatrixXd deriv_W=MatrixXd::Zero(Nv, Nh);
		VectorXd deriv_a=VectorXd::Zero(Nv);
		VectorXd deriv_b=VectorXd::Zero(Nh);
		for(int iter_deriv=0; iter_deriv<Niter_deriv; iter_deriv++){
			/*RBM|data*/ {
				rbm.v=int2state(gen_v_q(mt), Nv);
				rbm.sample_h();
				deriv_W-=rbm.v*rbm.h.transpose();
				deriv_a-=rbm.v;
				deriv_b-=rbm.h;
			}
			/*RBM*/ {
				for (int ki=0; ki<k;ki++) {
					rbm.sample_v();
					rbm.sample_h();
				}
				deriv_W+=rbm.v*rbm.h.transpose();
				deriv_a+=rbm.v;
				deriv_b+=rbm.h;
			}
		}
		rbm.W-=eta/Niter_deriv*deriv_W;
		rbm.a-=eta/Niter_deriv*deriv_a;
		rbm.b-=eta/Niter_deriv*deriv_b;
	}
	//checking
	run_hv(rbm);
	ofstream outfile;
	outfile.open("qv_qc.dat");
	for (int i=0; i<q.size(); i++) outfile<<q[i]<<endl;
	outfile.close();
	return 0;
}

				







