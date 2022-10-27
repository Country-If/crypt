# 实验报告

## 要求
- 求两个数的最大公约数。
- 判断一个数是否为素数。可以利用试除法或者教材P221 算法 
- 实现扩展欧几里得算法，可以计算模逆 
- 利用教材P221 反复平方乘算法，可以模指 
- 利用上述函数，实现RSA算法，ElGamal算法，DH密钥交换协议。 

## 已实现
### 基本函数
- 求两个数的最大公约数

递归法：
```python
def gcd_recursion(a, b):
    """
    递归法计算两个数的最大公约数: a = q * b + r

    :param a: int
    :param b: int
    :return: int
    """
    if b == 0:
        return a
    else:
        return gcd_recursion(b, a % b)
```
迭代法：
```python
def gcd_iteration(a, b):
    """
    迭代法计算两个数的最大公约数: a = q * b + r

    :param a: int
    :param b: int
    :return: int
    """
    while True:
        r = a % b  # Calculate the remainder
        if r == 0:
            break
        # Change the value of a and b
        a = b
        b = r
    return b
```
- 判断一个数是否是素数

试除法：
```python
def is_prime(n):
    """
    试除法判断整数n是否是素数

    :param n: int
    :return: bool：是素数返回True，否则返回False
    """
    i = 2  # 从2开始穷举
    while i <= math.sqrt(n):  # 穷举到sqrt(n)
        if n % i == 0:  # 是素数
            return False
        i += 1
    return True
```
参考Python第三方库primePy：
```python
def _factor(num):
    """
    Calculates the lowest prime factor by default

    :param num: int
    :return: int
    """
    if num == 2 or num % 2 == 0:
        return 2
    else:
        for i in range(3, int(math.sqrt(num)) + 1, 2):  # I could iterate over a list of primes
            if num % i == 0:  # But creating that list of primes turns out even more intensive task
                return i
        else:
            return num


def prime_check(num):
    """
    判断是否是素数，参考Python第三方库primePy

    :param num: int
    :return: bool: 是素数返回True，否则返回False
    """
    # from primePy import primes
    # primes.check()

    if _factor(num) == num:
        return True
    else:
        return False
```
- 扩展欧几里得算法计算模逆
```python
def InvMod(a, b):
    """
    递归实现扩展欧几里得算法: ed = 1 (mod n)

    :param a: e(int)
    :param b: n(int)
    :return: gcd, x, y (x即是e^-1，也就是d)(int, int, int)
    """
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = InvMod(b, a % b)
        t = x
        x = y
        y = t - a // b * y
        return gcd, x, y
```
- 反复平方乘算法计算模幂
```python
def ExpMod(a, b, n):
    """
    模指运算: a^b (mod n)

    :param a: int
    :param b: int
    :param n: int
    :return: int
    """
    b = bin(b)[2:]  # 获取二进制，去掉开头的'0b'
    # 快速平方乘算法得到列表
    L = [a]
    for i in range(len(b) - 1):
        a = a * a
        L.append(a)
    L.reverse()  # 列表反转，与二进制位对应
    # 对二进制值中为1的项相乘并模n
    res = 1
    for i in range(len(b)):
        if b[i] == '1':
            # 边乘边模
            res *= L[i]
            res %= n
    return res
```
- 随机生成二进制位数为n的大素数p、q
```python
def generate_p_q(n_bit):
    """
    随机生成二进制位数为n的大素数p、q

    :param n_bit: int，整数对应的二进制位数
    :return: (p, q)
    """
    # 随机生成n位二进制所对应的十进制整数
    if n_bit <= min_size:
        raise ValueError("n太小了，n必须大于" + str(min_size) + "，n值建议小于50")
    randint_list = ['1'] * n_bit  # 初始化长度为n的列表
    # 随机更改数据的位置
    pos_list = random.sample(range(1, n_bit), random.randint(min_size, n_bit) - 1)
    for pos in pos_list:
        randint_list[pos] = '0'
    randint_str = ''.join(randint_list)  # 列表转字符串
    randint = int(randint_str, 2)  # 十进制值
    # 获取p, q
    while not prime_check(randint):
        randint += 1
    p = randint
    randint += random.randint(min_size, n_bit)  # 加上随机数得到新的随机整数
    while not prime_check(randint):
        randint += 1
    q = randint
    return p, q
```
- 随机生成n位的素数
```python
def generate_prime(n_digit):
    """
    随机生成n位的素数

    :param n_digit: int，素数位数
    :return: int，n位素数
    """
    if n_digit < 1:
        raise ValueError("素数位数不能小于1")
    rand_list = random.sample([str(i) for i in range(1, 10)], 9)  # 初始化1-9的不重复列表，防止生成类似999的整数，影响后续操作
    randint_list = rand_list[: n_digit]
    if n_digit > 9:  # 超过位数则补齐
        while len(randint_list) < n_digit:
            randint_list.append(str(random.randint(0, 9)))
    randint = int("".join(randint_list))  # 转为整数
    while not prime_check(randint):  # 得到素数
        randint += 1
    return randint
```
- 生成大素数p及其本原元g
```python
def generate_p_g(n_digit):
    """
    生成大素数p及其本原元g

    :param n_digit: int，素数位数
    :return: (p, q), (int, int)
    """
    while True:
        q = generate_prime(n_digit)  # 随机生成一个n位的素数q
        if prime_check(2 * q + 1):  # 判断 2*q+1 是否为素数
            p = 2 * q + 1
            break
    while True:
        g = random.randint(2, p - 2)  # 随机选取整数g，g范围：(1, p - 1)
        if ExpMod(g, 2, p) != 1 and pow(g, q, p) != 1:  # 左边用了自己写的模指运算函数，右边用Python自带函数速度快一点
            break
    return p, g
```
### RSA
RSA加解密算法：

![](https://cdn.jsdelivr.net/gh/Country-If/Typora-images/img/20211028165709.png)
### ElGamal
- 准备及生成密钥

![](https://cdn.jsdelivr.net/gh/Country-If/Typora-images/img/20211028170057.png)

构造素数的本原元：[构造一个大素数条件下的本原元（JAVA实现）](https://blog.csdn.net/qq_37685156/article/details/88190088)
- 加密

![](https://cdn.jsdelivr.net/gh/Country-If/Typora-images/img/20211028170104.png)
- 解密

![](https://cdn.jsdelivr.net/gh/Country-If/Typora-images/img/20211028170111.png)
### DH(Diffie-Hellman)
算法：[DH密钥交换](https://blog.csdn.net/chengqiuming/article/details/83002352)
## 程序说明
- python依赖：无
- 程序执行

    可单独执行RSA.py/EIGamal.py/DH.py
  
    或执行main.py通过选择菜单执行不同算法

## 运行结果
- RSA

![](https://cdn.jsdelivr.net/gh/Country-If/Typora-images/img/20211028172352.png)

  从上图可以看出解密结果与原文相同
- ElGamal

![](https://cdn.jsdelivr.net/gh/Country-If/Typora-images/img/20211028172357.png)

  从上图可以看出A、B的解密结果均与原文相同
- DH

![](https://cdn.jsdelivr.net/gh/Country-If/Typora-images/img/20211028172401.png)

  从上图可以看出A、B的计算出的密钥相同