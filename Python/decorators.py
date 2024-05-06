def announce(f):
    # So wrapper function a basically a fucntion wrapping another funtionthat is modifies it.
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("Hello World!")

hello()