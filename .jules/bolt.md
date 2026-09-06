## 2025-05-18 - dataclasses.asdict Overhead in Serialization

**Learning:** Python's standard `dataclasses.asdict()` relies on recursive reflection, type checks, and deep copying for every field, which adds severe performance overhead (~8x slower) compared to explicit `to_dict()` methods on nested dataclasses.
**Action:** Replace `asdict()` with explicit `to_dict()` instance methods on dataclass models when dictionary serialization or JSON generation occurs frequently or in hot paths.
