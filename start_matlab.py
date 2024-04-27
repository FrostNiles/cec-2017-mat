import matlab.engine

def start_engine():
    eng = matlab.engine.start_matlab()
    return eng