#include <algorithm>
#include <iostream>
#include <iterator>
#include <vector>

using namespace std;

int main() {
  vector<int> numbers = {10, 1, 6, 9, 3, 8, 4, 5, 7, 2, 5, 3, 7, 1, 1};

  copy(begin(numbers), end(numbers), ostream_iterator<int>(cout, ", "));
  cout << endl;

  vector<size_t> counters(11);
  for (auto number: numbers) {
    ++counters[number];
  }
  copy(begin(counters), end(counters), ostream_iterator<int>(cout, ", "));
  cout << endl;

  for (size_t i = 1; i < size(counters); ++i) {
    counters[i] += counters[i-1];
  }
  copy(begin(counters), end(counters), ostream_iterator<int>(cout, ", "));
  cout << endl;

  vector<int> sorted(size(numbers));
  for (auto number: numbers) {
    sorted[(counters[number]--) - 1] = number;
  }
  copy(begin(sorted), end(sorted), ostream_iterator<int>(cout, ", "));
  cout << endl;

  return 0;
}
