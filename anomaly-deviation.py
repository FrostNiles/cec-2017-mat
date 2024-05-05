import sys
import runpy
import re
from start_matlab import start_engine
from run_matlab import run_main
from end_matlab import end_engine
# Read the numbers from the file

argNum = sys.argv[1]
dimension = sys.argv[2]
number_of_element = int(sys.argv[3]) - 1

with open(f'test_data/result/result_data_{argNum}_dim_{dimension}_number_of_element_{number_of_element+1}.txt', 'r') as file:
    lines = file.readlines()
print("lines", lines)
if len(lines) < 3:
    raise Exception("Stopping execution of anomaly-deviation.py because the number of lines in the file is less than 3.")
# Extract the numbers from the lines
number1 = float(lines[1])
number2 = float(lines[2])

# Calculate the deviation
deviation = abs(number1 - number2)
print("deviation", deviation)

#now I want to test the deviation with the original data
# Read the original numbers

with open(f'input_data/shift_data_{argNum}.txt', 'r') as file:
    original_data = file.read()

original_numbers = [float(i) for i in original_data.split()]

original_numbers[number_of_element] = original_numbers[number_of_element] - deviation

with open(f'test_data/shift_data_{argNum}.txt', 'w') as file:
    for number in original_numbers:
        file.write(f"{number} ")


run_main(eng)

with open(f'test_data/current_result_{argNum}.txt', 'r') as file:
    result = file.read()

# Find the number in the string
result = re.findall(r'\d+\.\d+', result)

# Keep the number as a string to preserve trailing zeroes
number_string = result[0]
# Convert to float when you need to do a numerical operation

result = str(result)
result = result.split('.')
#before the floating point
before = result[0]
#after the floating point
after = result[1]

# Now I want to get the first 8 digits from after
eightDigits = after[:8]
#this is how the ["['3000", "0000000053']"] looks like
#I want to get the last two digits from the after
# and im getting  "']" so I need to get the last two digits from the after
lastTwoDigits = after.split('\'')[0][-2:]
lastDeviation = str(deviation)

if int(eightDigits) > 0:

    while int(eightDigits) != 0:
        # I have this number 4.881784197001252e-16 in deviation and it is float and I want to subtract 1 from it (I mean like 3.881784197001252e-16)
        # I want to convert it to string and then I want to subtract 1 from it
        backup_deviation = deviation
        deviation = str(deviation)
        deviation = deviation.split('.')
        #before the floating point
        deviation_before = deviation[0]
        #after the floating point
        deviation_after = deviation[1]
        deviation[0] = str(int(deviation_before) - 1)
        deviation[1] = deviation_after
        deviation = '.'.join(deviation)
        deviation = float(deviation)
        
        original_numbers = [float(i) for i in original_data.split()]

        original_numbers[number_of_element] = original_numbers[number_of_element] - deviation

        with open(f'test_data/shift_data_{argNum}.txt', 'w') as file:
            for number in original_numbers:
                file.write(f"{number} ")


        run_main(eng)

        with open(f'test_data/current_result_{argNum}.txt', 'r') as file:
            result = file.read()

        # Find the number in the string
        result = re.findall(r'\d+\.\d+', result)

        # Keep the number as a string to preserve trailing zeroes
        number_string = result[0]
        # Convert to float when you need to do a numerical operation

        result = str(result)
        result = result.split('.')
        #before the floating point
        before = result[0]
        #after the floating point
        after = result[1]

        # Now I want to get the first 8 digits from after
        eightDigits = after[:8]
        lastTwoDigits = after.split('\'')[0][-2:]
        lastDeviation = str(deviation)
        
else:
    if int(lastTwoDigits) < 96:
        while int(eightDigits) == 0 and int(lastTwoDigits) < 96:
            backup_deviation = deviation
            deviation = str(deviation)
            deviation = deviation.split('.')
            #before the floating point
            deviation_before = deviation[0]
            #after the floating point
            deviation_after = deviation[1]
            deviation[0] = str(int(deviation_before) + 1)
            deviation[1] = deviation_after
            deviation = '.'.join(deviation)
            deviation = float(deviation)
            
            
            original_numbers = [float(i) for i in original_data.split()]

            original_numbers[number_of_element] = original_numbers[number_of_element] - deviation

            with open(f'test_data/shift_data_{argNum}.txt', 'w') as file:
                for number in original_numbers:
                    file.write(f"{number} ")


            run_main(eng)

            with open(f'test_data/current_result_{argNum}.txt', 'r') as file:
                result = file.read()

            # Find the number in the string
            result = re.findall(r'\d+\.\d+', result)

            # Keep the number as a string to preserve trailing zeroes
            number_string = result[0]
            # Convert to float when you need to do a numerical operation

            result = str(result)
            result = result.split('.')
            #before the floating point
            before = result[0]
            #after the floating point
            after = result[1]

            # Now I want to get the first 8 digits from after
            eightDigits = after[:8]
            lastTwoDigits = after.split('\'')[0][-2:]
            

middle = (backup_deviation + deviation) / 2
original_numbers = [float(i) for i in original_data.split()]
 
original_numbers[number_of_element] = original_numbers[number_of_element] - middle
 
with open(f'test_data/shift_data_{argNum}.txt', 'w') as file:
    for number in original_numbers:
        file.write(f"{number} ")


run_main(eng)

with open(f'test_data/current_result_{argNum}.txt', 'r') as file:
        result = file.read()

# Find the number in the string
result = re.findall(r'\d+\.\d+', result)

# Keep the number as a string to preserve trailing zeroes
number_string = result[0]
# Convert to float when you need to do a numerical operation

result = str(result)
result = result.split('.')
#before the floating point
before = result[0]
#after the floating point
after = result[1]

# Now I want to get the first 8 digits from after
eightDigits = after[:8]

lastTwoDigits = after.split('\'')[0][-2:]

counter = 0

while int(eightDigits) != 0 or int(lastTwoDigits) < 96:
    if int(eightDigits) != 0:
        backup_deviation = middle
    else:
        if int(lastTwoDigits) < 96:
            deviation = middle
        else:
            print("eightDigits is equal to 0 and lastTwoDigits is greater than 96")
    middle = (backup_deviation + deviation) / 2
    original_numbers = [float(i) for i in original_data.split()]

    original_numbers[number_of_element] = original_numbers[number_of_element] - middle
 
    with open(f'test_data/shift_data_{argNum}.txt', 'w') as file:
        for number in original_numbers:
            file.write(f"{number} ")

    

    with open(f'test_data/current_result_{argNum}.txt', 'r') as file:
            result = file.read()

    # Find the number in the string
    result = re.findall(r'\d+\.\d+', result)

    # Keep the number as a string to preserve trailing zeroes
    number_string = result[0]
    # Convert to float when you need to do a numerical operation

    result = str(result)
    result = result.split('.')
    #before the floating point
    before = result[0]
    #after the floating point
    after = result[1]
    counter += 1

    # Now I want to get the first 8 digits from after
    eightDigits = after[:8]
    lastTwoDigits = after.split('\'')[0][-2:]
    
    if deviation == backup_deviation:
        deviation = lastDeviation
        with open(f'test_data/result/result_data_{argNum}_dim_{dimension}_number_of_element_{number_of_element+1}.txt', 'w') as file:
            file.write("deviation:")
            file.write(deviation)
        raise Exception("Stopping execution of anomaly-deviation.py because the deviation is the same as the backup deviation.")
    if int(eightDigits) == 0:
        lastDeviation = str(middle)
    if int(eightDigits) == 0 and counter >= 50:
        deviation = str(middle)
        with open(f'test_data/result/result_data_{argNum}_dim_{dimension}_number_of_element_{number_of_element+1}.txt', 'w') as file:
            file.write("deviation:")
            file.write(deviation)
        raise Exception("Stopping execution of anomaly-deviation.py because the deviation is the same as the backup deviation.")
    elif counter >= 100:
        deviation = lastDeviation
        with open(f'test_data/result/result_data_{argNum}_dim_{dimension}_number_of_element_{number_of_element+1}.txt', 'w') as file:
            file.write("deviation:")
            file.write(deviation)
        raise Exception("Stopping execution of anomaly-deviation.py because the counter is greater than or equal to 100.")

deviation = str(middle)
with open(f'test_data/result/result_data_{argNum}_dim_{dimension}_number_of_element_{number_of_element+1}.txt', 'w') as file:
            file.write("deviation:")
            file.write(deviation)