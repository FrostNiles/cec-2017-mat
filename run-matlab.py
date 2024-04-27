import matlab.engine
import sys

# Start MATLAB engine
eng = matlab.engine.start_matlab()

try:
    # Call your MATLAB function
    func_num = matlab.double([int(sys.argv[1])])
    dimension = matlab.double([int(sys.argv[2])])

    eng.main(func_num, dimension, nargout=0)

finally:
    # Close MATLAB engine
    eng.quit()