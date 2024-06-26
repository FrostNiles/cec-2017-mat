import runpy
import re
import sys
import matlab.engine

skipped = [2, 9]
eng = matlab.engine.start_matlab()
for i in range(1, 31):
    # CEC 2022 has 12 functions
    if i in skipped:
        continue
    for j in [10, 30, 50, 100]:
        for k in range(1, j+1):
            args = {
                'arg1': str(i),
                'arg2': str(j),
                'arg3': str(k),
                'eng': eng,
            }
            try:
                runpy.run_path('./run-tests.py', init_globals=args)
            except Exception as e:
                print('Error:', e)
                continue


eng.quit()