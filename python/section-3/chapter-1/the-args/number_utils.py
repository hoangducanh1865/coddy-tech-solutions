def sum_all_numbers(*args):
    if not args:
        return 0
    
    for arg in args:
        # if isinstance(arg, bool) or not isinstance(arg, (int, float)):
        if type(arg) == bool or (type(arg) != int and type(arg) != float):
            print("Error: All arguments must be numbers")
            return None
    
    return sum(args)