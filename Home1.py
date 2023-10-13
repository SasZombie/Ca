def fibb(x) -> None:
    step = 0
    privious = 1
    for i in range(x):
        print(step)
        q = step
        step+=privious
        privious = q

def cmmdc(x, y) -> None:
    while x != 0:
        r = y % x;
        y = x
        x = r
    print(y)
    

def cmmmc(a, b) -> None:

    x = a
    y = b

    while x != y:
        if x < y:
            x = x + a
        else:
            y = y + b
    print(x)

def get_even_and_odd_list(x: list) -> tuple:
    
    list_even = []
    list_odd = []

    for i in x:
        if i % 2 == 0:
            list_even.append(i)
        else:
            list_odd.append(i)

    return list_even, list_odd


class Cube:

    length_of_side: int;

    def __init__(self, x: int) -> None:
        self.length_of_side = x
    
    def area(self) -> int:
        return self.length_of_side * self.length_of_side
    
    def area_of_all(self) -> int:
        return 6 * self.area();

    def volume(self) -> int:
        return self.area() * self.length_of_side


if __name__ == "__main__":
    #Ex 1
    nr_of_fibbs = int(input())
    fibb(nr_of_fibbs)

    #Ex2

    nr_of_cmm0 = int(input())
    nr_of_cmm1 = int(input())

    cmmmc(nr_of_cmm0, nr_of_cmm1);
    #Ex 3

    cmmmc(nr_of_cmm0, nr_of_cmm1);

    #Ex 4

    list_ex = [1, 2, 3, 4, 5, 6]

    list_even, list_odd = get_even_and_odd_list(list_ex);

    print(list_even);
    print(list_odd)
    #Ex 5
    new_cube = Cube(3)

    print(new_cube.area())
    print(new_cube.area_of_all())
    print(new_cube.volume())
    #Ex 6
    power = int(input())
    exponent = int(input())

    get_power = lambda x, y : x**y

    print(get_power(power, exponent))
