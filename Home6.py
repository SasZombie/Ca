import csv

def case1(first_number:int, seccond_number:int)->int:
    return first_number+seccond_number;

def case2(first_number:int, seccond_number:int)->int:
    return first_number-seccond_number

def case3(first_number:int, seccond_number:int)->int:
    return first_number*seccond_number

def case4(first_number:int, seccond_number:int)->float:
    return first_number/seccond_number

def case5(first_number:int, seccond_number:int)->float:
    return (first_number+seccond_number)/2;

def default(first_number:int, seccond_number:int)->str:
    return "Not a recognisable symbol"

def switch_case(nr1:int, nr2:int, case_value:chr):
    switch_dict = {
        '+': case1,
        '-': case2,
        '*': case3,
        '/': case4,
        '$': case5,
    }
    case_function = switch_dict.get(case_value, default)
    return case_function(nr1, nr2);

def simple_parser(first_number:int, seccond_number:int)->None:
    print(first_number+seccond_number);
    print(first_number-seccond_number);
    print(first_number*seccond_number);
    print(first_number/seccond_number);
    print((first_number+seccond_number)/2);


def complex_parser(first_number:int, seccond_number:int, symbol:chr)->None:
    print(switch_case(first_number, seccond_number, symbol))

def main()->None:
    simple_parser(4, 6);
    complex_parser(2, 3, '+')
    html_content = """
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Document</title>
                </head>
                <body style="background-color:powderblue;">
                    <h2> Ordered List: </h2>
                    
                    <ol>
                """;
    
    file = open('Lab7.csv', 'r')

    csv_reader = csv.DictReader(file);
    for row in csv_reader:
        First_Name = row['FirstName'];
        Last_Name = row['LastName'];
        html_content = html_content + '<li style=\'background-color: lightgray;\'>' + First_Name + ' ' + Last_Name + '</li>\n';
  
    html_content = html_content + '</ol> \n<h2> Unordered List</h2>\n <ul>'

    file.seek(0)
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        Email = row['Email'];
        html_content = html_content + '<li>' + Email + '</li>\n';
               
    html_content = html_content +  """
    
                </ul>
                    
                </body>
                </html>
    """;
    
    
    name=["Alex", "Emma", "Kate", "Ryan", "Lily"]
    age=[21,25,36,31,27]
    
    
    html_content = html_content + """
                <table border = "1">
                <tr>
                    <th> Name </th>
                    <th> Age </th>
                </tr>
    
    """
    
    for i in range(len(age)):
        html_content = html_content + "<tr>\n <td>" + str(name[i]) + "</td>\n <td>" + str(age[i]) + "</td>\n </tr>"
    
    with open('file2.html', 'w') as file2:
        file2.write(html_content)
    
if __name__ == "__main__":
    main()