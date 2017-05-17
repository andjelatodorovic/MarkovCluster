#ifndef MARKLAN_HPP
#define MARKLAN_HPP
#include "endzili/eigenutils.hpp"
#include "Common/OpenCVCommon.hpp"
#include <time.h> 
class marklan
{
public:
    marklan();
    MatrixXf _prelazak;
    MatrixXf _inicijalna;

   void setModel(Mat prelazak,Mat inicijalna);
   
    float verovatnoca(vector<int> sekvenca);

    int randstanje(MatrixXf matrica,int indeks);

    vector<int> gensek(int n);

};

class MarkovSequenceClassifier
{
    vector<marklan> model;
};


#endif
