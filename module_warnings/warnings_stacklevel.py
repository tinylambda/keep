import warnings


def old_function():
    warnings.warn('old_function() is depreciated, use new_function()', stacklevel=2)


def caller_of_old_function():
    old_function()


caller_of_old_function()

