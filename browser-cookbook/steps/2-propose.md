# Step 2: Verdict and recipe proposal

## Purpose

Decide script or playbook, then write the recipe.

## Input

The exploration log from step 1; the site notes.

## Output

`runs/{date}-{slug}/2-recipe/results.md` with:

- **Recipe name**: kebab-case.
- **Script verdict**: `script: yes` or `script: no`, followed by the reason. The default is yes. A no must name the concrete obstacle: content-dependent branching, unstable layout, anti-bot pressure. This verdict is copied into the recipe's index.md in step 3.
- **Anchoring**: for each element the script touches, list the anchor and its strategy (`text-label`, `aria-role`, `stable-id`, or `css-class`). Add one durability line: `high` when all anchors are stable types (text-label, aria-role, stable-id), `low` when any anchor is css-class, with the expected failure mode. Convention: prefer text-label and aria-role anchors over generated class names. Use css-class only when no stable alternative exists.
- **Parameters**: name, type, description, default for each. Give a default whenever a sensible standing value exists; a default makes the recipe's slash command runnable with zero typing.
- **Read-only or mutating**: from step 0, confirmed against what exploration showed.
- For `script: yes` - **Script**: full Python source. For `script: no` - **Playbook**: the ordered instructions the AI follows on future runs, referencing site blocks, plus which deterministic stretches go into `lib.py`.
- **Test plan**: input values and expected result.

## Script conventions

- Parameters as positional arguments, in frontmatter order, each with `nargs='?'` and the declared default.
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

- The CDP port is not a constant. Read it from the browser connection's `roster.md` at run time (parse the DEFAULT line for the port number). Never hardcode `9222` or any other port in a script.
- Extract a `blocks/*.md` fragment or a lib.py helper when a SECOND recipe needs the same thing, not speculatively.

## Done when

The user approved the proposal through the question tool (approve / change parameters / flip the script verdict / cancel). The proposal itself is one of the three prose points allowed by `style.md`; keep it complete.
