# week04 _01

```
#week01_01_if.py

#P.163

number = int(input("정수"))
if number > 0:
  print("양수")

if number < 0:    # elif 사용 시에는 맞지 않는 문제, 첫번째 if에서 양수로 출력되기 때문에 esif로 작성하는게 더 나음
  print("음수")

if number == 0:
  print("0")
```

```
# week04  01 if py

# 주민등록번호 1234561234567
reg_num = input("주민등록번호")
gen_num = int(reg_num[6])
# 남자인 경우를 출력해주세요.
# 7번째 (6). 1. 3. 5. 7

#if str(gen_num) in "1357":
#  print("남자")

if gen_num % 2 == 1 :
  print("남자")

if gen_num == 1 \
  or gen_num == 3 \
  or gen_num == 5 \
  or gen_num == 7 :
    print("남자")
```
