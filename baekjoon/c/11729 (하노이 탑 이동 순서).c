#include <stdio.h>

void move (char from, char to){
    printf("%d %d\n", from, to);
}

void hanoi_tower(int n, char from, char tmp, char to) {
	if (n == 1) {
        move(from, to);
        return;
	}
	hanoi_tower(n - 1, from, to, tmp);
    move(from, to);
    hanoi_tower(n - 1, tmp, from, to);
}

int main() {
    int n;
    scanf("%d", &n);

    printf("%d", (1 << n) - 1);

	hanoi_tower(n, 1, 2, 3);
	return 0;
}