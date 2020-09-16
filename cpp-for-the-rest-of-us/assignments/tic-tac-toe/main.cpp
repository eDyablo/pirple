#include <iostream>
#include <iomanip>

using namespace std;

int main() {
  char PLAYER_X = 'X', PLAYER_O = 'O';
  char lastPlayer = PLAYER_O, currentPlayer = PLAYER_X;
  char board[] = { '1', '2', '3', '4', '5', '6', '7', '8', '9'};
  // Main loop
  for (int turn = 1; turn <= 10; ++turn) {
    // Display the current board state
    cout << endl << "current board state:" << endl;
    for (int y = 0; y < 3; ++y) {
      cout << setw(4) << ' ';
      for (int x = 0; x < 3; ++x) {
        cout << board[3 * y + x] << (x < 2 ? '|' : char(0));
      }
      cout << endl;
      if (y < 2) {
        cout << setw(4) << ' ' << "-+-+-" << endl;
      }
    }
    cout << endl;
    // Check for a winner
    if (board[0] == lastPlayer && board[1] == lastPlayer && board[2] == lastPlayer) {
      cout << "Player " << lastPlayer << " win on the top row!" << endl; break;
    } else if (board[3] == lastPlayer && board[4] == lastPlayer && board[5] == lastPlayer) {
      cout << "Player " << lastPlayer << " win on the middle row!" << endl; break;
    } else if (board[6] == lastPlayer && board[7] == lastPlayer && board[8] == lastPlayer) {
      cout << "Player " << lastPlayer << " win on the bottom row!" << endl; break;
    } else if (board[0] == lastPlayer && board[3] == lastPlayer && board[6] == lastPlayer) {
      cout << "Player " << lastPlayer << " win on the left column!" << endl; break;
    } else if (board[1] == lastPlayer && board[4] == lastPlayer && board[7] == lastPlayer) {
      cout << "Player " << lastPlayer << " win on the middle column!" << endl; break;
    } else if (board[2] == lastPlayer && board[5] == lastPlayer && board[8] == lastPlayer) {
      cout << "Player " << lastPlayer << " win on the right column!" << endl; break;
    } else if (board[0] == lastPlayer && board[4] == lastPlayer && board[8] == lastPlayer) {
      cout << "Player " << lastPlayer << " win on the downward diagonal!" << endl; break;
    } else if (board[6] == lastPlayer && board[4] == lastPlayer && board[2] == lastPlayer) {
      cout << "Player " << lastPlayer << " win on the upward diagonal!" << endl; break;
    }
    // Handle player input
    while (turn < 10) {
      int chosenSquare = 0;
      cout << "Player " << currentPlayer << ", enter a number between 1 and 9: ";
      cin >> chosenSquare;
      if (chosenSquare < 1 || chosenSquare > 9) {
        cout << "Not a valid choice. Try Again." << endl;
      } else if (board[chosenSquare-1] == PLAYER_O || board[chosenSquare-1] == PLAYER_X) {
        cout << "That square is not available. Try again." << endl;
      } else {
        board[chosenSquare-1] = currentPlayer;
        break;
      }
    }
    // Switch players
    swap(currentPlayer, lastPlayer);
  }
  cout << endl << endl;
  return 0;
}
