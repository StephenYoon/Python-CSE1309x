# program that asks the user to enter an integer between 1 and 9999 (both inclusive)
# and then prints the input integer using words
def wordmagic(num):
    d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
        6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
        11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
        15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
        19 : 'nineteen', 20 : 'twenty',
        30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
        70 : 'seventy', 80 : 'eighty', 90 : 'ninty' }
    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000

    if (num < 20):
        return d[num]

    if (num < 100):
        if num % 10 == 0: return d[num]
        else: return d[num // 10 * 10] + ' ' + d[num % 10]

    if (num < k):
        if num % 100 == 0: return d[num // 100] + ' hundred'
        else:
            return d[num // 100] + ' hundred ' + wordmagic(num % 100)

    if (num <= 9999):
        if num % k == 0: return wordmagic(num // k) + ' thousand'
        else: return wordmagic(num // k) + ' thousand ' + wordmagic(num % k)

n=int(input('please enter an integer between 1 and 9999: '))
print(wordmagic(n))
