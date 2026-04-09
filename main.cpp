#include <iostream>
#include <cstdlib>
#include <string>
#include <chrono>
#include <thread>
using namespace std;

void thread_func() {
    while(true) {
        cout << "\033[2J\033[1;1H"; // Clear the console
        system("git push origin main");
        this_thread::sleep_for(chrono::seconds(1));
    }
}

int main() {
    thread t(thread_func);
    t.detach();
    for(int i = 0; ; i++) {
    FILE *fp = fopen("file.txt", "w");
    fprintf(fp, "%d", i);
    fclose(fp);
    system("git add file.txt");
    string cmd = "git commit -m \"commit " + to_string(i) + "\"";
    system(cmd.c_str());    
   }
   t.join();
    return 0;
}