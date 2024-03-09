import logging


counter = 0
log = logging.getLogger('uvicorn')

def test():
    global counter
    print(f'Test task with counter: {counter}')
    counter += 1
