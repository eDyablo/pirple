#include <iostream>

using namespace std;

int main() {
  cout << "Think of a number between 1 and 100dd" << endl;
  int highest = 100, lowest = 0, attempts = 0;
  while (true) {
    ++attempts;
    int guess = lowest + (highest - lowest) / 2;
    cout << "I guess " << guess << ". Am I right?" << endl;
    cout << "’q’ to quit, ‘y’ if correct, ‘h’ if too high, ‘l’ if too low." << endl;
    char answer;
    cin >> answer;
    switch (answer) {
    case 'y':
    case 'Y':
      cout << "I guessed it in " << attempts << " attempts." << endl;
      return attempts;
    case 'h':
    case 'H':
      highest = guess;
      break;
    case 'l':
    case 'L':
      lowest = guess;
      break;
    case 'q':
    case 'Q':
      cout << "You quit. Bye." << endl;
      return attempts;
    default:
      cout << "I didn’t understand that response." << endl;
      --attempts;
    }
  }
  return 0;
}
