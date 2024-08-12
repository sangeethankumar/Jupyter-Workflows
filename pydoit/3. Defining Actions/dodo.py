def task_simple_action():
    def simple_action():
        with open('simple.txt', 'w') as f:
            f.write('simple')
        
    return {
        'actions': [simple_action]
    }

def task_args_action():
    def args_action(a, b):
        with open('args.txt', 'w') as f:
            f.write(f'a={a}, b={b}')

    return {
        'actions': [(args_action, [3, 5])]
    }

def task_kwargs_action():
    def kwargs_action(a, b):
        with open('kwargs.txt', 'w') as f:
            f.write(f'a={a}, b={b}')

    return {
        'actions': [(kwargs_action, [], {
            'a': 3,
            'b': 5
        })]
    }

def task_args_kwargs_action():
    def args_kwargs_action(a, b, c=10, d=11):
        with open('args_kwargs.txt', 'w') as f:
            f.write(f'a={a}, b={b}, c={c}, d={d}')

    return {
        'actions': [(args_kwargs_action, [3, 5], {
            'c': 7,
            'd': 9
        })]
    }