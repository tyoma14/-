def scope_test():
    def do_local():
        spam = "local spam"

    def def_and_exec_do_nested_nonlocal():
        def do_nested_nonlocal():
            nonlocal spam
            spam = "nested nonlocal spam"
        do_nested_nonlocal()

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


if __name__ == '__main__':
    scope_test()
    print("In global scope:", spam)
