#include <iostream>
#include <string>

using namespace std;

int rotate4bitsLeft (int value, int amount)
{
  const int overflow = 0b10000;
  for (; amount > 0; --amount)
  {
    value <<= 1;
    if ((value & overflow) == overflow)
    {
      value &= 0b1111;  // remove overflow bit
      value |= 0b0001;  // set the rightmost bit
    }
  }
  return value;
}

int main() {
  int inValvesOpen  = 0b0010;
  int outValvesOpen = 0b0100;
  int pistonUp      = 0b1010;
  int cylinderFire  = 0b1000;
  for (int cycle = 0; cycle < 4; ++cycle) {
    string d1 = "   1       2       3       4   ";
    string d2 = "  ___     ___     ___     ___  ";
    string d3 = "x|   |x x|   |x x|   |x x|   |x";
    string d4 = " |   |   |   |   |   |   |   | ";
    string d5 = "  ---     ---     ---     ---  ";
    string d6 = "   ?       ?       ?       ?   ";
  }
  return 0;
}
