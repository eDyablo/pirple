#include <atomic>
#include <chrono>
#include <iostream>
#include <mutex>
#include <thread>
#include <vector>

using namespace std;

atomic<size_t> counter = 0;

mutex io_mutext;

auto inc() {
  static atomic<size_t> counter = 0;
  return ++counter;
}

void count(size_t n) {
  for (size_t i = 0; i < n; ++i) {
    auto const c = inc();
    {
      unique_lock<mutex> lock_io(io_mutext);
      cout << c << " thread using function" << endl;
    }
    this_thread::sleep_for(chrono::microseconds(10));
  }
}

struct counter_t {
  size_t n;

  counter_t(size_t n) : n(n) {
  }

  void operator() () {
    for (size_t i = 0; i < n; ++i) {
      auto const c = inc();
      {
        unique_lock<mutex> lock_io(io_mutext);
        cout << c << " thread using object" << endl;
      }
      this_thread::sleep_for(chrono::microseconds(20));
    }
  }
};

int main() {
  vector<thread> threads;
  
  threads.push_back(thread(::count, 5));
  threads.push_back(thread(counter_t(5)));
  threads.push_back(thread(counter_t(5)));

  for (auto& thread: threads) {
    if (thread.joinable()) {
      thread.join();
    }
  }
  return 0;
}
