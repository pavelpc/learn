# константы
actions = ["buy", "fill", "take", "remaining", "exit"]
coffees = ['espresso', 'latte', 'cappuccino']
buy = 0
sort = 0
fill = 0
add_water = 0
add_milk = 0
add_coffee = 0
add_cups = 0
water = 0
milk = 0
coffee = 0
money = 0
dcups = 1
# имеется:
water_in = 400
milk_in = 540
coffee_in = 120
money_in = 550
cups_in = 9


# считаем
# need_coffee = need_cups * coffee
# need_milk = need_cups * milk
# need_water = need_cups * water


# операции
def for_coffee() :
	global sort, water, milk, coffee, money, dcups
	if sort == 'espresso' :
		water = 250
		milk = 0
		coffee = 16
		money = 4
		dcups = 1
	elif sort == 'latte' :
		water = 350
		milk = 75
		coffee = 20
		money = 7
		dcups = 1
	elif sort == 'cappuccino' :
		water += 200
		milk = 100
		coffee = 12
		money = 6
		dcups = 1


m = 0


def check_needs() :
	global m
	e_water = water_in // water
	if milk != 0 :
		e_milk = milk_in // milk
	else:
		e_milk = 1
	e_coffee = coffee_in // coffee
	e_money = money_in // money
	e_dcups = cups_in // dcups
	engredients = [e_milk, e_water, e_coffee, e_dcups]
	cofcups = min(engredients)
	if cofcups >= 1 :
		print('I have enough resources, making you a coffee!')
	elif cofcups < 1 :
		if e_coffee == 0 :
			print('Sorry, not enough coffee!')
			m = 1
		if e_dcups == 0 :
			print('Sorry, not enough disposable cups!')
			m = 1
		if e_milk == 0 :
			print('Sorry, not enough milk!')
			m = 1
		if e_water == 0 :
			print('Sorry, not enough watter!')
			m = 1
	return m


def make_coffee() :
	global water, milk, coffee, money, dcups, water_in, milk_in, coffee_in, money_in, cups_in, m
	if m == 0 :
		water_in -= water
		milk_in -= milk
		coffee_in -= coffee
		cups_in -= dcups
		money_in += money
	return


# print('The coffee machine has:')
# print(water_in, 'of water')
# print(milk_in, 'of milk')
# print(coffee_in, 'of coffee beans')
# print(cups_in, 'of disposable cups')
# print('$', money_in, 'of money')
# работаем

a = 0
while a == 0 :
	action = input('Write action (buy, fill, take, remaining, exit):')
	m = 0
	if action != actions[4] :
		if action == actions[0] :
			buy = (input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:'))
			if buy == '1' :
				sort = coffees[0]
				for_coffee()
				check_needs()
				if m == 0 :
					make_coffee()
			elif buy == '2' :
				sort = coffees[1]
				for_coffee()
				check_needs()
				if m == 0 :
					make_coffee()
			elif buy == '3' :
				sort = coffees[2]
				for_coffee()
				check_needs()
				if m == 0 :
					make_coffee()
		elif action == actions[1] :
			add_water = int(input('Write how many ml of water do you want to add:'))
			add_milk = int(input('Write how many ml of milk do you want to add:'))
			add_coffee = int(input('Write how many grams of coffee beans do you want to add:'))
			add_cups = int(input('Write how many disposable cups of coffee do you want to add:'))
			water_in += add_water
			milk_in += add_milk
			coffee_in += add_coffee
			cups_in += add_cups
		elif action == actions[2] :
			print('I gave you $', money_in)
			money_in = 0
		elif action == actions[3] :
			print('The coffee machine has:')
			print(water_in, 'of water')
			print(milk_in, 'of milk')
			print(coffee_in, 'of coffee beans')
			print(cups_in, 'of disposable cups')
			print('$', end='')
			print(money_in, 'of money')
	else :
		exit()

#
# have_water = int(input('Write how many ml of water the coffee machine has:'))
# have_milk = int(input('Write how many ml of milk the coffee machine has:'))
# have_coffee = int(input('Write how many grams of coffee beans the coffee machine has:'))
# что хотим
# need_cups = int(input('Write how many cups of coffee you will need:'))
# расчитываем потребности
# print('For',need_cups, 'cup(s) of coffee you will need:')

# print(need_water, 'ml of water')

# print(need_milk, 'ml of milk')

# print(need_coffee, 'g of coffee beans')
# чтомогу


# engredients = [e_milk, e_water, e_coffee]
# cups = min(engredients)
# print(engredients)
# print('may', cups)
# if cups < need_cups:
#    print('No, I can make only',  cups, 'cup(s) of coffee')
# elif cups == need_cups:
#    print('Yes, I can make that amount of coffee')
# elif cups > need_cups:
#    print('Yes, I can make that amount of coffee(and even ', cups - need_cups, 'more than that')


# print('Starting to make a coffee')
# print('Grinding coffee beans')
# print('Boiling water')
# print('Mixing boiled water with crushed coffee beans')
# print('Pouring coffee into the cup')
# print('Pouring some milk into the cup')
# print('Coffee is ready!')
