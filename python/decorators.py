def announce(f):
    def wrapper():
        print("aboute to run the funciotn...")
        f()
        print("Done with the function")
        return wrapper
