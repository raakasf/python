def foo():
    try:
        1 / 0
    except ZeroDivisionError:
        return 1
    # The finally block is always executed, whether or not an exception was raised or handled. In this case, even though return 1 was about to return from the except block, the finally block overrides it because a return statement in the finally block always takes precedence.
    finally:
        return 2


print(foo())
