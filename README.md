# Python Basics — A Practical Tutorial

Welcome to the Python Basics tutorial repository. This collection of concise, well-commented example scripts is designed for beginners and intermediate learners who want to build a solid foundation in Python programming, from variables and control flow to functions, data structures, and OOP concepts.

## What you'll learns

- Core language concepts: data types, variables, expressions, and operators
- Control flow: conditionals and loops
- Functions: defining, invoking, closures, decorators, and function objects
- Data structures: lists, tuples, sets, dictionaries, and common operations
- Modules and packages: how to structure and run example scripts
- Object-oriented programming basics: classes, inheritance and composition
- Recursion, scope (global vs local), and more practical examples

## Repository structure

This folder contains short example scripts organized by topic. Each file is small and focused so you can read and run examples quickly.

- `main.py` — Small entry point / index (examples or launcher)
- `Introduction/` — Beginner topics (printing, variables, basic datatypes)
- `Variables/` — `PY_GlobalAndLocalVariables.py` — global vs local, mutability demos
- `Control Statements/` — conditionals and loops
- `Data Structures/` — lists, tuples, sets, dictionaries, strings
- `Functions/` — functions, lambdas, closures, and annotations
- `OOP Concepts/` — classes, objects, inheritance examples
- `Recursion/` — recursion examples

(If you add files, keep the pattern: one topic per file, with examples and comments.)

## Quick start (Windows PowerShell)

1. Make sure you have Python 3.8+ installed. To check:

```powershell
python --version
```

2. Run a single example script. From the `PY_BASIC` folder run:

```powershell
python .\Variables\PY_GlobalAndLocalVariables.py
```

or run the main launcher (if present):

```powershell
python .\main.py
```

3. If you prefer an isolated environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python --version
```

Then run any example while the virtual environment is active.

## How to read and use the examples

- Read the top-level docstring or header comment in each file for purpose and usage notes.
- Examples are intentionally small: study the code, run it, then tweak inputs to observe behavior.
- Look out for comments explaining CPython details where relevant (e.g., names -> objects, mutability vs immutability).

## Recommended learning path

1. `Introduction/` to get comfortable with the interpreter and basics.
2. `Variables/` to understand scope and mutability.
3. `Control Statements/` and `Data Structures/` to build small programs.
4. `Functions/` to learn decomposition, higher-order functions, and closures.
5. `OOP Concepts/` to structure larger programs and understand design choices.
6. `Recursion/` and small projects to combine concepts.

## Design notes and best practices

- Favor composition over inheritance for domain modelling (e.g., an Account should "have" an Owner, not be a Person).
- Use `super()` and cooperative multiple inheritance only for mixins or well-designed hierarchies.
- Keep functions small and test them interactively from the REPL.

## Contributing

Contributions are welcome!

- Follow the existing style: short files with clear comments and runnable examples.
- Add tests or examples that demonstrate the concept clearly.
- When in doubt, favor readability over cleverness.

## License

This repository does not include a license file by default. If you want permissive reuse, consider adding an `MIT` license file. If you'd like, I can add a license template for you.

## Contact / Next steps

If you want, I can:
- Add a `CONTRIBUTING.md` with contribution guidelines and a simple test harness.
- Add a small `Makefile` / `run_examples.ps1` to run all examples automatically.
- Add unit tests for a few modules to demonstrate test-driven learning.

Happy learning — open a file, run it, and experiment!
