## 2025-05-18 - Avoid `dataclasses.asdict` in Performance-Critical Data Serialization
**Learning:** Python's standard library `dataclasses.asdict()` relies on deep recursive introspection and defensive copying, causing substantial execution overhead during dictionary and JSON serialization.
**Action:** Implement explicit `.to_dict()` methods for dataclasses in hot serialization paths to achieve ~8x performance improvement without sacrificing type safety or readability.
