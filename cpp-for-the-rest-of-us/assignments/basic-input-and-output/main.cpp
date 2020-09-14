#include <iostream>
#include <iomanip>

int main() {
  using namespace std;

  float price1, price2, price3;
  float total;

  cout << "enter a price:" << endl;
  cin >> price1;

  cout << "enter a price:" << endl;
  cin >> price2;

  cout << "enter a price:" << endl;
  cin >> price3;

  total = price1 + price2 + price3;

  cout << setiosflags(ios::fixed) << setprecision(2)
       << "Price 1 is" << setw(10) << price1 << endl
       << "Price 2 is" << setw(10) << price2 << endl
       << "Price 3 is" << setw(10) << price3 << endl
       << "Total price is:" << setw(10) << total << endl;

  return 0;
}
