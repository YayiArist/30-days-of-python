#'Day 2: 30 Days of python programming'

firstname = "yairys"
lastname = "Aristigueta"
fullname = firstname, lastname
country = "Argentina"
city = "Buenos Aires"
age = 32
year = 2022
is_false= False
is_married = is_false
is_true= True
is_light_on= False
date, hour, adress = "25 de agosto", "3pm", "los picachos"
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'yairys', 
    'lastname':'Aristigueta', 
    'country':'Venezuela',
    'city':'Caracas'
    }

#level 2
print( type(firstname))
print( type(fullname))
print( type(age))
print( type(is_false))
print("first name length:", len(firstname))
print(skills)
print(type(skills))
print(type(person_info))
print("hola" + str(5))
print("hola " * 5)
print(len(firstname)==len(lastname))
print(len("hola") >= len("persona")) #false cuenta caracteres
print("aaaa">= "abaa") # false => ordenacion alfabetica


num_one = 5
num_two = 4

total= num_one+num_two
diff= num_one-num_two
product = num_two * num_one
division = num_one - num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two


print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', division)
print('remainder: ', remainder)

name = input( "what's your name?" ) 
print(name)