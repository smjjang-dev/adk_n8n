import random
def roll_dice(sides: int = 6) -> int:
 """
 주사위를 굴려 1부터 sides 사이의 숫자 하나를 무작위로 반환합니다.
 sides는 주사위 면의 개수이며, 지정하지 않으면 6면 주사위를 사용합니
다.
 """
 return random.randint(1, sides)