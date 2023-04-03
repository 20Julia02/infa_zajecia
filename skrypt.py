import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-x", "--x", type=float)
parser.add_argument("-y", "--y", type=float)
args = parser.parse_args()

suma = args.x + args.y

print(suma)

if __name__ == "__main__":  # __main__ przypisywane do modułu pythonowego, __name__ ma inną wartość gdy zaimportowany, inną gdy nie
    # po to by przy imporcie nie wykonywało się to co pod if, wykonanie kodu może być pod tym
    print("cos tam")
