def fizzbuzz_(number):
    if number % 3 == 0:
        return 'Fizz'

    if number % 5 == 0:
        return 'Buzz'


assert fizzbuzz_(3) == 'Fizz'
assert fizzbuzz_(5) == 'Buzz'
