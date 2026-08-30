## 2025-05-18 - Replacing dataclasses.asdict with Direct Dict Construction
**Learning:** `dataclasses.asdict()` recursively uses `copy.deepcopy()` and dynamic reflection, making object serialization up to ~8.8x slower compared to direct key-value dictionary construction.
**Action:** For performance-critical data serialization or dictionary conversion of fixed dataclasses, use direct dictionary mapping or explicit `.to_dict()` methods instead of `dataclasses.asdict()`.
