import re
from datetime import datetime
def print1(s):
    y = re.findall(r'(?=.*[a-zA-Z])(?=.*\d)(?=.*\*)[a-zA-Z0-9*]+', s);
    print(y);

def print2(s):
    y = re.findall(r'[A-Z]+_[a-z]+', s);
    print(y);

def print3(s):
    y = re.findall(r'm[A-Za-z][A-Za-z][A-Za-z]n', s)
    print(y);

def print4(s):
    y = re.findall(r'm[A-Za-z][A-Za-z][A-Za-z]n', s)
    print(y);

def print5(s):
    y = re.findall(r'(\b[hH][iI]{2,3}[A-HJ-Za-hj-z]\w*)', s)
    print(y)

def print6(s):
    y = re.findall(r'\w+q\w+', s)
    print(y)

def print7(s:str):
    s = s.replace('a', 'u')
    s = s.replace('e', 'i')
    print(s)

def main():
    print1("Buna1* aaa");
    print2("FILS_student mama mea 123");

    s1 = "rectangle square sphere triangle cone cube cylinder 1"
    print(re.findall(r'\w*re\W|\w*le\W', s1));

    print(re.findall(r'[A-Z] | [0-9]', s1));

    s1 = "2021/10/27 black as Black";
    year, month, day = re.match(r'(\d{4})/(\d{2})/(\d{2})', s1).groups();
    
    date = datetime.strptime(f'{year}-{month}-{day}', '%Y-%m-%d')

    new_time = date.strftime('%d-%B-%Y')

    print(new_time);

    print3("aaa migan")
    print5("Hiiia")

    print6("aaqaa qaaq")

    print7("ei")


if __name__ == '__main__':
    main();