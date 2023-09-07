
# 문자열은 연산 X, 새로 생성하게 됨
my_major = "컴퓨터정보" 
my_major += "1학년"             
my_major += "파이선프로그래밍" 
print(my_major)

# 슬라이싱
mymajor = "컴퓨터정보" 
print(mymajor[:])
print(mymajor[0:5:2]) # 2개씩 점프해서 뽑기
print(mymajor[0:5:1]) # 1개씩 점프해서 뽑기

mymajor = "컴퓨터정보"
print(mymajor[0:3])
print(mymajor[1:3])
print(mymajor[2:3])
print(mymajor[:3]) # 시작 인덱스 없으면 처음부터 실행
print(mymajor[3:5])
print(mymajor[3:]) # 끝 인덱스 없으면 마지막까지 실행
print(mymajor)

mymajor = "컴퓨터정보"
print(mymajor[-1])
print(mymajor[0])
print(mymajor[1])
print(mymajor[2])
print(mymajor[3])
print(mymajor[4])
print(mymajor[5])
print(mymajor)

mymajor = "컴퓨터정보"
print(mymajor[-5])
print(mymajor[-4])
print(mymajor[-3])
print(mymajor[-2])
print(mymajor[-1])
print(mymajor)

# 연산자의 양쪽엔 동일한 피연산자 사용 필요
print("=-" * 30)
print(10 + 10)
print("나이:" + "10")
#print("나이:" + 10) 
