# -*-coding:utf-8 -*-
class Solution:
    def setZeros(self,matrix):
        '''
        :param matrix: martrix
        :return: After setZeros matrix
        '''
        row=len(matrix)
        column=len(matrix[0])
        row_flag=False
        column_flag=False

        #检查第一行和第一列是否有零元素，更新标志位。
        #检查第一行
        for i in range(column):
            if matrix[0][i]==0:
                column_flag=True
                break
        #检查第一列
        for j in range(row):
            if matrix[j][0]==0:
                row_flag=True
                break

        #将第一行或者第一列作为标志位
        for i in range(1,row):
            for j in range(1,column):
                if matrix[i][j]==0:
                    matrix[0][j]=matrix[i][0]=0

        #内部置零操作
        for i in range(1,row):
            for j in range(1,column):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0

        #第一行、第一列置零操作
        if row_flag:
            for i in range(column):
                matrix[0][i]=0
        if column_flag:
            for j in range(row):
                matrix[j][0]=0

if __name__=="__main__":
    S=Solution()
    matrix=[[1,1,1],[1,0,1],[1,1,1]]
    S.setZeros(matrix)
    print(matrix)