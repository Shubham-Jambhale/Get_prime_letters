def count_prime_letters(num):
    prime_words ={2:"two",3:"three",5:"five",7:"seven",11:"eleven",13:"thirteen",17:"seventeen",19:"nineteen",23:"twentythree",29:"twentynine",31:"thirtyone",37:"thirtyseven",41:"fortyone",
                  43:"fortythree", 47 :"fortyseven",53:"fiftythree",59:"fiftynine",61:"sixtyone",67:"sixtyseven",71:"seventyone",
                  73:"seventythree",79:"seventynine",83:"eightythree",89:"eightynine",97:"nientyseven"}   
    prime_numbers=[]
    for i in range(0,num):
        if i > 1:
            for j in range(2,i):
                if i % j == 0:
                    break;
            else:
                prime_numbers.append(i)
    count = 0
    #print(prime_numbers)
    for x in prime_numbers:
        len_p=prime_words[x]
        count += len(len_p)
    #print(count_prime)
    return count