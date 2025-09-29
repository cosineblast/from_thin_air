# Things I want to work on:
# 1. Better output for assertions, properly explaining what went wrong
# 2. Better interface for defining test cases (possibily with builtin validation)

import sys
import thin_air
import problems
import rich.console
from rich.panel import Panel

console = rich.console.Console()

last_args = None


# Determines if the first value is less than the second, comparing
# each element pairwise recursively if necessary
def is_less(x, y):
    if (
        isinstance(x, str)
        and isinstance(y, str)
        or isinstance(x, int)
        and isinstance(y, int)
        or isinstance(x, float)
        and isinstance(y, float)
    ):
        return x < y

    return compare_sequences_for_less(x, y)


def compare_sequences_for_less(x, y):
    if len(x) < len(y):
        return True
    if len(x) > len(y):
        return False

    has_less = any((is_less(a, b) for a, b in zip(x, y)))
    has_more = any((is_less(b, a) for a, b in zip(x, y)))

    if has_more:
        return False

    return has_less


def get_test_cases():
    all_exercises = []

    def exercise(examples):
        def modify(function):
            all_exercises.append(
                {
                    "name": function.__name__,
                    "implementation": function,
                    "examples": examples,
                }
            )

        return modify

    # The exercises and their respective comparing implementation go here

    def base(*example):
        return (tuple(example), "base")

    def step(*example):
        return (tuple(example), "step")

    @exercise(
        [base(b, 0) for b in [2, 3, 10]]
        + [step(b, n) for b in [2, 3, 10] for n in range(1, 10)]
    )
    def pow(b, n):
        assert isinstance(b, int)
        assert isinstance(n, int)
        assert b >= 0
        assert n >= 0
        return int(b**n)

    @exercise(
        [
            base([]),
            step([1]),
            step([2]),
            step([3]),
            step([1, 2, 30]),
            step([3, 20, 1]),
            step(list(range(2))),
            step(list(range(4))),
            step(list(range(8))),
            step(list(range(16))),
            step(list(reversed(range(100)))),
        ]
    )
    def list_sum(stuff):
        assert isinstance(stuff, list)
        return sum(stuff)

    @exercise(
        [
            base([1]),
            base([2]),
            base([-4]),
            step([1, 2, 30]),
            step([3, 20, 1]),
            step([1, 2, 30]),
            step([3, 20, 1]),
            step([1, -2, 3]),
            step([3, -4, 5]),
            step(list(range(2))),
            step(list(range(4))),
            step(list(range(8))),
            step(list(range(16))),
            step(list(reversed(range(100)))),
        ]
    )
    def list_max(stuff):
        assert isinstance(stuff, list)
        return max(stuff)

    @exercise(
        [
            base(1, []),
            base(2, []),
            base(-1, []),
            base(0, []),
            step(0, [1, 2, 3]),
            base(1, [1, 2, 3]),
            step(2, [1, 2, 3]),
            step(3, [1, 2, 3]),
            step(4, [1, 2, 3]),
            base(10, [10, 20, 30]),
            step(-1, [10, 20, 30]),
            step(7, [0, 1, 1, 2, 3, 5, 8]),
        ]
    )
    def list_element(x, stuff):
        assert isinstance(x, int)
        assert isinstance(stuff, list)
        return x in stuff

    return all_exercises


current_test = None


def ensure(condition, kind, message):
    if not condition:
        console.print(":boom:", end="")
        print()
        print()

        pretty_arg = lambda args: "({})".format(", ".join([str(it) for it in args]))

        console.rule("TEST FAILED!!!", style="red")
        console.print(
            "  - [bold red]error[/bold red]: [white bold]{}[/white bold]".format(kind)
        )
        console.print(
            "  - While testing [blue]{}[/blue]{}".format(
                current_test, pretty_arg(last_args)
            )
        )
        console.print("  " + message)

        sys.exit(1)


def import_problem_or_none(name):
    try:
        return getattr(problems, name)
    except AttributError:
        return None


def main():
    console.rule("RUNNING TESTS", style="bold")
    global current_test

    for test in get_test_cases():
        name = test["name"]
        implementation = test["implementation"]
        examples = test["examples"]

        did_call = [False]

        def new_solve_function(*args):
            assert last_args is not None

            ensure(
                is_less(args, last_args),
                kind="non shrinking argument",
                message=(
                    "The argument passed down to [bold green]solve[/bold green] was not less than the one passed to your function."
                    "\n  Your function received {}, but {} was passed to solve"
                ).format(last_args, args),
            )

            did_call[0] = True

            return implementation(*args)

        print("     {}   ".format(name), end="")
        current_test = name

        thin_air.solve_function = new_solve_function

        for example, kind in examples:
            global last_args
            last_args = example
            did_call[0] = False
            expected = implementation(*example)
            got = getattr(problems, name)(*example)
            ensure(
                expected == got,
                kind="wrong answer",
                message="The expected output for this input is {} but your implementation returned {}".format(
                    expected, got
                ),
            )
            ensure(
                did_call[0] or kind == "base",
                kind="missing call to solve",
                message="Your function is expected to call [green bold]thin_air.solve[/green bold] for this particular case, but it is not doing so.",
            )
            print(".", end="")

        console.print(" [bold green]ok![/bold green]")

    console.print("[green] well done![/green].")
    console.print(" now you know recursion ;]")


if __name__ == "__main__":
    main()
