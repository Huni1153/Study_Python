# ----- 4장-----
# if,elif,else문 (비교연산자는 자바랑 동일[==, !=, <, <=, >, >=])

color = "black"
if color == "red":
    print("빨간색")
elif color == "green":
    print("초록색")
elif color == "black":
    print("검은색")
else:
    print("색이 없네?")

# in 연산자
vowels = 'aeiou'
letter = 'o'
letter in vowels
# 를 하게되면 결과값이 True가 나온다.

print("# 4장 연습문제")
print("# 4.1")
secret = 7
guess = 8
if secret == guess:
	print("juset right")
elif guess < secret:
	print("too low")
else:
	print("too high")
