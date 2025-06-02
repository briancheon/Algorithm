#include <stdio.h>
#include <stdlib.h>

#define INF 1000000001LL
typedef long long ll;

typedef struct {
    ll max1, max2, max_cnt, s;
} Node;

int N, M;
ll *A;
Node *tree;
ll *lazy;

ll maxll(ll a, ll b) { return a > b ? a : b; }
ll minll(ll a, ll b) { return a < b ? a : b; }

Node compare_nodes(Node a, Node b) {
    Node res;
    if (a.max1 == b.max1) {
        res.max1 = a.max1;
        res.max2 = maxll(a.max2, b.max2);
        res.max_cnt = a.max_cnt + b.max_cnt;
        res.s = a.s + b.s;
    } else {
        if (a.max1 > b.max1) {
            Node tmp = a; a = b; b = tmp;
        }
        res.max1 = b.max1;
        res.max2 = maxll(a.max1, b.max2);
        res.max_cnt = b.max_cnt;
        res.s = a.s + b.s;
    }
    return res;
}

void build(int start, int end, int idx) {
    lazy[idx] = -INF;
    if (start == end) {
        tree[idx].max1 = A[start];
        tree[idx].max2 = -INF;
        tree[idx].max_cnt = 1;
        tree[idx].s = A[start];
        return;
    }
    int mid = (start + end) / 2;
    build(start, mid, idx * 2);
    build(mid + 1, end, idx * 2 + 1);
    tree[idx] = compare_nodes(tree[idx * 2], tree[idx * 2 + 1]);
}

void push(int start, int end, int idx) {
    if (lazy[idx] == -INF) return;
    ll v = lazy[idx];
    Node *node = &tree[idx];
    if (node->max1 <= v) {
        lazy[idx] = -INF;
        return;
    }
    node->s -= node->max_cnt * (node->max1 - v);
    node->max1 = v;
    if (start != end) {
        for (int i = idx * 2; i <= idx * 2 + 1; ++i) {
            if (lazy[i] == -INF || lazy[i] > v) {
                lazy[i] = (lazy[i] == -INF) ? v : minll(lazy[i], v);
            }
        }
    }
    lazy[idx] = -INF;
}

void update_lazy(int start, int end, int idx) {
    push(start, end, idx);
}

ll interval_max(int start, int end, int idx, int left, int right) {
    update_lazy(start, end, idx);
    if (left > end || right < start) return -INF;
    if (left <= start && right >= end) return tree[idx].max1;
    int mid = (start + end) / 2;
    return maxll(
        interval_max(start, mid, idx * 2, left, right),
        interval_max(mid + 1, end, idx * 2 + 1, left, right)
    );
}

ll interval_sum(int start, int end, int idx, int left, int right) {
    update_lazy(start, end, idx);
    if (left > end || right < start) return 0;
    if (left <= start && right >= end) return tree[idx].s;
    int mid = (start + end) / 2;
    return interval_sum(start, mid, idx * 2, left, right) +
           interval_sum(mid + 1, end, idx * 2 + 1, left, right);
}

void update_tree(int start, int end, int idx, int left, int right, ll value) {
    update_lazy(start, end, idx);
    Node *node = &tree[idx];
    if (right < start || left > end || node->max1 <= value) return;
    if (left <= start && end <= right && node->max2 < value) {
        lazy[idx] = value;
        update_lazy(start, end, idx);
        return;
    }
    int mid = (start + end) / 2;
    update_tree(start, mid, idx * 2, left, right, value);
    update_tree(mid + 1, end, idx * 2 + 1, left, right, value);
    tree[idx] = compare_nodes(tree[idx * 2], tree[idx * 2 + 1]);
}

int main() {
    scanf("%d", &N);

    A = (ll*)malloc(sizeof(ll) * 4 * N);
    tree = (Node*)malloc(sizeof(Node) * (4 * N));
    lazy = (ll*)malloc(sizeof(ll) * (4 * N));

    for (int i = 0; i < N; ++i) scanf("%lld", &A[i]);
    build(0, N - 1, 1);

    scanf("%d", &M);
    for (int i = 0; i < M; ++i) {
        int q, L, R;
        ll X;
        scanf("%d", &q);
        if (q == 1) {
            scanf("%d %d %lld", &L, &R, &X);
            update_tree(0, N - 1, 1, L - 1, R - 1, X);
        } else if (q == 2) {
            scanf("%d %d", &L, &R);
            printf("%lld\n", interval_max(0, N - 1, 1, L - 1, R - 1));
        } else {
            scanf("%d %d", &L, &R);
            printf("%lld\n", interval_sum(0, N - 1, 1, L - 1, R - 1));
        }
    }

    free(A);
    free(tree);
    free(lazy);
    return 0;
}