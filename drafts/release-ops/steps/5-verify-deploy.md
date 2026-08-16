# 5 - Verify Deploy

## Purpose

Confirm that the deploy triggered by the push actually succeeded. Block the announcement until the service is live and healthy. Skip this step for scopes that publish to a package registry only (e.g. PyPI) with no deploy.

## Input

- The scope and version from step 3.
- The deploy-target connection (if configured).
- The live URL for the scope.

## Output

Write `5-verify-deploy/results.md` in the run folder with: deploy/build status, HTTP health check result, and pass/fail verdict. If skipped, write a one-line note: "No deploy target for this scope. Step skipped."

## How to execute

1. **Check if this scope has a deploy target.** If the scope publishes to a package registry only, write the skip note and close the step.

2. **Wait for the build to start.** Auto-deploy typically triggers on push. Wait 10 seconds after the push before the first check.

3. **Poll the deploy platform.** Query the deploy target connection for the most recent deployment status. Poll every 15 seconds until the status is success or failure. Timeout after 5 minutes.
   - If success: continue to step 4.
   - If failure: report the error, include the build log if available, and stop. Do not announce.

4. **HTTP health check.** Send a GET request to the live URL. Expect a 200 status code. Retry up to 3 times with 10-second intervals (the new container may need a moment to start serving).
   - If 200: pass.
   - If not 200 after 3 retries: report the status code and stop. Do not announce.

5. **Record the result.** Write pass/fail, the deployment ID, and the HTTP status to the run folder.

## Done when

Both checks pass. The deployment is confirmed live and healthy.
