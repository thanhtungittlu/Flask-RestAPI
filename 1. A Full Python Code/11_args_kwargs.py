def addition_simlified(*args):
    return sum(args)

print(addition_simlified(1,2,3))

def multiple(*args, **kwargs):
    print(args)
    print(kwargs)

multiple(56, 43, location ="UK", name="Tung")