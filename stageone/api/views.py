import math
import requests
from django.http import JsonResponse

def classify_number(request):
    try:
        number = request.GET.get("number")

        if number is None:
            return JsonResponse({
                "number": "alphabet",
                "error": True,
            }, status=400)
        
        n = int(number)
        return JsonResponse({
            "number": n,
            "is_prime": is_prime(n),
            "is_perfect": is_perfect(n),
            "properties": get_properties(n),
            "digit_sum": get_sum(n),
            "fun_fact": get_funfact(n) 
        })


    except ValueError:
        return JsonResponse({
            "number": {n},
            "error": True,
        }, status=400)
    
def is_prime(n):

    # Check if n is 1 or 0
    if n <= 1:
        return False

    # Check if n is 2 or 3
    if n == 2 or n == 3:
        return True

    # Check whether n is divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check from 5 to square root of n
    # Iterate i by (i+6)
    i = 5
    while i <= math.sqrt(n):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

def is_perfect(n):
    n = abs(n)
    """if n < 2:
        return False
    sum = 0
    for i in range(1, math.sqrt(n) + 1):
        if n % i == 0:
            sum += i
            sum += (n / i)
    return sum == n """

    if n < 2:
        return False
    sum = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sum += i
            if (n // i) != i:
                sum += (n // i)
    return sum == n


def get_properties(n):
    n = abs(n)
    sum = 0
    properties = []
    num = list(map(int, str(n)))
    for i in range(len(num)):
        sum += (i ** len(num))
    if sum == n:
        properties.append("armstrong")

    if n % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    
    return properties


def get_sum(n):
    n = abs(n)
    res = sum(int(x) for x in str(n))  
    return res

def get_funfact(n):
    try: 
        response = requests.get(f"http://numbersapi.com/{n}?json")
        data = response.json().get("text")
        return data
    except:
        return("Error with number fact-finding")