# SEO Content Pipeline

An SEO research agent. It researches keywords, discovers content opportunities, and builds a prioritized list of content ideas. Each run explores a seed topic and produces actionable suggestions, not finished articles.

## Install

```
gcontext add seo-pipeline
```

## How it works

1. Give the agent a seed topic and a scope (`narrow` for one niche, `broad` for cluster discovery).
2. It pulls keyword data and groups it into clusters.
3. Each cluster is scored for opportunity.
4. You get a prioritized list of content ideas.
5. Findings carry over to the next run.

## Connections

- `keyword-source`: a keyword research tool or data source (Google Search Console, Ahrefs, Semrush, or similar).

## What it learns

Insights about keyword landscapes across runs, so it can avoid saturated niches and spot recurring opportunities over time.

## Layout

- `commands/`: user-invokable entry points.
- `insights/`: accumulated keyword landscape knowledge.
- `runs/`: one folder per exploration.
- `steps/`: the research flow.

See `index.md` for the full agent definition.
