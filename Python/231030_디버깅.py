# 디버깅 하는법

a = [1,2,3,4]
print(a)
# 중단점 설정하기 : F9
# 빨간 점은 중단점(브레이크 표식). 클릭으로 누르거나 F9 누르거나!

# 그리고 디버깅이전까지 실행 하려면 F5 
# 새로운 실행 창이 작게 뜬다.

b = [5]
print(b) # 여기에 커서 위치가 있다 가정한다면.
# printb(b)가 노란색 불이 들어오고 빨간 중단점엔 집이 생김.

# 그리고 수정을 위해 오류메시지가 발생한 줄로 이동하려면 F4
c = ['apple']
print(c)

## 그 외 단축키
# 한 단계씩 코드 실행 : F11
# 프로시저 단위 실행 : F10
# 커서의 위치까지 디버깅 진행 : Ctrl + F10

# 디버그 중단 : Shift + F5
# 디버그 다시 시작 : Ctrl + Shift + F5
# 모든 중단점 삭제 : Ctrl + Shift + F9