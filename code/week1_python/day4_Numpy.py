import numpy as np
mat1 =np.array([[1,2],[3,4],[5,6]])
mat2 = np.array([[10,20,30],[40,50,60]])
print(mat1[1])
c=np.array([100,200])
sum=c+mat1
print(sum)
print(mat1@mat2)
rand_mat=np.random.randint(1,100,(3,2))
print(rand_mat*mat1)


score = np.array([
    [85, 59],
    [92, 76],
    [45, 68],
    [98, 88],
    [60, 55]
])
print(score[score>60])
print(score[:,0][score[:,0]>80])
print(score[(score>70)&(score<95)])


ran_dom=np.random.randint(0,100,(4,3))
print(ran_dom)
print(ran_dom[1])
print(ran_dom[:,0])
arr=np.array([5,10,15])
new_arr=arr+ran_dom
new_arr1=new_arr*ran_dom
ran_dom1=np.random.randint(0,100,(3,4))
new_arr2=ran_dom@new_arr
new_arr3=ran_dom[ran_dom>=50]
print(len(new_arr3))