  #Aadil Mallick Gabor period 7

def string_times(str, n):
  return str*n

def front_times(str, n):
  return str[:3]*n if len(str) >= 3 else str*n

def string_bits(str):
  return str[::2]

def string_splosion(str):
  return ''.join([str[:i] for i in range(1 , len(str) + 1)])

def last2(str):
  return sum([1 for index,value in enumerate(str[:-2]) if str[index:index+2] == str[-2:] ])

def array_count9(nums):
  return nums.count(9)

def array_front9(nums):
  return 9 in nums if len(nums) < 4 else 9 in nums[:4]

def array123(nums):
  return 0 < sum([1 for x,v in enumerate(nums[:-2]) if v == 1 and nums[x+1] == 2 and nums[x+2] == 3])

def string_match(a, b):
  return sum([1 for x in range(min(len(a), len(b)) - 1) if a[x:x + 2] == b[x:x + 2]])

def double_char(str):
  return ''.join([char*2 for char in str])

def count_hi(str):
  return str.count('hi')

def cat_dog(str):
  return str.count('cat') == str.count('dog')

def count_code(str):
  return sum([1 for x in range(len(str)-3) if (str[x:x+2] == 'co' and str[x+3] == 'e') ])

def end_other(a, b):
  return a.lower().endswith(b.lower()) or b.lower().endswith(a.lower())

def xyz_there(str):
  return 0 < sum([1 for x in range(len(str)-2) if (str[0:1] == x or (str[x:x+3] == 'xyz' and str[x-1:x] != '.'))])

def make_bricks(small, big, goal):
  return goal%5 >= 0 and goal%5 - small <= 0 and small + 5*big >= goal

def lone_sum(a, b, c):
  return sum([ [a,b,c][x] for x in range(3) if not [a,b,c].count([a,b,c][x]) > 1])

def lucky_sum(a, b, c):
  return sum([a,b,c][:[a,b,c].index(13)]) if 13 in [a,b,c] else sum([a,b,c])

def no_teen_sum(a, b, c):
  return sum([x for x in [a,b,c] if x not in [13,14,17,18,19]])

def round_sum(a, b, c):
  return sum((num // 10 + 1) * 10 if num % 10 >= 5 else (num // 10) * 10 for num in (a, b, c))

def close_far(a, b, c):
  return (abs(a-b) <= 1 or abs(a-c) <= 1) and ((abs(b-a)>=2 and abs(b-c)>=2) or (abs(c-a) >= 2 and abs(c-b)>=2))

def make_chocolate(small, big, goal):
  return (lambda n: n if n <= small else -1)(goal - 5 * min(big, goal//5))

def count_evens(nums):
  return sum([1 for x in nums if x % 2 == 0])

def big_diff(nums):
  return max(nums) - min(nums)

def centered_average(nums):
  return sum(sorted(nums)[1:-1]) // (len(nums) - 2)

def sum13(nums):
  return sum(nums[x] for x in range(len(nums)) if nums[x]!=13 and (x==0 or nums[x-1]!=13))

def sum67(nums):
  count = 0
  flag = False
  for n in nums:
    if n == 6:
      flag = True
      continue
    if n == 7 and flag:
      flag = False
      continue
    if not flag:
      count += n
  return count




def has22(nums):
  return 0 < sum([1 for x,v in enumerate(nums[:-1]) if v == 2 and nums[x+1] == 2])


