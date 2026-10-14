#include <iostream>
using namespace std;

// 1. Static Array Stack
struct StaticStack {
    int a[100], top = -1;
    void push(int x) { if(top < 99) a[++top] = x; }
    void pop() { if(top >= 0) top--; }
    void display() { for(int i = top; i >= 0; i--) cout << a[i] << " "; cout << "\n"; }
};

// 2. Linked List Stack
struct SNode { int data; SNode* next; SNode(int v): data(v), next(nullptr) {} };
struct LinkedStack {
    SNode* top = nullptr;
    void push(int x) { SNode* n = new SNode(x); n->next = top; top = n; }
    void pop() { if(top) { SNode* t = top; top = top->next; delete t; } }
    void display() { for(SNode* c = top; c; c = c->next) cout << c->data << " "; cout << "\n"; }
};

// 3. Static Array Queue
struct StaticQueue {
    int a[100], front = 0, rear = -1;
    void enqueue(int x) { if(rear < 99) a[++rear] = x; }
    void dequeue() { if(front <= rear) front++; }
    void display() { for(int i = front; i <= rear; i++) cout << a[i] << " "; cout << "\n"; }
};

// 4. Linked List Queue
struct LinkedQueue {
    SNode *front = nullptr, *rear = nullptr;
    void enqueue(int x) {
        SNode* n = new SNode(x);
        if(!rear) front = rear = n;
        else { rear->next = n; rear = n; }
    }
    void dequeue() {
        if(front) { SNode* t = front; front = front->next; if(!front) rear = nullptr; delete t; }
    }
    void display() { for(SNode* c = front; c; c = c->next) cout << c->data << " "; cout << "\n"; }
};

int main() {
    cout << "--- Static Stack ---\n";
    StaticStack ss; ss.push(10); ss.push(20); ss.display(); ss.pop(); ss.display();

    cout << "\n--- Linked Stack ---\n";
    LinkedStack ls; ls.push(10); ls.push(20); ls.display(); ls.pop(); ls.display();

    cout << "\n--- Static Queue ---\n";
    StaticQueue sq; sq.enqueue(10); sq.enqueue(20); sq.display(); sq.dequeue(); sq.display();

    cout << "\n--- Linked Queue ---\n";
    LinkedQueue lq; lq.enqueue(10); lq.enqueue(20); lq.display(); lq.dequeue(); lq.display();
}
