#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void initializeArray(char** arr, int size) {
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < 2 * size - 1; j++) {
            arr[i][j] = ' ';
        }
    }
}

void printArray(char** arr, int size) {
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < 2 * size - 1; j++) {
            printf("%c", arr[i][j]);
        }
        printf("\n");
    }
}

void sierpinski(char** arr, int size, int row, int col) {
    if (size == 3) {
        arr[row][col] = '*';
        arr[row + 1][col - 1] = '*';
        arr[row + 1][col + 1] = '*';
        for (int i=col-2; i<=col+2; i++) {
            arr[row + 2][i] = '*';
        } 
        return;
    }
    
    int newSize = size / 2;

    sierpinski(arr, newSize, row, col);
    sierpinski(arr, newSize, row + newSize, col - newSize);
    sierpinski(arr, newSize, row + newSize, col + newSize);
}

int main() {
    int size;
    scanf("%d", &size);

    char** arr = (char**)malloc(size * sizeof(char*));
    for (int i = 0; i < size; i++) {
        arr[i] = (char*)malloc((2 * size - 1) * sizeof(char));
    }

    initializeArray(arr, size);
    sierpinski(arr, size, 0, size - 1);
    printArray(arr, size);


    for (int i = 0; i < size; i++) {
        free(arr[i]);
    }
    free(arr);

    return 0;
}