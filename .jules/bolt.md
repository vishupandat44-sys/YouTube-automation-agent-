## 2026-08-31 - Python `dataclasses.asdict` Overhead in Serialization
**Learning:** `dataclasses.asdict()` relies on recursive deep-copying and dynamic field introspection, introducing significant performance overhead compared to explicit dictionary mapping for dataclass models.
**Action:** Replace `dataclasses.asdict(self)` with explicit `to_dict()` methods on known dataclasses for a ~8x speedup in serialization.
