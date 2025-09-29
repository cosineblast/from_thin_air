import sys
import thin_air
import problems
import random

try:
    import rich.console

    console = rich.console.Console()
except ImportError:

    import re

    class BasicConsole:
        def print(self, *args, **kwargs):
            no_bb = [self.__remove_bbcode(arg) for arg in args]

            print(*no_bb, **kwargs)

        def rule(self, *args, **kwargs):
            print("  ===============  ", *args, "  ===")

        def __remove_bbcode(self, string):
            b = "\\[(\\w|\\s)+\\](.*?)\\[/(\\w|\\s)+\\]"
            r = "\\2"
            return re.sub(b, r, string)

    console = BasicConsole()


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

    # base cases are cases which don't necessarily have to call `thin_air.solve`
    # (usually base cases)
    def base(*example):
        return (tuple(example), "base")

    # step cases are cases which necessarily expect calls to thin_air.solve
    def step(*example):
        return (tuple(example), "step")

    random.seed(21)

    def random_list(size=10):
        return [random.randint(1, size * 2) for _ in range(size)]

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
        ]
        + [step(random_list(size)) for size in [2, 4, 8, 16, 32, 64, 128, 256]]
    )
    def list_sum(stuff):
        assert isinstance(stuff, list)
        return sum(stuff)

    @exercise(
        [
            base([1]),
            base([2]),
            base([-4]),
        ]
        + [step(random_list(2**n)) for n in range(2, 16)]
    )
    def list_max(stuff):
        assert isinstance(stuff, list)
        return max(stuff)

    @exercise(
        # empty list
        [base(n, []) for n in random_list(10)]
        +
        # x is in the stuff
        [
            (lambda stuff: base(random.choice(stuff), stuff))(random_list(2**n))
            for n in range(2, 8)
        ]
        +
        # x is not in the stuff
        [
            (lambda stuff: step(max(stuff) + 1, stuff))(random_list(2**n))
            for n in range(2, 8)
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


def run_test_case(test):
    global current_test
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


def main():
    console.rule("RUNNING TESTS", style="bold")
    global current_test

    for test in get_test_cases():
        run_test_case(test)

    console.print("[green] well done![/green]")
    console.print(" i think you you should try [red bold]recursion[/red bold] ;)")


if __name__ == "__main__":
    main()
