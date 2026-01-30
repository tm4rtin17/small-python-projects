import pyinputplus as pyip 

#user prompt to choose conversion method
choice = pyip.inputMenu(['Celcius -> Farenheit', 'Farenheit -> Celcius'], numbered=True)

if choice == 'Celcius -> Farenheit':
    temp_c = pyip.inputNum('Enter a number to convert to Farenheit. ')
    temp_f = (temp_c * 1.8) + 32
    print(f'{temp_c}C converts to {temp_f}F.')
else:
    temp_f = pyip.inputNum('Enter a number to convert to Celcius. ')
    temp_c = (temp_f - 32) / 1.8
    print(f'{temp_f}F converts to {temp_c}C.')