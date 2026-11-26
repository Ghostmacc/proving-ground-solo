import sys


def main():
    if len(sys.argv) > 1:
        if len(sys.argv) == 2 and sys.argv[1] == "--version":
            print("fizzbuzz 1.0")
            return
        try:
            upto = int(sys.argv[1])
        except ValueError:
            upto = 0
        if upto < 1:
            print("error: N must be a positive integer", file=sys.stderr)
            sys.exit(2)
    else:
        upto = 100
    for n in range(1, upto + 1):
        print("FizzBuzz" if n % 15 == 0 else "Fizz" if n % 3 == 0 else "Buzz" if n % 5 == 0 else n)


if __name__ == "__main__":
    main()
