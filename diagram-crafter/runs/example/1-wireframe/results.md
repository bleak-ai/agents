# Wireframe

Candidates: pipeline-flow (three actors, the pull hop carries the claim),
cycle-loop (enqueue, hold, pull, ack as a ring; rejected: the loop is per
job, the claim is about direction).

Approved: pipeline-flow.

    +-- Producers --+     +-- Broker ----+     +-- Workers ---+
    | enqueue jobs  | --> | holds queue  | <-- | pull when    |
    |               | job |  [queue]     | pull| ready        |
    |               |     |  [acks]      | --> |  [worker]    |
    +---------------+     +--------------+ ack +--------------+

    (1) producers never wait   (2) the broker holds   (3) workers set the pace
