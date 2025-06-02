import sys
sys.setrecursionlimit(1000000)

n = int(sys.stdin.readline().rstrip())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))

inorder_index = {val: idx for idx, val in enumerate(inorder)}

def preorder(inorder_start, inorder_end, post_start, post_end):
    if inorder_start > inorder_end or post_start > post_end:
        return

    root = postorder[post_end]
    print(root, end=' ')
    
    inorder_root = inorder_index[root]
    left_tree = inorder_root - inorder_start
    
    preorder(inorder_start, inorder_root - 1, post_start, post_start + left_tree - 1)
    preorder(inorder_root + 1, inorder_end, post_start + left_tree, post_end - 1)

preorder(0, n - 1, 0, n - 1)
