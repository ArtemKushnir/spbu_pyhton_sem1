def curry_explicit(function, arity):
    f_args = []

    def accept_arguments(args):
        nonlocal f_args
        if arity < 0:
            return "arity cannot be negative"
        elif arity == 0:
            return function()
        else:
            while True:
                f_args += [args]
                if len(f_args) == arity:
                    return function(*f_args)
                return accept_arguments

    return accept_arguments


def uncurry_explicit(function, arity):
    result = []

    def accept_arguments(*args):
        nonlocal result
        if arity < 0:
            return "arity cannot be negative"
        elif arity != len(args):
            return "incorrect arity"
        else:
            for i in args:
                result += [function(i)]
            return function(*result)

    return accept_arguments
