import random
import pygame
n = 4
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
    count = -1
    count_index = -1
    dc ={}
    for i in mat[0]:
        count_index+=1
        if i==0:
            count+=1
            dc[count] = count_index
    m = count+1
    zero_num = k1%m
    for j in dc.keys():
        if j==zero_num:
            change = dc[j]
    mat[0][change]=d1
    return mat
#print(count_zero_down([[0, 0, 0, 0], [0, 1, 1, 3], [2, 0, 0, 3], [3, 3, 0, 1]]))
def count_zero_up(mat,k1,d1,n1=n-1):
    count = -1
    count_index = -1
    dc ={}
    for i in mat[n1]:
        count_index+=1
        if i==0:
            count+=1
            dc[count] = count_index
    m = count+1
    zero_num = k1%m
    for j in dc.keys():
        if j==zero_num:
            change = dc[j]
    mat[n1][change]=d1
    return mat
#print(count_zero_up([[2, 1, 1, 6], [0, 1, 0, 1], [3, 2, 0, 0], [0, 0, 0, 0]]))

def count_zero_right(mat,k1,d1):
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
    zero_num = k1%m
    for j in dc.keys():
        if j==zero_num:
            change = dc[j]
    mat[change][0] = d1
    return mat
#print(count_zero_right([[0, 1, 1, 3], [0, 2, 0, 3], [0, 0, 1, 1], [0, 3, 2, 0]]))

def count_zero_left(mat,k1,d1,n1=n-1):
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
    zero_num = k1%m
    for j in dc.keys():
        if j==zero_num:
            change = dc[j]
    mat[change][n1] = d1
    return mat
#************************************************************************
def mat_score(mat):
    score=0
    for i in mat:
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
    return score
#pygame.init() will initialize all imported pygame packages
#we can use pygame.get_init to check if all packages have imported successfuly

pygame.init()
#print(pygame.get_init())
#first i will open a pygame window and change the color of its surface
size = (300,350)
surface = pygame.display.set_mode(size)
color = (170, 157, 255)
surface.fill(color)
pygame.display.flip()
pygame. display. set_caption('Threes By Raha')
#now i will crear a rectangle
rect_color = (71, 61, 138)
square_color = (255,255,255)
pygame.draw.rect(surface,rect_color,pygame.Rect(50,50,200,200))
def drawing_rect(surface):
    pygame.draw.rect(surface,square_color,pygame.Rect(20,20,60,60),0,4)
    pygame.draw.rect(surface,square_color,pygame.Rect(88,20,60,60),0,4)
    pygame.draw.rect(surface,square_color,pygame.Rect(156,20,60,60),0,4)
    pygame.draw.rect(surface,square_color,pygame.Rect(224,20,60,60),0,4)
    pygame.draw.rect(surface,square_color,pygame.Rect(20,88,60,60),0,4)
    pygame.draw.rect(surface,square_color,pygame.Rect(88,88,60,60),0,4)
    pygame.draw.rect(surface,square_color,pygame.Rect(156,88,60,60),0,4)
    pygame.draw.rect(surface,square_color,pygame.Rect(224,88,60,60),0,4)
    pygame.draw.rect(surface,square_color,pygame.Rect(20,156,60,60),0,4)
    pygame.draw.rect(surface,square_color,pygame.Rect(88,156,60,60),0,4)
    pygame.draw.rect(surface,square_color,pygame.Rect(156,156,60,60),0,4)
    pygame.draw.rect(surface,square_color,pygame.Rect(224,156,60,60),0,4)
    pygame.draw.rect(surface,square_color,pygame.Rect(20,224,60,60),0,4)
    pygame.draw.rect(surface,square_color,pygame.Rect(88,224,60,60),0,4)
    pygame.draw.rect(surface,square_color,pygame.Rect(156,224,60,60),0,4)
    pygame.draw.rect(surface,square_color,pygame.Rect(224,224,60,60),0,4)
    return surface

drawing_rect(surface)
threes = [[0]*4 for i in range(4)]
for i in range(9):
    r,c = random.randint(0,3), random.randint(0,3)
    while threes[r][c]!=0:
        r,c = random.randint(0,3), random.randint(0,3)
    threes[r][c] = random.randint(1,3)
[print(" ".join([str(x) for x in r])) for r in threes]


for i in range(4):
    for j in range(4):
        font_name, font_size = "Times new Roman", 30
        font = pygame.font.SysFont(font_name, font_size)
        color = (0,0,0)
        if threes[i][j]!=0:
            text = font.render(str(threes[i][j]), True, color)
            surface.blit(text,(45+j*(68),35+i*(68)))
pygame.draw.rect(surface,square_color,pygame.Rect(25,300,250,30),0,4)
text = font.render('Your score is:0', True, (71, 61, 138))
surface.blit(text,(55,300))
pygame.display.flip()

flag = True
while True:
    while True:
        for event in pygame.event.get():
            drawing_rect(surface)
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key== pygame.K_ESCAPE):
                exit(0)
            if (down_change(threes)==threes) and (up_change(threes)==threes) and (left_change(threes)==threes) and (right_change(threes)==threes):
                flag = False
                break
            if event.type == pygame.KEYDOWN and event.key== pygame.K_DOWN:
                if down_change(threes)!= threes:
                    k = random.randint(0,3)
                    d = random.randint(1,3)
                    threes = count_zero_down(down_change(threes),k,d)
                print(threes)
                for i in range(4):
                    for j in range(4):
                        font_name, font_size = "Times new Roman", 30
                        font = pygame.font.SysFont(font_name, font_size)
                        color = (0,0,0)
                        if threes[i][j]!=0:
                            text = font.render(str(threes[i][j]), True, color)
                            surface.blit(text,(45+j*(68),35+i*(68)))
                pygame.draw.rect(surface,square_color,pygame.Rect(25,300,250,30),0,4)
                score = mat_score(threes)
                text = font.render('Your score is:'+str(score), True, (71, 61, 138))
                surface.blit(text,(55,300))
                pygame.display.flip()
                break
            elif event.type == pygame.KEYDOWN and event.key== pygame.K_UP:
                if up_change(threes)!= threes:
                    k = random.randint(0,3)
                    d = random.randint(1,3)
                    threes = count_zero_up(up_change(threes),k,d)
                print(threes)
                for i in range(4):
                    for j in range(4):
                        font_name, font_size = "Times new Roman", 30
                        font = pygame.font.SysFont(font_name, font_size)
                        color = (0,0,0)
                        if threes[i][j]!=0:
                            text = font.render(str(threes[i][j]), True, color)
                            surface.blit(text,(45+j*(68),35+i*(68)))
                pygame.draw.rect(surface,square_color,pygame.Rect(25,300,250,30),0,4)
                score = mat_score(threes)
                text = font.render('Your score is:'+str(score), True, (71, 61, 138))
                surface.blit(text,(55,300))
                pygame.display.flip()
                break
            elif event.type == pygame.KEYDOWN and event.key== pygame.K_LEFT:
                if left_change(threes)!= threes:
                    k = random.randint(0,3)
                    d = random.randint(1,3)
                    threes = count_zero_left(left_change(threes),k,d)
                print(threes)
                for i in range(4):
                    for j in range(4):
                        font_name, font_size = "Times new Roman", 30
                        font = pygame.font.SysFont(font_name, font_size)
                        color = (0,0,0)
                        if threes[i][j]!=0:
                            text = font.render(str(threes[i][j]), True, color)
                            surface.blit(text,(45+j*(68),35+i*(68)))
                pygame.draw.rect(surface,square_color,pygame.Rect(25,300,250,30),0,4)
                score = mat_score(threes)
                text = font.render('Your score is:'+str(score), True, (71, 61, 138))
                surface.blit(text,(55,300))
                pygame.display.flip()
                break
            elif event.type == pygame.KEYDOWN and event.key== pygame.K_RIGHT:
                if right_change(threes)!= threes:
                    k = random.randint(0,3)
                    d = random.randint(1,3)
                    threes = count_zero_right(right_change(threes),k,d)
                print(threes)
                for i in range(4):
                    for j in range(4):
                        font_name, font_size = "Times new Roman", 30
                        font = pygame.font.SysFont(font_name, font_size)
                        color = (0,0,0)
                        if threes[i][j]!=0:
                            text = font.render(str(threes[i][j]), True, color)
                            surface.blit(text,(45+j*(68),35+i*(68)))
                pygame.draw.rect(surface,square_color,pygame.Rect(25,300,250,30),0,4)
                score = mat_score(threes)
                text = font.render('Your score is:'+str(score), True, (71, 61, 138))
                surface.blit(text,(55,300))
                pygame.display.flip()
                break
        if not flag:
            score = mat_score(threes)
            rect_color = (71, 61, 138)
            square_color = (255,255,255)
            pygame.draw.rect(surface,rect_color,pygame.Rect(0,0,300,350))
            font_name, font_size = "Times new Roman", 30
            font = pygame.font.SysFont(font_name, font_size)
            color = (255,255,255)
            text = font.render('Your final score is:'+str(score), True, color)
            surface.blit(text,((size[0]-text.get_width())//2,(size[1]- text.get_height())//2))
            pygame.display.flip()
