
def solution(x, y):
    # Your code here
    x, y = int(x), int(y)
    i = 0

    def cycle(x, y):
        diff = x - y
        floor = diff // y
        rem = (diff % y > 0)
        s = floor + rem
        x, y = x - s * y, y
        return x, y, s

    while x != y:
        if x > y:
            x, y, s = cycle(x, y)
        elif y > x:
            y, x, s = cycle(y, x)
        i += s

    if x == 1 and y == 1:
        return str(i)
    else:
        return 'impossible'


print(solution(4,7))
#answer 4
#print answer(2,1)
#answer 1
