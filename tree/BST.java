package datastructuresandalgorithms.tree;

/**
 * Created by arivolitirouvingadame on 3/17/17.
 */
public class BST {
    static class BSTNode {
        int data;
        BSTNode left;
        BSTNode right;

        public BSTNode(int data) {
            this.data = data;
            this.left = null;
            this.right = null;
        }
    }

    public static boolean isIdentical(BSTNode root1, BSTNode root2) {
        if (root1 == null && root2 == null) {
            return true;
        }

        if (root1 == null && root2 != null) {
            return false;
        }

        if (root1 != null && root2 == null) {
            return false;
        }

        if (root1.data != root2.data) {
            return false;
        }

        return (isIdentical(root1.left, root2.left) && isIdentical(root1.right, root2.right));
    }

    public static void inorder(BSTNode root) {
        if (root == null) {
            return;
        }

        inorder(root.left);
        System.out.print(" " + root.data);
        inorder(root.right);
    }

    public static void preorder(BSTNode root) {
        if (root == null) {
            return;
        }

        System.out.print(" " + root.data);
        preorder(root.left);
        preorder(root.right);
    }

    public static void postorder(BSTNode root) {
        if (root == null) {
            return;
        }

        postorder(root.left);
        postorder(root.right);
        System.out.print(" " + root.data);
    }

    public static void treeTraversal(BSTNode root) {
        System.out.println("\n\n void treeTraversal(BSTNode root)");

        System.out.println("\n\n void inorder");
        inorder(root);

        System.out.println("\n\n void preorder");
        preorder(root);

        System.out.println("\n\n void postorder");
        postorder(root);
    }

    public static void main(String[] args) {
        BSTNode ten = new BSTNode(10);
        BSTNode twenty = new BSTNode(20);
        BSTNode thirty = new BSTNode(30);
        BSTNode forty = new BSTNode(40);
        BSTNode fifty = new BSTNode(50);

        thirty.left = twenty;
        twenty.left = ten;

        thirty.right = forty;
        forty.right = fifty;

        BSTNode root = thirty;
        treeTraversal(root);


        BSTNode root1 = root;
        BSTNode root2 = root;

        boolean identicalFlag = isIdentical(root1, root2);
        System.out.println("\n\n identicalFlag: " + identicalFlag);
    }
}