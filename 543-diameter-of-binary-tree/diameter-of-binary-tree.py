class Solution(object):
    def diameterOfBinaryTree(self, root):

        def height(node):
            if node is None:
                return 0, 0  # (height, diameter)

            lh, ld = height(node.left)
            rh, rd = height(node.right)

            current_height = max(lh, rh) + 1

            current_diameter = max(
                ld,          # best diameter in left subtree
                rd,          # best diameter in right subtree
                lh + rh      # diameter through current node
            )

            return current_height, current_diameter

        return height(root)[1]