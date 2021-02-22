from random import sample

from django.shortcuts import render

class SecretNumbers:
    def generate_numbers(n):
        numbers = range(0,9)
        return sample(numbers, n)

numbers = SecretNumbers
secret_numbers = numbers.generate_numbers(4)

def guess_numbers(secret, actual):
    guessed_bulls = 0
    guessed_cows = 0
    for i in actual:
        if len(str(i)) != 1:
            context = {
                'result': 'Numbers must be less than 10!'
            }
    if secret == actual:
        context = {'result': 'You got it right!!!'}
    elif len(actual) != 4:
        context = {'result': 'Enter only 4 numbers!!!'}
    else:
        for i in range(len(secret)):
            for num in range(len(actual)):
                if secret[i] == actual[num]:
                    if i == num:
                        guessed_bulls += 1
                    else:
                        guessed_cows += 1
        context = {'result': f'Bulls: {guessed_bulls}, Cows: {guessed_cows}'}
    return context

def index_view(request):
    if request.method == 'GET':
        return render(request,'index.html')
    elif request.method == 'POST':
        try:
            numbers = list(map(int, request.POST.get('numbers').split(' ')))
            result = guess_numbers(secret_numbers, numbers)
            print(numbers)
            print(secret_numbers)
        except ValueError:
            result = {'result': 'Enter only numbers separated with only one space!!!'}
        except KeyError:
            result = {'result': 'Enter numbers'}
        return render(request, 'index.html', result)


# Create your views here.
