emails=['me@gmail.com', 'you@hotmail.com', 'they@gmail.com']
for email in emails:
    #print(email)
    if 'gmail' in email:
        print(email)


#fun currency converter
def currency_converter(rate, currency):
    dollars = rate * currency
    return dollars
r = input("Enter rate: ")
c = input("Enter currency: ")
print(currency_converter(float(r), float(c)))

#while loops
password=''
while password != 'python123':
    password = input("Enter password: ")
    if password == 'python123':
        print("You are logged in.")
    else:
        print("Sorry try again")

names=['james', 'john', 'jack']
email_domains=['gmail', 'hotmail', 'yahoo']

for i,j in zip(names, email_domains):
    print(i, j)
