
def fibonacci(num):
    num1, num2, num3, series_list = 0, 1, 0,[]
    for i in range(num+1):
        series_list.append(num3)
        num1 = num2
        num2 = num3
        num3 = num1 + num2
    return(series_list[-1])


def lucas (num , num1 = 2 ,num2 = 1):
    series_list = [num1,num2]
    for i in range(num):
        num3 = num1 + num2
        series_list.append(num3)
        num1 = num2
        num2 = num3
    return(series_list[num])

def sum_series (num,first_value = 2 , second_value = 1):
    fibonacci_result = fibonacci(num)
    luces_result =  lucas (num , num1 = first_value ,num2 = second_value)
    return {'fibonacci_result':fibonacci_result,'luces_result':luces_result}

if __name__ == "__main__":
    print('Ente the number "n" to return the nth value in the fibonacci and lucas series:')
    num = int(input('> ')) 
    result = sum_series(num)
    print(f'The {num}th number in the fibonacci series is {result["fibonacci_result"]}')
    print(f'The {num}th number in the lucas series is {result["luces_result"]}')

 



