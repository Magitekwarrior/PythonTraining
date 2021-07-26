temperature = 5

if temperature > 30:
  print('It''s a hot day')           #same block of code
  print('Drink plenty of water')     #same block of code
elif temperature > 20:               # (> 20, < 30)
  print('It''s a nice day')
elif temperature > 10:               # (> 10, < 20)
  print('A bit chilly out.')
else:
 print('Stay indoors. It''s too cold.')
 
print('DONE .. and .. done')