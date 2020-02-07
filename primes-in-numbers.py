def primeFactors(n):
    divisor = 1
    result = ''
    while n > 1:
        count = 0
        divisor += 1
        while n % divisor == 0:
            n /= divisor
            count += 1
        if count == 1:
            result += '({0})'.format(divisor)
        elif count > 1:
            result += '({0}**{1})'.format(divisor, count)
    return result
