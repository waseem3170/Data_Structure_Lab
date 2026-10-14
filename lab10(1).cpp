#include <iostream>
#include <vector>
#include <list>
using namespace std;

// 1. Open Hashing (Chaining)
struct OpenHash {
    vector<list<int>> table;
    OpenHash(int s) : table(s) {}
    void insert(int k) { table[k % table.size()].push_back(k); }
    void display() {
        for (int i = 0; i < table.size(); i++) {
            cout << i << ": ";
            for (int x : table[i]) cout << x << " -> ";
            cout << "NULL\n";
        }
    }
};

// 2. Closed Hashing (Linear Probing)
struct ClosedHash {
    vector<int> table;
    int size;
    ClosedHash(int s) : size(s), table(s, -1) {}
    void insert(int k) {
        int idx = k % size;
        while (table[idx] != -1) idx = (idx + 1) % size;
        table[idx] = k;
    }
    void display() {
        for (int i = 0; i < size; i++) cout << i << ": " << table[i] << "\n";
    }
};

int main() {
    cout << "--- Open Hashing (Chaining) ---\n";
    OpenHash oh(5); oh.insert(10); oh.insert(15); oh.insert(7); oh.display();

    cout << "\n--- Closed Hashing (Linear Probing) ---\n";
    ClosedHash ch(5); ch.insert(10); ch.insert(15); ch.insert(7); ch.display();
}
