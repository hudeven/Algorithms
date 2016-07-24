class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        length = rowIndex + 2
        curRow = [0] * (length)
        lastRow = [0] * (length)
        curRow[1] = 1
        lastRow[1] = 1
        for i in range(1, rowIndex + 1):
            for j in range(1, i + 2):
                curRow[j] = lastRow[j - 1] + lastRow[j]
            print "row%d is: %s" % (i, lastRow)
            lastRow = copy.copy(curRow)

        return curRow[1:]
