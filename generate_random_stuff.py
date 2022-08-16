def generate_some_stuff(start, stop):
    print('{',end="")
    for i in range(start,stop + 1):
        print(f'"{i}":"",',end="")
    print('}')