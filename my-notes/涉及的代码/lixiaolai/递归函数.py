# def f(n):
#     print('\tn =', n)
#     if n == 1:
#         print('Returning...')
#         print('\tn =', n, 'return:', 1)
#         return 1
#     else:
#         r = n * f(n-1)
#         print('\tn =', n, 'return:', r)
#         return r
#
# print('Call f(5)...')
# print('Get out of f(n), and f(5) =', f(5))

# def a_monk_telling_story():
#     print('山上有座庙，庙里有个和尚，和尚讲故事，他说…… ')
#     return a_monk_telling_story()
#
# a_monk_telling_story()


import random

def in_dream(day=0, dead=False, kicked=False):
    dead = not random.randrange(0,10) # 1/10 probability to be dead
    kicked = not random.randrange(0,10) # 1/10 probability to be kicked
    day += 1
    print('dead:', dead, 'kicked:', kicked)

    if dead:
        print((f"I slept {day} days, and was dead to wake up..."))
        return day
    elif kicked:
        print(f"I slept {day} days, and was kicked to wake up...")
        return day

    return in_dream(day)

print('The in_dream() function returns:', in_dream())