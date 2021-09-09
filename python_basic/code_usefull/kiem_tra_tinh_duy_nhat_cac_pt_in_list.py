def unique(l):
    if len(l) == len(set(l)):
        print("unique")
    else:
        print("!unique")

unique([1,2,3,4,5])

unique([1,1,2,3])