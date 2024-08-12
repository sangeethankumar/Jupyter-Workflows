def task_return_true():
    def return_true():
        return True

    return {
        'actions': [return_true]
    }

def task_return_none():
    def return_none():
        return None
    
    return {
        'actions': [return_none]
    }

def task_return_dictionary():
    def return_dict():
        return {
            'return': "Yes"
        }
    
    return {
        'actions': [return_dict]
    }    

def task_return_string():
    def return_str():
        return "Yes"
    
    return {
        'actions': [return_str]
    }      

def task_return_false():
    def return_false():
        return False
    
    return {
        'actions': [return_false]
    }      

def task_raise_exception():
    def raise_exception():
        raise Exception('Nope')
    
    return {
        'actions': [raise_exception]
    }      