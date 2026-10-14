// Waseem_cu25220310

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct HeapFactory {
    vector<int> heap;
    bool isMin;
    HeapFactory(bool minH) : isMin(minH) {}

    void bubbleUp(int i) {
        while (i > 0) {
            int p = (i - 1) / 2;
            if (isMin ? heap[i] < heap[p] : heap[i] > heap[p]) {
                swap(heap[i], heap[p]);
                i = p;
            } else break;
        }
    }

    void insert(int val) {
        heap.push_back(val);
        bubbleUp(heap.size() - 1);
    }

    void display() {
        for (int x : heap) cout << x << " ";
        cout << "\n";
    }
};

int main() {
    cout << "--- Min Heap Factory ---\n";
    HeapFactory minH(true);
    for (int x : {20, 15, 30, 5, 10}) minH.insert(x);
    minH.display();

    cout << "--- Max Heap Factory ---\n";
    HeapFactory maxH(false);
    for (int x : {20, 15, 30, 5, 10}) maxH.insert(x);
    maxH.display();
}
