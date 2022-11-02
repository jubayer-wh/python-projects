


#########################

for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()

############another

teams = ['Argentina', 'Brazil', 'Italy', 'Japan', 'Germany', 'Estonia']
for home_team in teams:
    for away_teams in teams:
        if home_team != away_teams:
            print(home_team + " VS " + away_teams)

############another2
number = 1
while number <= 7:
    print(number, " ")
    number += 1


############another3

def show_letters(word):
    for letter in word:
        print(letter)
show_letters("JUBAYER")

############another4

def digits(n):
    count = 0
    if n == 0:
        return 1
    while (n >= 1):
        count += 1
        n = n / 10
    return count

print(digits(25))
print(digits(10087))

############another4

def multiplication_number(start, stop):
    for x in range(start, stop+1):
        for y in range(start, stop+1):
            print(str(x*y), end=" ")
        print()
multiplication_number(1, 4)

############another5

def counter(start, stop):
    x = start
    if start > stop:
        return_string = "Counting down: "
        while x >= stop:
            return_string += str(x)
            if x > stop:
                return_string += ","
            x -= 1
    else:
        return_string = "Counting up: "
        while x <= stop:
            return_string += str(x)
            if x < stop:
                return_string += ","
            x += 1
    return return_string
print(counter(1, 10))
print(counter(2, 1))
print(counter(5, 5))

############another6
def even_numbers(maximum):
	return_string = ""
	for x in [num for num in range(1, maximum+1) if num % 2 == 0]:
		return_string += str(x) + " "
	return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed


############another7
def decade_counter():
	while year < 50:
		year += 10
	return year

#####################8
for x in range(1, 10, 3):
    print(x)

##################9
    def votes(params):
        for vote in params:
            print("Possible option:" + vote)

###########################10
def double_word(word):
    return word + word +str(2*len(word))
print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0

##################11

def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

##############
" yes ".strip()
