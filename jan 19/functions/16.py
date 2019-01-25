def shut_down(x):
    if x ==  ("yes"):
        print("Shutting down")
    elif x == ("no"):
        print("Shutdown aborted")
    else:
        print("Sorry")
a=str(input("shutdown(yes/no)?"))
shut_down(a)
