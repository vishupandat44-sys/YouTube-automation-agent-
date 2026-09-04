## 2025-05-18 - Python Dataclass `asdict` Overhead

**Learning:** `dataclasses.asdict()` in Python recursively inspects fields and uses `copy.deepcopy` logic internally for serialization. Replacing `asdict(self)` with explicit `to_dict()` methods on dataclasses yields ~8.3x faster dictionary conversion and speeds up JSON generation.
**Action:** Use custom explicit `to_dict()` methods on dataclasses instead of standard `dataclasses.asdict()` when serializing data models.
