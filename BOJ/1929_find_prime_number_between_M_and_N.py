import sys
sys.stdin = open('input_1929.txt','r')

m,n = map(int,input().split())

def find_prime_number(m,n):
    prime_number= []
    result_array = []
    for num in range(2,n+1):
        for i in prime_number:
            if num % i == 0 and i*i <= n:
                break
        else:
            prime_number.append(num)
            if num >= m:
                result_array.append(num)
    return result_array

def find_prime_list_under_number(m,number):
    all_numbers = [True]*(number+1)
    answer = []

    for index in range(2,number+1): # n <- 2 ~ num
        # 소수인지 아닌지 판별해야 한다.
        if all_numbers[index]:
            for index2 in range(2,number//index+1):
                all_numbers[index*index2] = False
    for index,num in enumerate(all_numbers):
        if index> 1 and index >= m and num:
            answer.append(index)

    return answer

# result = find_prime_number(m,n)
result = find_prime_list_under_number(m,n)
for ele in result:
    print(ele)