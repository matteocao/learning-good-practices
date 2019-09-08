def hello_world(name):
    """
    Print `name` for greetings
    Args:
        name (str): your name
    Returns:
        None
    """
    if not isinstance(name,str):
        raise TypeError("The varaible 'name' is not a str")
    print("Hello " + name + ".")