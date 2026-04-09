#include <iostream>
#include <cstdlib>
#include <string>
#include <chrono>
#include <thread>
using namespace std;
int main() {
   for(int i = 0; ; i++) {
    FILE *fp = fopen("file.txt", "w");
    fprintf(fp, "%d", i);
    fclose(fp);
    system("git add file.txt");
    string cmd = "git commit -m \"commit " + to_string(i) + "\"";
    system(cmd.c_str());
    cmd = "git push origin master";
    system(cmd.c_str());
    this_thread::sleep_for(chrono::seconds(3));
   }
    return 0;
}