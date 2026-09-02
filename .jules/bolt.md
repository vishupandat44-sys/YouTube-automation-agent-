## 2025-05-18 - Avoid dataclasses.asdict for high-frequency object serialization
**Learning:** `dataclasses.asdict` uses recursion, `copy.deepcopy`, and heavy type inspection for generic dataclass conversion, which introduces significant overhead (~8x slower than explicit dict construction).
**Action:** Replace `asdict(obj)` with explicit dict building when serializing dataclass instances to JSON/dict in performance-critical paths.
