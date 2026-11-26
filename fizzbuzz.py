import sys


def main():
    if len(sys.argv) > 1:
        if len(sys.argv) == 2 and sys.argv[1] == "--version":
            print("fizzbuzz 1.7")
            return
        if sys.argv[1] in ("--help", "-h"):
            print("usage: fizzbuzz.py [-h] [--version] [--upto N] [N]")
            return
        if sys.argv[1] == "--upto" and len(sys.argv) == 2:
            print("error: --upto requires a value", file=sys.stderr)
            sys.exit(2)
        arg = sys.argv[2] if sys.argv[1] == "--upto" else sys.argv[1]
        try:
            upto = int(arg)
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
