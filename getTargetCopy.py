class Solution(object):

    def getTargetCopy(self, original, cloned, target):

        """
      :type original: TreeNode
      :type cloned: TreeNode
      :type target: TreeNode
      :rtype: TreeNode
      """

    if original == None:
        return None

    if original == target:
        return cloned

    else:
        answer1 = self.getTargetCopy(original.left, cloned.left, target)
        answer2 = self.getTargetCopy(original.right, cloned.right, target)

    return answer1 or answer2
