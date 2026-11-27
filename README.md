# proving-ground-solo

Test repository for merge automation on a branch with no merge queue. A change
merges only at an inspected commit with a green required check; anything the
ship policy does not cover needs the owner's approval of that exact commit.

## Usage

- `python fizzbuzz.py` prints 1 through 100.
- `python fizzbuzz.py N` prints 1 through N, where N is a positive integer.
- `--help` or `-h` prints usage.
- `--version` prints the version.

## Proof markers

- `.flaky-once` makes the first attempt of the check fail on purpose.
- `.deploy-flaky-once` makes the first deployment attempt fail on purpose.

Both exist so the factory's reruns can be observed.
