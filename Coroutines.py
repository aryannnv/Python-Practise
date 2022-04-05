def searcher():
    import time
    book="My name is Aryan Verma"
    time.sleep(4)

    while True:
        txt=(yield)
        if txt in book:
            print("Text has been found")
        else:
            print("Text has not been found")

sea=searcher()
print("Starting now")
next(sea)
print("The program has started")
sea.send("Aryan")
sea.send("Bund")
sea.close()