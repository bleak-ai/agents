# Intake

**Source**: docs page draft for "Queuely", a fictional job queue. Producers
enqueue jobs; workers pull when ready; a broker holds the queue and
acknowledgements.

**Audience**: backend developers evaluating the queue, reading the docs
landing page.

**Claim**: workers pull jobs, they never receive them.

**Follow or compare**: follow a job from producer through broker to a
worker, and the acknowledgement back.

**Left out**: retry policy, dead-letter queue, deployment options.

**Prior art**: gcontext-architecture (pipeline-flow) matched the claim
shape: three actors, hops carry the claim.
