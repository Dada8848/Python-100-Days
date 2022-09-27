# import random
#
# r1 = random.SystemRandom()
# rand_num = r1.randint(0, 10)
#
# rand_nums = [r1.randint(0, 10) for i in range(10)]
#
# print(rand_nums)

# from turtle import*
#
#
# def setting():          #参数设置
#     pensize(4)
#     hideturtle()        #使乌龟无形（隐藏）
#     colormode(255)      #将其设置为1.0或255.随后 颜色三元组的r，g，b值必须在0 .. cmode范围内
#     color((255,155,192),"pink")
#     setup(840,500)
#     speed(10)
#
# def piecewise(x):
#     # x = float(input('x = '))
#     if x > 1:
#         y = 3 * x - 5
#     elif x >= -1:
#         y = x + 2
#     else:
#         y = 5 * x + 3
#     # print('f(%.2f) = %.2f' % (x, y))
#     color(239, 69, 19)
#     penup()
#     goto(x+100, y)
#     pendown()
#     setheading(-80)
#     dot(2, "blue")
#
# setting()
# for i in range(-100, 100):
#     piecewise(i)

# import textwrap
# import time
#
# available_clocks = [
#     ('monotonic', time.monotonic),
#     ('perf_counter', time.perf_counter),
#     ('process_time', time.process_time),
#     ('time', time.time),
# ]
#
# for clock_name, func in available_clocks:
#     print(textwrap.dedent('''\
#     {name}:
#         adjustable    : {info.adjustable}
#         implementation: {info.implementation}
#         monotonic     : {info.monotonic}
#         resolution    : {info.resolution}
#         current       : {current}
#     ''').format(
#         name=clock_name,
#         info=time.get_clock_info(clock_name),
#         current=func())
#     )

# time_perf_counter.py
# import hashlib
# import time
#
# # Data to use to calculate md5 checksums
# data = open(__file__, 'rb').read()
#
# loop_start = time.perf_counter()
#
# for i in range(5):
#     iter_start = time.perf_counter()
#     h = hashlib.sha1()
#     for i in range(300000):
#         h.update(data)
#     cksum = h.digest()
#     now = time.perf_counter()
#     loop_elapsed = now - loop_start
#     iter_elapsed = now - iter_start
#     print(time.ctime(), ': {:0.3f} {:0.3f}'.format(
#         iter_elapsed, loop_elapsed))

#zlib_memory.py
# import zlib
# import binascii
#
# original_data = b'This is the original text.'
# print('Original     :', len(original_data), original_data)
#
# compressed = zlib.compress(original_data)
# print('Compressed   :', len(compressed),
#       binascii.hexlify(compressed))
#
# decompressed = zlib.decompress(compressed)
# print('Decompressed :', len(decompressed), decompressed)

class planes(object):
    def __init__(self, **kwargs):
        if 'name' in kwargs and 'size' in kwargs and 'height' in kwargs:
            self.name = kwargs['name']
            self.size = kwargs['size']
            self.height = kwargs['height']

    def __str__(self):
        return 'The plane %s is flying at an altitude of %dm.' % (self.name, self.height)

    def fly(self, height):
        self.height = height
        print('The plane %s is flying at an altitude of %dm.' % (self.name, self.height))


def main():
    pla1 = planes(name='J20', size=10, height=10000)
    print(pla1)
    pla1.fly(30000)
    print(pla1.size)


if __name__ == '__main__':
    main()
