"""Acceptance check: fizzbuzz.py must print FizzBuzz for 1..100, one per line."""
import subprocess
import sys


def expected():
    for n in range(1, 101):
        yield "FizzBuzz" if n % 15 == 0 else "Fizz" if n % 3 == 0 else "Buzz" if n % 5 == 0 else str(n)


def main():
    try:
        out = subprocess.run([sys.executable, "fizzbuzz.py"], capture_output=True, text=True, timeout=30)
    except FileNotFoundError:
        print("FAIL: python not runnable")
        return 1
    if out.returncode != 0:
        print(f"FAIL: fizzbuzz.py exited {out.returncode}: {out.stderr.strip()[:200]}")
        return 1
    got = out.stdout.splitlines()
    want = list(expected())
    if got != want:
        for i, (g, w) in enumerate(zip(got, want), 1):
            if g != w:
                print(f"FAIL: line {i}: got {g!r}, want {w!r}")
                return 1
        print(f"FAIL: {len(got)} lines, want {len(want)}")
        return 1
    print("PASS: 100 lines match")
    for extra, want in (([], "2418"), (["10"], "33"), (["15"], "60")):
        cmd = [sys.executable, "fizzbuzz.py", "--sum", *extra]
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        label = " ".join(cmd[1:])
        if out.returncode != 0:
            print(f"FAIL: {label} exited {out.returncode}: {out.stderr.strip()[:200]}")
            return 1
        if out.stdout != want + "\n":
            print(f"FAIL: {label} printed {out.stdout!r}, want {want!r}")
            return 1
        print(f"PASS: {label} prints {want}")
    out = subprocess.run([sys.executable, "fizzbuzz.py", "--sum", "0"], capture_output=True, text=True, timeout=30)
    if out.returncode != 2:
        print(f"FAIL: fizzbuzz.py --sum 0 exited {out.returncode}, want 2")
        return 1
    print("PASS: fizzbuzz.py --sum 0 exits 2")
    out = subprocess.run([sys.executable, "-m", "unittest", "test_roman"], capture_output=True, text=True, timeout=30)
    if out.returncode != 0:
        print(f"FAIL: test_roman exited {out.returncode}: {out.stderr.strip()[:200]}")
        return 1
    print("PASS: test_roman")
    out = subprocess.run([sys.executable, "-m", "unittest", "test_fizzbuzz"], capture_output=True, text=True, timeout=30)
    if out.returncode != 0:
        print(f"FAIL: test_fizzbuzz exited {out.returncode}: {out.stderr.strip()[:200]}")
        return 1
    print("PASS: test_fizzbuzz")
    return 0


if __name__ == "__main__":
    sys.exit(main())
