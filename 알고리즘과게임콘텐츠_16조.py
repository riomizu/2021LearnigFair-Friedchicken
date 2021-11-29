def corona(jiyuk):
    global inwon
    if jiyuk=='경기' or jiyuk=='서울' or jiyuk=='인천':
        inwon=10
    elif jiyuk=='강원' or jiyuk=='충북' or jiyuk=='충남' or jiyuk=='전북' or jiyuk=='전남' or jiyuk=='경북' or jiyuk=='경남' or jiyuk=='제주':
        inwon=12
    else:
        print("정확한 지역명을 입력해주세요.")
        A=input("지역명을 다시 입력해주세요 ")
        corona(A)

def covid(saram):
    global b
    global c
    if 0 <= b-c <= 4 and 0 < b <= saram:
        print("이용이 가능합니다")
    else:
        print("이용이 불가능합니다")

inwon=0

print("11월부터 적용되는 위드 코로나 사회적 거리두기 방안에 따라 판단합니다.")

a=input("현재 본인이 계신 지역(서울, 경기, 인천, 강원, 충북, 충남,\
전북, 전남, 경북, 경남,제주)을 입력해주세요: ")


corona(a)

b=int(input("이용하실 총 인원수를 입력해 주세요: "))
c=int(input("예방 접종 완료자 인원수를 입력해 주세요: "))

covid(inwon)



