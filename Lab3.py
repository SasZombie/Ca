import re

def start_with(s):
    y = re.findall(r'(\b[tT]\w*[sS][eE]\b)', s);
    print(y)

def start_with2(s):

    y = re.findall(r'(\b[mM]\w*.{3}[nN]\b)', s);
    print(y)

def start_with3(s):

    y = re.findall(r'(\b[hH][iI]{2,3}[A-HJ-Za-hj-z]\w*)', s)
    print(y)

def start_with4(s):
    y = re.findall(r'[Qq]\B\w*|\B\w*[Qq]', s)
    print(y)


def start_with5(s):
    y = re.findall(r'\w*\B[Qq]\B\w*', s)
    print(y)

def start_with6(s:str):
    s = s.replace('a', 'u')
    s = s.replace('e', 'i')
    print(s)


def main():
    string = "example@gmail.com example2@yahoo.com example3@outlook.com example4yahoo.com example5gmail.com"

    y = re.findall(r'(\w+@)', string)
    x = re.findall(r'\w+\b@\w+.\w+', string)
    z = re.findall(r'(\w+)@', string)

    print(y);
    print(x);
    print(z);

    string2 = "car, cat, dog, pool, bath, cone, cube, ring, int"
    
    y = re.findall(r'\w{4}' , string2)
    print(y)


    list1 = ["square","triangle","cube","sphere","circle","pentagon", "hexagon", "rectangle","parallelogram","trapezoid"]
    geo="A square has 4 sides, a triangle has 3, a pentagon has 5, a hexagon has 6. While a square has 4 equal sides, a triangle can have 0, 2 or 3 equal sides."

    for i in list1:
        # y = re.findall(r'\w+re\Z', i)
        # if y:
        #     print(y)
        
        y = re.findall(i, geo)
        if y:
            print(y)

    x = re.findall(r'\d+\W', geo)
    print(x)
    
    start_with("These")
    start_with2("maaan")
    start_with3("hiiia")
    start_with4("qaaaq");
    start_with5("aaaqaaa")
    start_with6("ae")




if __name__ == '__main__':
    main();