# AI Pipeline Engineering Assignment

## Part 1 – Token Optimization

### Baseline
- Total Tokens: **85,676**

### Optimized
- Total Tokens: **66,382**

### Optimizations Implemented

1. Reduced repeated system prompts by using a shorter shared prompt.
2. Reduced conversation history passed to downstream agents while keeping the retriever's context intact.

### Result

- Token reduction: **19,294 tokens (~22.5%)**
- Lower inference cost.
- Lower latency.
- Minimal impact on response quality.

---

## Part 2 – Debugging

### Issues Identified

- Intermittent timeout failures.
- Potential malformed outputs.
- Silent propagation of invalid data.

### Fixes

- Added retry logic for transient failures.
- Added output validation.
- Added centralized exception handling.
- Improved logging for troubleshooting.

---

## Part 3 – CI/CD

Implemented a GitHub Actions workflow that:

- Runs automatically on every push.
- Installs dependencies.
- Executes the test suite.
- Deploys to a staging environment when changes are merged into the `main` branch.

### Secrets Management

- Store API keys using GitHub Secrets.
- Never commit secrets to the repository.
- Inject secrets as environment variables during the workflow.

### Rollback Plan

If a production deployment fails:

1. Stop further deployments.
2. Roll back to the last stable release.
3. Verify application health.
4. Review workflow logs.
5. Fix the issue before redeploying.

---