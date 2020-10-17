# Aadil Mallick period 6 Gabor 1768092 codingbat exercises 1



def sleep_in(weekday, vacation):
    return False if weekday == True and vacation == False else True

def monkey_trouble(a_smile, b_smile):
    return True if a_smile == b_smile else False

def sum_double(a, b):
    return 2 * (a + b) if a==b else a + b

def diff21(n):
    return 2 * abs(n - 21) if n > 21 else abs(n-21)

def parrot_trouble(talking, hour):
    return True if talking == True and (hour < 7 or hour > 20) else False

def makes10(a, b):
    return True if (a == 10 or b == 10 or a + b == 10) else False

def near_hundred(n):
    return True if abs(n - 100) <= 10 or abs(n - 200) <= 10 else False

def pos_neg(a, b, negative):
    return (a < 0 and b < 0) if negative else ((a < 0 and b > 0) or (a > 0 and b < 0))

def hello_name(name):
    return 'Hello ' + name + '!'

def make_abba(a, b):
    return a + b + b + a

def make_tags(tag, word):
    return '<' + tag + '>' + word + '</' + tag + '>'

def make_out_word(out, word):
    return out[:len(out) // 2] + word + out[len(out) // 2:]

def extra_end(str):
    return str[-2:] * 3

def first_two(str):
    return str if len(str) < 2 else str[:2]

def first_half(str):
    return str[:len(str) // 2]

def without_end(str):
    return str[1:len(str) - 1]

def first_last6(nums):
    return nums[0] == 6 or nums[len(nums) - 1] == 6

def same_first_last(nums):
    return len(nums) >= 1 and nums[0] == nums[len(nums) - 1]

def make_pi(n):
    return [int(x) for x in (str(22/7)[:n+1]) if x != '.'] if n>1 else [3]

def common_end(a, b):
    return True if((a[0] == b[0]) or (a[-1:] == b[-1:])) else False

def sum3(nums):
    return(int(sum(nums)))

def rotate_left3(nums):
    return nums[1:] + [nums[0]] if len(nums) > 1 else nums

def reverse3(nums):
    return(list(reversed(nums)))

def max_end3(nums):
    return [nums[0] for x in nums] if(nums[0] > nums[-1]) else [nums[-1] for x in nums]

def cigar_party(cigars, is_weekend):
    return (cigars >= 40) if is_weekend else (cigars >= 40 and cigars <= 60)

def date_fashion(you, date):
    return 2 if (you >= 8 and date > 2) or (you > 2 and date >= 8) else 0 if you <= 2 or date <= 2 else 1

def squirrel_play(temp, is_summer):
    return 60 <= temp <= 100 if is_summer else 60 <= temp <= 90


def caught_speeding(speed, is_birthday):
    return 0 if (speed <= 60 + is_birthday * 5) else 1 if (speed >= 61 and speed <= (80 + is_birthday * 5)) else 2


def sorta_sum(a, b):
    return 20 if(a + b >= 10 and a + b <= 19) else a + b

def alarm_clock(day, vacation):
    return 'off' if (vacation == True and (day == 0 or day == 6)) else '10:00' if (vacation == True or (day == 0 or day == 6)) else '7:00'

def love6(a, b):
    return True if ((a==6 or b==6) or a+b==6 or abs(a-b) == 6) else False

def in1to10(n, outside_mode):
    return 1<=n<=10 if not outside_mode else (n <= 1 or n >= 10)

