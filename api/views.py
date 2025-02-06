from django.http import response
from django.http import JsonResponse
import requests
import json

from sympy import isprime, is_perfect


def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d**power for d in digits) == n

def classifyNum(request):
    try:
        numParam = request.GET.get("number", "default")
        num = int(numParam)
    except ValueError:
        return response.HttpResponseBadRequest(json.dumps({"number": numParam, "error": True}))
       
    res = requests.get(f"http://numbersapi.com/{num}/math?notfound=floor")
                       
    if num % 2 == 1:
        checkeven = "odd"
    else:
        checkeven = "even"

    if is_armstrong(num):
        props = ["armstrong", checkeven]
    else:
      props = [checkeven]

    mydict = {
        "number": num,
        "is_prime": isprime(num),
        "is_perfect": is_perfect(num),
        "properties": props,
        "digit_sum": sum_of_digits(num),
        "fun_fact": res.text,
    }

    return JsonResponse(mydict)