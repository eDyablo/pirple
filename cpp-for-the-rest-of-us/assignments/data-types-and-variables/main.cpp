#include <iostream>

using namespace std;

int main() {
  int const MINUTES_PER_HOUR = 60;
  int numHours = 23;
  //MINUTES_PER_HOUR++;
  numHours++;
  cout << "There are " << numHours * MINUTES_PER_HOUR << " minutes in "
       << numHours << " hours" << endl;
  unsigned int zeroHour = 0;
  zeroHour--;
  cout << "1 hour before zero hour is " << zeroHour << endl;
  return 0;
}
