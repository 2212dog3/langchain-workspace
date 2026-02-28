# 실행 할지 말지
is_rain = False

print("학원으로 갑니다.")
# print("우산 챙기기")
# print("학원에 도착합니다")

if is_rain:
    print("우산 챙기기")

print("학원에 도착합니다.")


# 둘 중 하나
num = 123

if (num % 2) == 0:
    print("짝")
else:
    print("홀")

# 여럿 중 하나
score = 99

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("c")
elif score >= 60:
    print("D")
elif score >= 50:
    print("F")