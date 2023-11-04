
list1=list(set([1,2,3,4,5]))
list2=list(set([3,4,4,5,6,7]))



def common_elements(list1:list,list2:list):
    if len(list1)<=len(list2):
        common_list=[list1[i] for i in range(len(list1)) if list1[i] in list2]
    return common_list

common_list=common_elements(list1,list2)
print(common_list)