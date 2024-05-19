### Testing CEC benchmark 2017 MATLAB version of code 

Testing CEC benchmark 2017 from https://github.com/P-N-Suganthan/CEC2017-BoundContrained 

The codes could be found in https://github.com/P-N-Suganthan/CEC2017-BoundContrained/blob/master/codes.rar 

The raw codes were taken there and modified for testing purposes.

### Running the tests

To run tests check combine-dim-func.py where you set number of functions i, dimensions j, and number of element k.

It would be required to run with matlab engine which is compatible currently with python 3.11, check documentation at https://www.mathworks.com/support/requirements/python-compatibility.html

For manual testing check run-tests.py. It is possilbe to run this script with arguments number of function, dimension and number of element.

### Results

Results are find in test_data/result

For graphs and comparisons check C version of the code at https://github.com/FrostNiles/CEC-benchmark-testing-2017-C

### portability

It is possilbe to run all the tests in different years, just check the years documentation, change mains so it writes results in appropriate files.

Change the precission - it is now to 10e-08 in every document, it is possilbe to change it globally one day not now. (seven digits now in scripts.py and 9 floating point numbers in mains)

First try run-tests.py for single element few times.

Lastly change the combine-dim-func.py so you can run it automatically for the years functions.

