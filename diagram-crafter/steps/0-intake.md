# Step 0: Intake

## Purpose

Take the initial text and the audience, and pin down the single claim the
diagram must make. Ask only what the text does not already answer.

## Input

The task description (the initial text, or a pointer to it); `diagrams/`
(the library of past work).

## Output

- `runs/{date}-{slug}/index.md`: claim, audience, and a status line.
- `runs/{date}-{slug}/0-intake/results.md` with:
  - **Source**: the initial text, verbatim or summarized if long.
  - **Audience**: who reads this diagram and where they see it.
  - **Claim**: the single sentence the diagram must make.
  - **Follow or compare**: what the reader must follow (a flow) or
    compare (states, layers).
  - **Left out**: what the text mentions that the diagram will not show.
  - **Prior art**: past diagrams from `diagrams/index.md` with a related
    claim shape, and what worked or did not (from their metadata).

## How to execute

1. Read the initial text from the task. If the task names a file path,
   read that file. If there is no usable text, print BLOCKED per
   `style.md`.
2. Derive the kebab-case slug (two or three words). The run folder is
   `runs/<YYYY-MM-DD>-<slug>/` per `style.md`.
3. Draft answers to all four scoping dimensions yourself first: reader,
   claim, follow-or-compare, leave-out.
4. Ask ONE round of scoping questions, maximum 4, through the question
   tool, and only for dimensions the text left genuinely open. Offer
   your drafted answer as the first option of each question. Never ask a
   second round.
5. Read `diagrams/index.md`. For entries with a similar claim shape,
   read their metadata headers and note reusable compositions or
   recorded weaknesses in the results file.
6. Write the intake results file. Present claim and audience as two
   short lines. Confirm through the question tool (correct / adjust).
7. Set the run index status line to `intake done`.

## Done when

The results file is written and the user has confirmed the claim and the
audience.
