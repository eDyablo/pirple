#include <math.h>
#include <iostream>

using namespace std;

int main() {
  float a, b, c;
  float x1, x2;

  cout << "enter the value for a" << endl;
  cin >> a;

  cout << "enter the value for b" << endl;
  cin >> b;

  cout << "enter the value for c" << endl;
  cin >> c;

  x1 = (-b - sqrtf(b * b - 4 * a * c)) / (2 * a);
  x2 = (-b + sqrtf(b * b - 4 * a * c)) / (2 * a);

  cout << "The first value of x is " << x1 << endl;
  cout << "The second value of x is " << x2 << endl;

  return 0;
}
