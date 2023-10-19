def curry_explicit(function, arity):
    if arity < 0:
        raise ValueError("arity cannot be negative")
    elif arity == 0:
        return function

    def curry(arguments):
        if len(arguments) == arity:
            return function(*arguments)

        def accept_new_argument(new_argument):
            return curry([*arguments, new_argument])

        return accept_new_argument

    return curry(arguments=[])


def uncurry_explicit(function, arity):
    if arity < 0:
        raise ValueError("arity cannot be negative")

    def accept_arguments(*args):
        if arity != len(args):
            raise ValueError("incorrect arity")
        if arity == 0:
            return function()
        result = function(args[0])
        for i in range(1, arity):
            result = result(args[i])
        return result

    return accept_arguments
