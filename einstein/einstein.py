def main():
    c = 300000000
    m = int(input('m: '))
    print(energy(m, c))

def energy(mass, light):
    return mass * (light ** 2)

main()
