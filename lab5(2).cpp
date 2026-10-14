#include <iostream>
#include <string>
#include <stack>
using namespace std;

int evaluatePostfix(string s) {
    stack<int> st;
    for (char c : s) {
        if (isdigit(c)) st.push(c - '0');
        else {
            int v2 = st.top(); st.pop();
            int v1 = st.top(); st.pop();
            if (c == '+') st.push(v1 + v2);
            else if (c == '-') st.push(v1 - v2);
            else if (c == '*') st.push(v1 * v2);
            else if (c == '/') st.push(v1 / v2);
        }
    }
    return st.top();
}

int main() {
    string postfix = "23*5+";
    cout << "Postfix Expression: " << postfix << "\n";
    cout << "Evaluation Result: " << evaluatePostfix(postfix) << "\n";
}
