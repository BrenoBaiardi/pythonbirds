def soma(*args):
    total = 0
    for n in args:
        total += n
    return total

if __name__ == "__main__":
    print(soma(1,2,3))
    print(soma(2,2,2))