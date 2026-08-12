# Steps

`run_create_cookbook` runs all four. `run_once` runs 0 and 1 only (no recipe artifacts). `run_recipe` re-enters at 1 when healing needs re-exploration.

0. [Analyze](0-analyze.md): understand the task, check recipes and site knowledge, define success.
1. [Explore](1-explore.md): drive the browser, record every step, update site knowledge.
2. [Propose](2-propose.md): write the script verdict, then the recipe (script by default).
3. [Test](3-test.md): run the recipe, save on success, heal on failure.
