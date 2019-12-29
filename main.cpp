#include <cstdlib>
#include <cmath>
#include <limits>
#include <iostream>
#include <random>

double generateGaussianNoise(double mu, double sigma);

double generateGaussianNoise(double mu, double sigma)
{
    static const double epsilon = std::numeric_limits<double>::min();
    static const double two_pi = 2.0*3.14159265358979323846;
    std::random_device rd;
    int seed_in=rd();
    //seed_in=1729
    std::mt19937 mt(seed_in);
    std::uniform_real_distribution<double> dist(0.0, 1.0);
    thread_local double z0;
    thread_local double z1;
    thread_local double z2;
    thread_local bool generate;
    generate = !generate;

    if (!generate)
        return z1 * sigma + mu;

    double u1, u2;
    do
    {
        //u1 = rand() * (1.0 / RAND_MAX);
        //u2 = rand() * (1.0 / RAND_MAX);
        u1 = dist(mt);
        u2 = dist(mt);
    }
    while (u1 <= epsilon);

    //double z0;
    //double z1;
    z0 = sqrt(-2.0 * log(u1)) * cos(two_pi * u2);
    z1 = sqrt(-2.0 * log(u1)) * sin(two_pi * u2);

    return z0 * sigma + mu;
}
using namespace std;
int main(void) {

    int i=0;
    int rep=10000;
    while(i<rep) {
        int m=0;
        int s=100;
        i++;
        double x=generateGaussianNoise(m, s);
        cout <<  x << endl;
    }
    exit(0);

}








