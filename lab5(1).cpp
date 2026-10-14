#include <iostream>
#include <string>
#include <stack>
using namespace std;

int prec(char c) {
    if (c == '+' || c == '-') return 1;
    if (c == '*' || c == '/') return 2;
    return -1;
}

string infixToPostfix(string s) {
    stack<char> st;
    string res = "";
    for (char c : s) {
        if (isalnum(c)) res += c;
        else if (c == '(') st.push(c);
        else if (c == ')') {
            while (!st.empty() && st.top() != '(') { res += st.top(); st.pop(); }
            if (!st.empty()) st.pop();
        } else {
            while (!st.empty() && prec(st.top()) >= prec(c)) { res += st.top(); st.pop(); }
            st.push(c);
        }
    }
    while (!st.empty()) { res += st.top(); st.pop(); }
    return res;
}

int main() {
    string infix = "A+(B*C)";
    cout << "Infix Expression: " << infix << "\n";
    cout << "Postfix Conversion: " << infixToPostfix(infix) << "\n";
}
