#my strategy is to choose the movement that has the most number of merged elements
#and apply that movement on te matrice
n = int(input())
mat_input =[]
for i in range(n):
    a = input().split()
    a = [int(x) for x in a]
    mat_input+=[a]
#print(mat)
#********************************************************
def left_change(mat):
    mat2=[]
    for list1 in mat:
        list1=[int(x) for x in list1]
        for i in range(len(list1)-1):
            if list1[i]==0:
                list1[i+1],list1[i]=list1[i],list1[i+1]
            else:
                if (list1[i]==1 and list1[i+1]==2) or (list1[i]==2 and list1[i+1]==1):
                    list1[i] = 3
                    list1[i+1] = 0
                else:
                    if list1[i] == list1[i+1] and list1[i]!=1 and list1[i]!=2:
                        list1[i]= 2*list1[i]
                        list1[i+1] = 0
        mat2+=[list1]
    return mat2
#print(left_change(mat_input))
#********************************************************
def right_change(mat):
    mat2 =[]
    for list1 in mat:
        list1 = [int(x) for x in list1]
        list1 = list1[::-1]
        for i in range(len(list1)-1):
            if list1[i]==0:
                list1[i+1],list1[i]=list1[i],list1[i+1]
            else:
                if (list1[i]==1 and list1[i+1]==2) or (list1[i]==2 and list1[i+1]==1):
                    list1[i] = 3
                    list1[i+1] = 0
                else:
                    if list1[i] == list1[i+1] and list1[i]!=1 and list1[i]!=2:
                        list1[i]= 2*list1[i]
                        list1[i+1] = 0
        list1 = list1[::-1]
        mat2+=[list1]
    return mat2
#print(right_change(mat_input))
#*********************************************************
def down_change(mat,n1=n):
    mat2 =[]
    j = 0
    while j<n1:
        ls =[]
        for i in range(n1):
            ls+=[mat[i][j]]
            ls = [int(x) for x in ls]
        mat2+=[ls]
        j+=1
    mat3 = right_change(mat2)
    mat4 =[]
    j = 0
    while j<n1:
        ls =[]
        for i in range(n1):
            ls+=[mat3[i][j]]
            ls = [int(x) for x in ls]
        mat4+=[ls]
        j+=1
    return mat4
#print(down_change(mat_input,n))
#*****************************************************
def up_change(mat,n1=n):
    mat2 =[]
    j = 0
    while j<n1:
        ls =[]
        for i in range(n1):
            ls+=[mat[i][j]]
            ls = [int(x) for x in ls]
        mat2+=[ls]
        j+=1
    mat3 = left_change(mat2)
    mat4 =[]
    j = 0
    while j<n1:
        ls =[]
        for i in range(n1):
            ls+=[mat3[i][j]]
            ls = [int(x) for x in ls]
        mat4+=[ls]
        j+=1
    return mat4
#print(up_change(mat_input))
#***************************************************
def count_zero_down(mat,k1,d1):
    unchanged_mat = mat
    count = -1
    count_index = -1
    dc ={}
    for i in mat[0]:
        count_index+=1
        if i==0:
            count+=1
            dc[count] = count_index
    m = count+1
    if m ==0:
        return unchanged_mat
    zero_num = k1%m
    for j in dc.keys():
        if j==zero_num:
            change = dc[j]
    mat[0][change]=d1
    return mat
#print(count_zero_down([[0, 0, 0, 0], [0, 1, 1, 3], [2, 0, 0, 3], [3, 3, 0, 1]]))
def count_zero_up(mat,k1,d1,n1=n-1):
    unchanged_mat = mat
    count = -1
    count_index = -1
    dc ={}
    for i in mat[n1]:
        count_index+=1
        if i==0:
            count+=1
            dc[count] = count_index
    m = count+1
    if m ==0:
        return unchanged_mat
    zero_num = k1%m
    for j in dc.keys():
        if j==zero_num:
            change = dc[j]
    mat[n1][change]=d1
    return mat
#print(count_zero_up([[2, 1, 1, 6], [0, 1, 0, 1], [3, 2, 0, 0], [0, 0, 0, 0]]))

def count_zero_right(mat,k1,d1):
    unchanged_mat = mat
    count = -1
    count_index = -1
    dc = {}
    for i in mat:
        count_index+=1
        a = i[0]
        if a==0:
            count+=1
            dc[count] = count_index
    m = count+1
    if m ==0:
        return unchanged_mat
    zero_num = k1%m
    for j in dc.keys():
        if j==zero_num:
            change = dc[j]
    mat[change][0] = d1
    return mat
#print(count_zero_right([[0, 1, 1, 3], [0, 2, 0, 3], [0, 0, 1, 1], [0, 3, 2, 0]]))

def count_zero_left(mat,k1,d1,n1=n-1):
    unchanged_mat = mat
    count = -1
    count_index = -1
    dc = {}
    for i in mat:
        count_index+=1
        a=i[n1]
        if a==0:
            count+=1
            dc[count] = count_index
    m = count+1
    if m ==0:
        return unchanged_mat
    zero_num = k1%m
    for j in dc.keys():
        if j==zero_num:
            change = dc[j]
    mat[change][n1] = d1
    return mat
#*******************************************************************************
#here starts the new code of part3
#I created 4 functions to find the biggest change in elements of a matrice after a movement
def biggest_change_left(mat,n1=n):
    previous_mat = mat
    ls = []
    dc ={}
    if mat!=left_change(mat):
        mat = left_change(mat)
        for i in range(n1):
            for j in range(n1):
                if previous_mat[i][j]==0:
                    break
                else:
                    if mat[i][j]>previous_mat[i][j]:
                        ls+=[mat[i][j]]
                        break
        number_of_changes = len(ls)
        dc['L'] = number_of_changes
    return dc
#print(biggest_change_left(mat_input))


def biggest_change_right(mat,n1=n):
    mat2 = []
    for i in mat:
        i = i[::-1]
        mat2+=[i]
    previous_mat = mat2
    ls = []
    dc ={}
    if mat2!=left_change(mat2):
        mat2 = left_change(mat2)
        for i in range(n1):
            for j in range(n1):
                if previous_mat[i][j]==0:
                    break
                else:
                    if mat2[i][j]>previous_mat[i][j]:
                        ls+=[mat2[i][j]]
                        break
        number_of_changes = len(ls)
        dc['R'] = number_of_changes
    return dc
#print(biggest_change_right(mat_input))

def biggest_change_up(mat,n1=n):
    mat2 =[]
    j = 0
    while j<n1:
        ls =[]
        for i in range(n1):
            ls+=[mat[i][j]]
            ls = [int(x) for x in ls]
        mat2+=[ls]
        j+=1
    previous_mat = mat2
    ls = []
    dc ={}
    if mat2!=left_change(mat2):
        mat2 = left_change(mat2)
        for i in range(n1):
            for j in range(n1):
                if previous_mat[i][j]==0:
                    break
                else:
                    if mat2[i][j]>previous_mat[i][j]:
                        ls+=[mat2[i][j]]
                        break
        number_of_changes = len(ls)
        dc['U'] = number_of_changes
    return dc


#print(biggest_change_up(mat_input))
def biggest_change_down(mat,n1=n):
    mat2 =[]
    j = 0
    while j<n1:
        ls =[]
        for i in range(n1):
            ls+=[mat[i][j]]
            ls = [int(x) for x in ls]
        mat2+=[ls]
        j+=1
    mat3 = []
    for i in mat2:
        i = i[::-1]
        mat3+=[i]
    previous_mat = mat3
    ls = []
    dc ={}
    if mat3!=left_change(mat3):
        mat3 = left_change(mat3)
        for i in range(n1):
            for j in range(n1):
                if previous_mat[i][j]==0:
                    break
                else:
                    if mat3[i][j]>previous_mat[i][j]:
                        ls+=[mat3[i][j]]
                        break
        number_of_changes = len(ls)
        dc['D'] = number_of_changes
    return dc

#now I will find the movement that has the most merged elements and then apply it on the matrice
def find_best_move(mat):
    final_answer_dict = {**biggest_change_left(mat),**biggest_change_down(mat),**biggest_change_right(mat),**biggest_change_up(mat)}
    #now we will find the move with most changes
    if len(final_answer_dict)>0:
        max_change = max(final_answer_dict.values())
        max_list = []
        for i in final_answer_dict :
            if final_answer_dict[i] == max_change:
                max_list+=[i]
        best_move = max_list[0]
        return best_move
    return 0

movement_number = int(input())
movement = ''
used_inputs =0
for i in range(movement_number):
    if find_best_move(mat_input)!=0:
        movement+=find_best_move(mat_input)
        inp = input().split()
        used_inputs+=1
        k = int(inp[0])
        d = int(inp[1])
        if find_best_move(mat_input)=='L':
            mat_input=count_zero_left(left_change(mat_input),k,d)
        elif find_best_move(mat_input)=='U':
            mat_input=count_zero_up(up_change(mat_input),k,d)
        elif find_best_move(mat_input)=='D':
            mat_input=count_zero_down(down_change(mat_input),k,d)
        elif find_best_move(mat_input)=='R':
            mat_input=count_zero_right(right_change(mat_input),k,d)
#now there is this one possibility that our matrice will not be changed anymore
#but there are more inputs that we have to receive
#to solve this problem we will do this:
for nn in range(movement_number-used_inputs):
    input()


score=0
for i in mat_input:
    for j in i:
        count_tavan=-1
        if j==0 or j==1 or j==2:
            continue
        else:
            num=j//3
            while num!=0:
                num=num//2
                count_tavan+=1
        score += 3**(count_tavan+1)
#******************************************************************
#now we print the results
print(movement)
for m in mat_input:
    for n in m:
        print(n, end = '\t')
    print()
if (down_change(mat_input)==mat_input) and (up_change(mat_input)==mat_input) and (left_change(mat_input)==mat_input) and (right_change(mat_input)==mat_input):
    print('The final score is '+str(score)+'.')
else:
    print('The partial score is '+str(score)+'.')













#
