def ft_filter(function, iterable):
    """
        reproduction of built-in filter function
    """
    if function is None:
        return [x for x in iterable if x]
    return [x for x in iterable if function(x)]
