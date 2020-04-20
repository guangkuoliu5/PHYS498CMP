#include <iostream>
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



void run_h(RBM & rbm) {
	ofstream outfile; outfile.open("hcondv.dat");
	ArrayXd probs=ArrayXd::Zero((int)pow(2,rbm.Nh));
	int ct;
	for (ct=1; ct<=100000; ct++) {
		rbm.sample_h();
		probs(rbm.h2int())++;
	}
	probs=probs/ct;
	for (int i=0; i<(int)pow(2,rbm.Nh);i++) {
		outfile<<probs(i)<<endl;
	}
	//cout<<probs<<endl<<endl;
	//cout<<rbm.v<<endl<<endl;
	outfile.close();
}
void al_hcondv(RBM & rbm) {
	ofstream outfile; outfile.open("al_hcondv.dat");
	int totalh=(int)pow(2,rbm.Nh);
	ArrayXd probs(totalh);
	for (int i=0; i<totalh; i++) {
		rbm.h=int2state(i,rbm.Nh);
		probs(i)=exp(-rbm.E());
	}
	probs=probs/probs.sum();
	for (int i=0; i<totalh;i++) {
		outfile<<probs(i)<<endl;
	}
	//cout<<probs<<endl<<endl;
	//cout<<rbm.v<<endl<<endl;
	outfile.close();
}
void run_v(RBM & rbm) {
	ofstream outfile; outfile.open("vcondh.dat");
	ArrayXd probs=ArrayXd::Zero((int)pow(2,rbm.Nv));
	int ct;
	for (ct=1; ct<=100000; ct++) {
		rbm.sample_v();
		probs(rbm.v2int())++;
	}
	probs=probs/ct;
	for (int i=0; i<(int)pow(2,rbm.Nv);i++) {
		outfile<<probs(i)<<endl;
	}
	//cout<<probs<<endl<<endl;
	//cout<<rbm.v<<endl<<endl;
	outfile.close();
}
void al_vcondh(RBM & rbm) {
	ofstream outfile; outfile.open("al_vcondh.dat");
	int totalv=(int)pow(2,rbm.Nv);
	ArrayXd probs(totalv);
	for (int i=0; i<totalv; i++) {
		rbm.v=int2state(i,rbm.Nv);
		probs(i)=exp(-rbm.E());
	}
	probs=probs/probs.sum();
	for (int i=0; i<totalv;i++) {
		outfile<<probs(i)<<endl;
	}
	//cout<<probs<<endl<<endl;
	//cout<<rbm.v<<endl<<endl;
	outfile.close();
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
		hcount(hi)++;
		vhcount(vi*(int)pow(2,rbm.Nh)+hi)++;
	}
	vcount/=ct;
	hcount/=ct;
	vhcount/=ct;
	outfile.open("v.dat");
	for (int i=0; i<vcount.size(); i++) outfile<<vcount(i)<<endl;
	outfile.close();
	outfile.open("h.dat");
	for (int i=0; i<hcount.size(); i++) outfile<<hcount(i)<<endl;
	outfile.close();
	outfile.open("vh.dat");
	for (int i=0; i<vhcount.size(); i++) outfile<<vhcount(i)<<endl;
	outfile.close();
}
void al_hv(RBM & rbm) {
	ofstream outfile;
	int totalh=(int)pow(2,rbm.Nh);
	int totalv=(int)pow(2,rbm.Nv);
	int totalvh=totalh*totalv;
	ArrayXd hprobs=ArrayXd::Zero(totalh);
	ArrayXd vprobs=ArrayXd::Zero(totalv);
	ArrayXd vhprobs=ArrayXd::Zero(totalvh);
	for (int i=0; i<totalh; i++) {
		rbm.h=int2state(i,rbm.Nh);
		for (int j=0; j<totalv; j++) {
			rbm.v=int2state(j,rbm.Nv);
			hprobs(i)+=exp(-rbm.E());
		}
	}
	double Z=hprobs.sum();
	hprobs/=Z;
	for (int i=0; i<totalv; i++) {
		rbm.v=int2state(i,rbm.Nv);
		for (int j=0; j<totalh; j++) {
			rbm.h=int2state(j,rbm.Nh);
			vprobs(i)+=exp(-rbm.E());
		}
	}
	vprobs/=Z;
	for (int i=0; i<totalv; i++) {
		rbm.v=int2state(i,rbm.Nv);
		for (int j=0; j<totalh; j++) {
			rbm.h=int2state(j,rbm.Nh);
			vhprobs(i*totalh+j)+=exp(-rbm.E());
		}
	}
	vhprobs/=Z;
	outfile.open("al_v.dat");
	for (int i=0; i<totalv; i++) outfile<<vprobs(i)<<endl;
	outfile.close();
	outfile.open("al_h.dat");
	for (int i=0; i<totalh; i++) outfile<<hprobs(i)<<endl;
	outfile.close();
	outfile.open("al_vh.dat");
	for (int i=0; i<totalvh; i++) outfile<<vhprobs(i)<<endl;
	outfile.close();
}




int main() {
	int Nv=5, Nh=2;
	srand(time(NULL));
	RBM rbm(Nv,Nh);
	rbm.W=ArrayXXd::Random(Nv,Nh);
	rbm.v=round((1+ArrayXd::Random(Nv))/2)*2-1;
	rbm.h=round((1+ArrayXd::Random(Nh))/2)*2-1;
	rbm.a=ArrayXd::Random(Nv);
	rbm.b=ArrayXd::Random(Nh);
	run_h(rbm);
	al_hcondv(rbm);
	rbm.v=round((1+ArrayXd::Random(Nv))/2)*2-1;
	rbm.h=round((1+ArrayXd::Random(Nh))/2)*2-1;
	run_v(rbm);
	al_vcondh(rbm);
	rbm.v=round((1+ArrayXd::Random(Nv))/2)*2-1;
	rbm.h=round((1+ArrayXd::Random(Nh))/2)*2-1;
	run_hv(rbm);
	al_hv(rbm);
	return 0;
}

				







