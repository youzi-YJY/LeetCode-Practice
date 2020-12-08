class Solution:
    def findmin(self,num):
        '''
        :param num:输入的列表
        :return:最小项的索引
        除了循环之外，还有一些操作指令，这些指令都是伴随着循环的
        该算法必须要访问列表中的每一项，以保证能找到最小的项
        从而算法的复杂度是O(n)
        '''
        cur_index=1
        min_index=0
        while cur_index < len(num):
            if num[cur_index]<num[min_index]:
                min_index=cur_index
            cur_index+=1
        return min_index