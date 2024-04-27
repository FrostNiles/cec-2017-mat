import sys
import matlab.engine
from start_matlab import start_engine

def run_main(eng):
    try:
        func_num = matlab.double([int(sys.argv[1])])
        dimension = matlab.double([int(sys.argv[2])])
        eng.main(func_num, dimension, nargout=0)
    except Exception as e:
        print(f"An error occurred: {e}")