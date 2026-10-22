# Native merge queue lab

Disposable public synthetic fixtures; no production data or deployment.

Base: mode v1, feature disabled. PR A switches mode to v2. PR B enables a feature without v2 support. Each passes alone; A+B must fail. Fix B by adding v2 support, then let the native queue retest and merge.

The required `compatibility` job runs on both `pull_request` and `merge_group: checks_requested`. It checks actual fixture content, records the event and checkout SHA, and waits 45 seconds on merge groups solely to allow observation. There are no deployments, secrets, generated success statuses, or skipped assertions.
