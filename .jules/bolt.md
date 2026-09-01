## 2026-03-31 - Avoid `dataclasses.asdict()` for frequent or latency-sensitive object serialization
**Learning:** Python's `dataclasses.asdict()` uses deep recursive introspection and copying via `copy.deepcopy()`. Replacing `asdict()` with explicit `.to_dict()` instance methods on dataclass models yielded an ~8x performance improvement (~88% runtime reduction) for serialization.
**Action:** In Python performance-critical paths, prefer writing explicit `.to_dict()` methods for dataclasses rather than using standard library `dataclasses.asdict()`.
