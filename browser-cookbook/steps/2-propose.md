# Step 2: Verdict and recipe proposal

## Purpose

Decide script or playbook, then write the recipe.

## Input

The exploration log from step 1; the site notes.

## Output

`runs/{slug}/2-recipe/results.md` with:

- **Recipe name**: kebab-case.
- **Script verdict**: `script: yes` or `script: no`, followed by the reason. The default is yes. A no must name the concrete obstacle: content-dependent branching, unstable layout, anti-bot pressure. This verdict is copied into the recipe's index.md in step 3.
- **Parameters**: name, type, description, default for each.
- **Read-only or mutating**: from step 0, confirmed against what exploration showed.
- For `script: yes` - **Script**: full Python source. For `script: no` - **Playbook**: the ordered instructions the AI follows on future runs, referencing site blocks, plus which deterministic stretches go into `lib.py`.
- **Test plan**: input values and expected result.

## Script conventions

- Parameters via argparse, matching the parameter list exactly.
- The last thing a script does is assert the success definition. "No exception" is not success.
- Shared site logic goes into `sites/<domain>/lib.py`, not into the script. Because domain folders contain dots, load lib.py with this helper (put it in the script as-is):

```python
import importlib.util, pathlib

def load_site_lib(domain):
    p = pathlib.Path(__file__).resolve().parents[2] / "sites" / domain / "lib.py"
    spec = importlib.util.spec_from_file_location("site_lib", p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod
```

- Extract a `blocks/*.md` fragment or a lib.py helper when a SECOND recipe needs the same thing, not speculatively.

## Done when

The user has approved the recipe proposal.
