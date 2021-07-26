weight = float(input('Enter your Weight: '))

weightUnit = input('(K)g or (L)bs: ')

if (weightUnit.upper() == 'K'):
  converted = weight * 0.45359237
  print('Weight in Kg: ', converted)
elif (weightUnit.upper() == 'L'):
  converted = weight / 0.45359237
  print('Weight in Lbs: ', converted)
else:
  print('Invalid option')