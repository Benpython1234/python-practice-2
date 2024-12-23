print('/n Enter player name: ') # player1
player1=input('What player is it: ') # string data type
age1=int(input('what is age: ')) # integer data type
height1=float(input('what is height: ')) #float data type 
Position1=input('what postion: ') #string data type 
is_captian1=input('is the player a captian: ').lower()=="yes"

print('/n Enter player name: ')
player2=input('What player is it: ')
age2=int(input('what is age: '))
height2=float(input('what is height: '))
Position2=input('what postion: ')
is_captian2=input('is the player a captian: ').lower()=="yes"

print(f'first player is {player1} and his age is {age1} his height is {height1} and he plays {Position1}and he is a {is_captian1}')

print(f'first player is {player2} and his age is {age2} his height is {height2} and he plays {Position2}and he is a {is_captian2}')

print("\n predict salary based on experience")
years_of_experience=float(input('years of expereince: '))
current_salary=float(input('your current salary: '))
expected_salary_rate=float(input('Enter expexted salary rate per year (in %)'))
predicted_salary=current_salary*(1+expected_salary_rate/(100))**(years_of_experience)
print(predicted_salary)


