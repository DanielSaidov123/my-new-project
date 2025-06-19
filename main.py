print("Hello, GitHub!")


def matrix_in_matrix(arr_big,arr_small):
    flag=0
    for i in range(len(arr_big)):
        for j in  range(len(arr_big)):
            if arr_big[i][j]==arr_small[0][0]:
                for k in range(len(arr_small)):
                    for g in range(len(arr_small[k])):
                        if i+k>len(arr_big)-1 or j+g>len(arr_big[i])-1:
                            flag=1
                            break
                        elif arr_big[i+k][j+g]!=arr_small[k][g]:
                            flag=1
                            break
                    if flag==1:
                        break
                if flag==0:
                    return True
                else:
                    flag=0
    return False