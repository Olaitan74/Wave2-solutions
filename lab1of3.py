# Use this playground to experiment with list methods, using Test Run

car_brands = ['Honda', 'Toyota', 'Lexus', 'Benz', 'Ford', 'Volkswagen', 'Peugeot', 'Innoson', 'Ferrari', 'Lamborghini',
              'Acura']

print('1. ', car_brands, '\n')

print('2. ', '\n'.join(car_brands), '\n')

print('3. ', car_brands.count('Lexus'), '\n')

more_brands = ['BMW', 'Volvo']
car_brands.extend(more_brands)
print('4. ', car_brands, '\n')

car_brands.insert(5, 'Rolls royce')
print('5. ', car_brands, '\n')

print('6. ', car_brands.pop(6), '\n')

car_brands.remove('Ford')
print('7. ', car_brands, '\n')

car_brands.reverse()
print('8. ', car_brands, '\n')

car_brands.sort()
print('9. ', car_brands)


