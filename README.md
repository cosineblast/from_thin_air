

# `from thin_air` challenge

This is a small challenge intended to teach you on how to
adapt existing algorithms into new ones.

The main goal is to exercise the programmer's ability to answer the following question:

"How would I solve this problem if someone had already solved part of it for me"

In this challenge, you will be solving a variety of exercises, which consist of
implementing functions to solve simple tasks, such as sorting lists, or computing
list sums.

However, there's a catch! To pass this challenge, your solutions must use the aid of a
an existing helper function `solve` that can solve this same problem for you,
and you always have to use `solve` with an argument that is less than the one your function received
(in other words, you can't cheat by calling `solve` on the original input itself).

This skills can be really useful for developing new algorithms to solve problems, and
can help you tame other subjects which are typically [more scary](https://en.wikipedia.org/wiki/Recursion).

## running this project

You can clone the whole repository with

```bash
  git clone  https://github.com/cosineblast/from_thin_air
```

The challenge itself resides in `problems.py`, which you'll modify.
You can run the tests by executing `tests.py` with `python3 tests.py`.
The tests will initially fail, you edit `problems.py` to make them pass.

Have fun!

### optional: prettier output

This project is self-contained, it does not depend on external python libraries.
However, you may benefit from prettier test output by installing the `rich` python library:

```bash
python3 -m venv env
source env/bin/activate
pip install rich
````

Then run `python3 tests.py` as usual.

