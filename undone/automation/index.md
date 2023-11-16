---
title: "Automation"
tag: "Let the computer do the work."
syllabus:
- FIXME
---

## Continuous Integration

-   Should always run checks when committing code
    -   Or changing documentation, or...
-   But human beings are fallible, so automate: continuous integration (CI)
-   Many dedicated CI services like [Circle CI][circle-ci]
-   For a project this size, easiest is [GitHub Actions][gh-actions]
-   Create a directory `.github/workflows` beneath the root of the project
-   Add a file `test-on-push.yml` in that directory:

```yaml
name: Test on Push
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v1
        with:
          python-version: 3.9
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run code checks
        run: inv lint
      - name: Run tests
        run: inv test
        if: ${{ always() }}
```

-   `name` is the name of the action (used in error reporting, etc.)
-   `on` defines when the action runs
    -   When there's a `push` to the `main` branch
    -   When anyone creates a pull request whose target is `main`
    -   Lots of other options
-   `jobs` defines what to do when the action runs
    -   An action can run many jobs in parallel
-   We want to build our software on the latest version of Ubuntu Linux
    -   Probably the most common platform
-   Spell out the steps:
    -   Use a [pre-defined `checkout` action][gh-actions-predefined] to get a fresh copy of the repo
    -   Set up Python using another pre-defined action
    -   Install everything listed in `requirements.txt`
    -   Run the code checks (do *not* reformat, just check)
    -   Run the tests: the `if` condition means "even if the previous linting step fails"
-   Before we test it, let's split requirements into "needed for install" and "also used in dev"
-   `requirements.txt` becomes:

```
kaleido>=0.2
pandas>=1.4
plotly>=5.6
pydantic>=1.9.0
pyyaml>=5.4
requests>=2.27
statsmodels>=0.13
```

-   Create a new file `development.txt` that tells `pip` to read `requirements.txt` (using `-r`) then add more packages

```
-r requirements.txt
black>=22.1
coverage>=6.3
flake8>=4.0
invoke>=1.7
isort>=5.10
ivy>=6.2
pdoc3>=0.10
pymdown-extensions>=9.3
pyproject-flake8
pytest>=7.1
```

-   `git add` changes, commit, push to GitHub, go to the `Actions` tab: the job has failed
    -   Because `invoke` isn't included in `requirements.txt`, but is needed for the action
    -   So are `black`, `flake8`, `isort`, and `pytest`
-   Move `invoke` to `requirements.txt`, add, commit, push
    -   Works this time
    -   Some projects have `development.txt`, `testing.txt`, and `requirements.txt` for this reason
    -   It all should live in `pyproject.toml`...

<div class="callout" markdown="1">
### Other Jobs

The GitHub Actions tab shows all the jobs, including the ones that build and deploy the website.
If you have pushed several times, then rebase and push the combined commit,
the jobs run by the now-squashed commits still show up.
</div>

---

Everyone is talking about DevOps these days,
even though (or perhaps because) no one can quite agree what it is.  The term
mostly seems to refer to practices that minimize the time between a developer
implementing a change and that change being tested, integrated, tested again,
and deployed.  Those practices have one thing in common: automating as many steps as possible to make them fast and
reliable.  You may not be required to do this for your project, but if you have
time, you should try to do a little—it will save time when you are up against
the end-of-term deadline, and more importantly, prevent mistakes when you are
stretched thin.

## Build Manager

The foundation for almost all automation in software development is a
build manager—a tool that will
transform what you've typed into what you want to deliver. The origin build
manager is [Make][make], which was
invented in 1975 by a summer intern at Bell Labs to compile programs in which
some modules depended on others. To use it, you create a Makefile that specifies
the dependencies between the files in your project and the commands needed to
update them. For example:

```make
game.exe : game.bc graphics.bc utils.bc
        tx -E -o game.exe game.bc graphics.bc utils.bc

%.bc : %.grace
        tx -C $<
```

<!-- continue -->
tells Make that `game.exe` can't be built until `game.bc`, `graphics.bc`, and
`utils.bc` exist, and that once they do, the way to create `game.exe` is to run
the `tx` compiler with several options.  Below that is a
pattern rule telling Make
how to create any `.bc` file from a `.grace` file with the same root name;
the cryptic expression `$<` is Make's way of saying "the first thing the target depends on".

Make has been used by hundreds of thousands of programmers for more than thirty
years, but has some fundamental flaws. The
first is its syntax, which looks like something produced by a cat dancing on the
keyboard. The second is that it runs commands by handing them over to whatever
operating system it is running on, which make portability a constant headache.
(Quick, should you use `rm` or `del` to delete a file?) Third, Make doesn't have
a debugger: the only way to track down problems in your build configuration is
to stare at the configuration file until little drops of blood form on your
forehead.

I could live with ugly syntax—if Ie kan lurn Inglish speling, Ie kan lurn
eneething. But the lack of a debugger is a never-ending headache, because real
build systems aren't just configured: they're programmed. For example, this
book's Makefile checks the consistency of cross-references and glossary
entries, makes sure all the bibliography citations are in place, and copies
files to my web site, and is more complex than many programs I've written.
Thinking of it as a "configuration" file is a mistake: you *have* to approach builds as a programming problem.

The current generation of build managers dispense with custom configuration file
syntax, but most still don't have debuggers. The `package.json` file used by
[Node.js][nodejs] serves as both a package manifest and a build
file—as the example below shows, some of its entries describe the package or
its dependencies, while others store commands that can be re-run by typing
things like `npm run test`:

```js
{
  "name": "stjs",
  "version": "1.0.0",
  "description": "Software Design by Example",
  "type": "module",
  "main": "index.js",
  "scripts": {
    "ejslint": "ejslint inc/*.html *.md */*.md",
    "serve": "http-server docs -p 4000 --utc",
    "test": "mocha */test/test-*.js"
  },
  "dependencies": {
    "argparse": "^2.0.1",
    "caller": "^1.0.1",
    "csv": "^5.3.2",
    ..
  }
}
```

<!-- continue -->
`package.json` files have two flaws: there is no standard way to write comments
(since JSON itself doesn't have this) and there is no way
to express dependencies between tasks, i.e., there's no way to say, "A depends
on B which depends on C".

[Snakemake][snakemake] and
[Rake][rake] take the idea of "build
file as data structure" one step further. Their users describe dependencies as
small Python or Ruby programs respectively, making use of an extensive support
library that handles dependencies, invokes appropriate compilers, and so on.
Debugging is still problematic, but at least it's possible. Unfortunately, like
front-end JavaScript frameworks and static site generators, a simple build tool
is so simple to create that hundreds have proliferated. As a result, none has
achieved critical mass.

Whatever you choose or are told to use, please follow these rules:

Pick something that plays nicely with your other tools.
:   For example, most Java editors and IDEs integrate with a build tool called
    [Ant][ant],
    which means they can jump directly to compilation errors when they occur.

Be very cautious about adding dependencies.
:   "Reduce, re-use, recycle" is as important for software as it is for daily
    life, but every library you depend on is one more way for your project to
    accumulate technical debt.  Recent
    research shows that we are all biased toward solving problems by adding
    things instead of taking them away [%b Meyvis2021 %]; checking the
    packages your project depends on before every release and cutting any you
    can will prevent a lot of future headaches.

Always use the build manager—never compile or copy things by hand.
:   This isn't just for efficiency's sake: if any of the things you need to do
    to get your application up on your web site have to be done by hand, the
    odds are that you'll forget a crucial step right before your end-of-term
    demo.

Always use the build manager—never compile or copy things by hand.
:   Yes, I'm repeating myself, but this time the reason is different. If you do
    something by hand, one of your teammates might do it differently.  "But it
    works on my machine!" isn't something you want to hear an hour before a
    deadline…

A good way to start using a build manager is to create a "version zero" of the
project. Set up the build and make sure it works even when there isn't anything
to compile, run, test, or copy. Now add something—anything.  Does the build
still work? If it does, you're on your way.

<blockquote markdown="1">
### Never break the build

Once you have a build system in place, never commit anything to version control
that breaks the build. This is one of the golden rules of working in a
team: if your code won't compile, or doesn't pass whatever automated tests you
have, then putting it into the repository means putting every other person on
your team into exactly the same broken state you're in. When you're working on
your own, it's OK to use version control as a way to transfer files from one
machine to another, or as a way to back things up at the end of the day. Do
*not* carry this habit over to teamwork.
</blockquote>

## Checking Style

One task you should add to your build system right at the start of the project
is something that runs a style checker to make sure your code follows the team's formatting rules.
(Style checkers are often called linters
because an early one called `lint` looked for problems in C programs.)  Some of
these rules are as simple as "no method can be longer than 100 lines" or "class
names must be written in CamelCase".  Modern tools like [ESLint][eslint] for JavaScript, [Checkstyle][checkstyle] for Java, or [Black][black] for Python
can do a lot more: they can find code that is never called, parameters that are
never used, duplicated code that could be refactored, and a lot more.  Code
reviews are much more straightforward when the code you're looking at is
guaranteed to be clean, so if something violates style rules, treat it as a
broken build.

Style checkers are just one kind of static analysis tool, since they work by parsing the source
code for your program rather than by watching the program run. Compilers also do
a lot of static analysis; the non-fatal warnings they produce are a lot more
useful than many students realize, and a "zero warnings" policy can prevent a
lot of subtle bugs.  As we'll see in FIXME, requiring type
definitions in code helps programmers understand software as well.

## Continuous Integration

Build tools will do a lot more for you if you adopt some kind of continuous integration system such as [Travis CI][travis-ci] or
[GitHub
Actions][github-actions].  These can be set up to run either at regular
intervals (e.g., every hour or at three a.m.), or every time someone checks into
version control (which I find more useful). Each time they run, they check a
fresh copy of the project out of version control, build it, re-run all the
tests, and post the results to the project's blog, web site, and mailing list.

Research has proven the benefits of CI [%b Hilton2016 %].  It acts as a
"heartbeat" for the project: as soon as anything goes wrong, everyone knows. It
also encourages good development practices: if someone checks something in that
doesn't compile, run, or pass the project's tests, everyone will know very
quickly. (Funnily enough, after the system has shamed you a couple of times,
you'll stop checking in broken code…)

For example, we can check every attempt to push changes to the repository for a
Python project, and every pull request created for that repository, by putting
these commands in a file called `.github/workflows/check.yml`:

```yml
name: Check

on: [push, pull_request]

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Setup Python
        uses: actions/setup-python@v1
        with:
          python-version: 3.9

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - run: black --check .
      - run: flake8
      - run: pytest
```

From top to bottom:

-   The `name` key tells GitHub what this action is called, while the values
    associated with the `on` key determine when the action runs.

-   An action can have many jobs (or tasks); in this case there's just one called
    `check`.  We want it to run on the latest version of Ubuntu Linux.

-   The `uses` key tells GitHub to run the steps in another action before
    running the steps for this one; `actions/checkout@v2` points at steps in
    GitHub's own `actions` repository, but there are lots of others.

-   Similarly, we can use a pre-defined action to set up Python 3.9, and then
    use `pip` to install our project's requirements (which are listed in a file
    called `requirements.txt`). This ensures that we have a brand-new
    environment every time we run our checks.

-   We can now run our checks: `black` to check code style, `flake8` to look for
    common errors, and `pytest` to run our tests. If any of these fail (i.e., if
    any return a non-zero exit status), the overall action fails and the push or
    pull request doesn't go through.

Configuring actions like these is a programming task like any other, except for
the fact that you specify what you want in YAML rather than in Python,
JavaScript, or some other language.  [%b Zampetti2020 %] looks at how
*not* to use CI, and can serve as a good checklist of things to avoid.

If you don't want to go this far, you can add pre-commit or post-commit hooks to your repository to specify actions to run on your machine before
and after each commit. When I set these up, I almost always have them run
commands via the build manager so that I can also run checks whenever I want.

<blockquote markdown="1">
### Getting past the dip

Any new tool or practice initially makes you less productive, so if you're up
against a deadline (as you almost always will be), the safest course of action
is often to keep doing things the "wrong" way because there isn't time to learn
how to do it more efficiently.  This is why I think that lab exams should be
part of project courses, i.e., that you should be required to demonstrate to
your instructor that you're able to use a build manager or a debugger.  People
learn how to use version control because they're required to in order to submit
work for grading; if you are required to submit a screen recording of you using
particular tools as part of an assignment, it will help you in the long run.
</blockquote>
