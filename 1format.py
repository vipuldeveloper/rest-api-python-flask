import datetime
import calendar

greeting = "Hello, {}. Today is {}"

greeting_to_vipul = greeting.format("Vipul", datetime.datetime.today().strftime('%A'))

print(greeting_to_vipul)