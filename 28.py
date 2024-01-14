
def perm3(s1):
    i=0
    list1=[]
    list1.append(s1[i]+s1[i+1]+s1[i+2])
    list1.append(s1[i]+s1[i+2]+s1[i+1])
    list1.append(s1[i+1]+s1[i]+s1[i+2])
    list1.append(s1[i+1]+s1[i+2]+s1[i])
    list1.append(s1[i+2]+s1[i]+s1[i+1])
    list1.append(s1[::-1])
    return list1

def perm4(s2):
    
    list4=[]
    part1=s2[0]
    part2=s2[1:4]
    list1=(perm3(part2))
    for i in range(0,6,1):
        list4.append(part1+list1[i])
    part1=s2[1]
    part2=s2[0]+s2[2]+s2[3]
    list1=(perm3(part2))
    for i in range(0,6,1):
        list4.append(part1+list1[i])
    part1=s2[2]
    part2=s2[0]+s2[1]+s2[3]
    list1=(perm3(part2))
    for i in range(0,6,1):
        list4.append(part1+list1[i])
    part1=s2[3]
    part2=s2[0]+s2[1]+s2[2]
    list1=(perm3(part2))
    for i in range(0,6,1):
        list4.append(part1+list1[i])
    return list4

def perm5(s3):
    
    list5=[]
    part1=s3[0]
    part2=s3[1:5]
    list1=(perm4(part2))
    for i in range(0,24,1):
        list5.append(part1+list1[i])
    part1=s3[1]
    part2=s3[0]+s3[2]+s3[3]+s3[4]
    list1=(perm4(part2))
    for i in range(0,24,1):
        list5.append(part1+list1[i])
    part1=s3[2]
    part2=s3[0]+s3[1]+s3[3]+s3[4]
    list1=(perm4(part2))
    for i in range(0,24,1):
        list5.append(part1+list1[i])
    part1=s3[3]
    part2=s3[0]+s3[1]+s3[2]+s3[4]
    list1=(perm4(part2))
    for i in range(0,24,1):
        list5.append(part1+list1[i])
    part1=s3[4]
    part2=s3[0]+s3[1]+s3[2]+s3[3]
    list1=(perm4(part2))
    for i in range(0,24,1):
        list5.append(part1+list1[i])
    return list5


def perm6(s4):
    
    list6=[]
    part1=s4[0]
    part2=s4[1:6]
    list1=(perm5(part2))
    for i in range(0,120,1):
        list6.append(part1+list1[i])
    part1=s4[1]
    part2=s4[0]+s4[2]+s4[3]+s4[4]+s4[5]
    list1=(perm5(part2))
    for i in range(0,120,1):
        list6.append(part1+list1[i])
    part1=s4[2]
    part2=s4[0]+s4[1]+s4[3]+s4[4]+s4[5]
    list1=(perm5(part2))
    for i in range(0,120,1):
        list6.append(part1+list1[i])
    part1=s4[3]
    part2=s4[0]+s4[1]+s4[2]+s4[4]+s4[5]
    list1=(perm5(part2))
    for i in range(0,120,1):
        list6.append(part1+list1[i])
    part1=s4[4]
    part2=s4[0]+s4[1]+s4[2]+s4[3]+s4[5]
    list1=(perm5(part2))
    for i in range(0,120,1):
        list6.append(part1+list1[i])
    part1=s4[5]
    part2=s4[0]+s4[1]+s4[2]+s4[3]+s4[4]
    list1=(perm5(part2))
    for i in range(0,120,1):
        list6.append(part1+list1[i])
    return list6






def perm7(s5):
    
    list7=[]
    part1=s5[0]
    part2=s5[1:7]
    list1=(perm6(part2))
    for i in range(0,720,1):
        list7.append(part1+list1[i])
    part1=s5[1]
    part2=s5[0]+s5[2]+s5[3]+s5[4]+s5[5]+s5[6]
    list1=(perm6(part2))
    for i in range(0,720,1):
        list7.append(part1+list1[i])
    part1=s5[2]
    part2=s5[0]+s5[1]+s5[3]+s5[4]+s5[5]+s5[6]
    list1=(perm6(part2))
    for i in range(0,720,1):
        list7.append(part1+list1[i])
    part1=s5[3]
    part2=s5[0]+s5[1]+s5[2]+s5[4]+s5[5]+s5[6]
    list1=(perm6(part2))
    for i in range(0,720,1):
        list7.append(part1+list1[i])
    part1=s5[4]
    part2=s5[0]+s5[1]+s5[2]+s5[3]+s5[5]+s5[6]
    list1=(perm6(part2))
    for i in range(0,720,1):
        list7.append(part1+list1[i])
    part1=s5[5]
    part2=s5[0]+s5[1]+s5[2]+s5[3]+s5[4]+s5[6]
    list1=(perm6(part2))
    for i in range(0,720,1):
        list7.append(part1+list1[i])
    part1=s5[6]
    part2=s5[0]+s5[1]+s5[2]+s5[3]+s5[4]+s5[5]
    list1=(perm6(part2))
    for i in range(0,720,1):
        list7.append(part1+list1[i])
    return list7

def perm8(s6):
    
    list8=[]
    part1=s6[0]
    part2=s6[1:8]
    list1=(perm7(part2))
    for i in range(0,5040,1):
        list8.append(part1+list1[i])
    part1=s6[1]
    part2=s6[0]+s6[2]+s6[3]+s6[4]+s6[5]+s6[6]+s6[7]
    list1=(perm7(part2))
    for i in range(0,5040,1):
        list8.append(part1+list1[i])
    part1=s6[2]
    part2=s6[0]+s6[1]+s6[3]+s6[4]+s6[5]+s6[6]+s6[7]
    list1=(perm7(part2))
    for i in range(0,5040,1):
        list8.append(part1+list1[i])
    part1=s6[3]
    part2=s6[0]+s6[1]+s6[2]+s6[4]+s6[5]+s6[6]+s6[7]
    list1=(perm7(part2))
    for i in range(0,5040,1):
        list8.append(part1+list1[i])
    part1=s6[4]
    part2=s6[0]+s6[1]+s6[2]+s6[3]+s6[5]+s6[6]+s6[7]
    list1=(perm7(part2))
    for i in range(0,5040,1):
        list8.append(part1+list1[i])
    part1=s6[5]
    part2=s6[0]+s6[1]+s6[2]+s6[3]+s6[4]+s6[6]+s6[7]
    list1=(perm7(part2))
    for i in range(0,5040,1):
        list8.append(part1+list1[i])
    part1=s6[6]
    part2=s6[0]+s6[1]+s6[2]+s6[3]+s6[4]+s6[5]+s6[7]
    list1=(perm7(part2))
    for i in range(0,5040,1):
        list8.append(part1+list1[i])
    part1=s6[7]
    part2=s6[0]+s6[1]+s6[2]+s6[3]+s6[4]+s6[5]+s6[6]
    list1=(perm7(part2))
    for i in range(0,5040,1):
        list8.append(part1+list1[i])
    return list8



def perm9(s7):
    
    list9=[]
    part1=s7[0]
    part2=s7[1:9]
    list1=(perm8(part2))
    for i in range(0,40320,1):
        list9.append(part1+list1[i])
    part1=s7[1]
    part2=s7[0]+s7[2]+s7[3]+s7[4]+s7[5]+s7[6]+s7[7]+s7[8]
    list1=(perm8(part2))
    for i in range(0,40320,1):
        list9.append(part1+list1[i])
    part1=s7[2]
    part2=s7[0]+s7[1]+s7[3]+s7[4]+s7[5]+s7[6]+s7[7]+s7[8]
    list1=(perm8(part2))
    for i in range(0,40320,1):
        list9.append(part1+list1[i])
    part1=s7[3]
    part2=s7[0]+s7[1]+s7[2]+s7[4]+s7[5]+s7[6]+s7[7]+s7[8]
    list1=(perm8(part2))
    for i in range(0,40320,1):
        list9.append(part1+list1[i])
    part1=s7[4]
    part2=s7[0]+s7[1]+s7[2]+s7[3]+s7[5]+s7[6]+s7[7]+s7[8]
    list1=(perm8(part2))
    for i in range(0,40320,1):
        list9.append(part1+list1[i])
    part1=s7[5]
    part2=s7[0]+s7[1]+s7[2]+s7[3]+s7[4]+s7[6]+s7[7]+s7[8]
    list1=(perm8(part2))
    for i in range(0,40320,1):
        list9.append(part1+list1[i])
    part1=s7[6]
    part2=s7[0]+s7[1]+s7[2]+s7[3]+s7[4]+s7[5]+s7[7]+s7[8]
    list1=(perm8(part2))
    for i in range(0,40320,1):
        list9.append(part1+list1[i])
    part1=s7[7]
    part2=s7[0]+s7[1]+s7[2]+s7[3]+s7[4]+s7[5]+s7[6]+s7[8]
    list1=(perm8(part2))
    for i in range(0,40320,1):
       list9.append(part1+list1[i])
    part1=s7[8]
    part2=s7[0]+s7[1]+s7[2]+s7[3]+s7[4]+s7[5]+s7[6]+s7[7]
    list1=(perm8(part2))
    for i in range(0,40320,1):
        list9.append(part1+list1[i])
    return list9

s7="BEAUTIFUL"
list9=perm9(s7)
print(list9)




