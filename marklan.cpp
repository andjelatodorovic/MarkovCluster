#include "marklan.hpp"

class marklan::marklan()
{
    srand(time(NULL));
}


void marklan::setModel(Mat prelazak,Mat inicijalna)
{
    _prelazak=EigenUtils::setDataf(prelazak);
    _inicijalna=EigenUtils::setDataf(inicijalna);
}

float marklan::verovatnoca(vector<int> sekvenca)
{
    float rez=0;
    float in=_inicijalna(0,sekvenca[0]);
    rez=in;
    for(int i=0;i<sekvenca.size()-1;i++)
    {
        rez=rez*_prelazak(sekvenca[i],sekvenca[i+1]);
    }
    return rez;

}

int marklan::randstanje(MatrixXf matrica,int indeks)
{

    float u=((float)rand())/RAND_MAX;
    cerr << u << endl;
    float s=matrica(0,0);
    int i=0;
    while(u>s & (i<matrica.col()))
    {
        i=i+1;
        s=s+matrica(indeks,i);
    }
    return i;
}


vector<int> marklan::gensek(int n)
{

    vector<int> rez;
    rez.resize(n);
    int i=0;
    int indeks=0;
    int init=randstanje(_inicijalna,0);
    rez[i]=in;
    index=in;
    for(i=1;i<n;i++)
    {
    indeks=randstanje(_prelazak,indeks);
    rez[i]=indeks;
    }
    return rez;
}
