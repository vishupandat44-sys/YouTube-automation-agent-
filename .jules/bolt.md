## 2025-05-18 - dataclasses.asdict Overhead in Serialization

**Learning:** Python's standard `dataclasses.asdict()` relies on recursive reflection, type checks, and deep copying for every field, which adds severe performance overhead (~8x slower) compared to explicit `to_dict()` methods on nested dataclasses.
**Action:** Replace `asdict()` with explicit `to_dict()` instance methods on dataclass models when dictionary serialization or JSON generation occurs frequently or in hot paths.

## 2025-05-19 - Preset Key Caching & Joined String Formatting

**Learning:** Converting dictionary key views (`list(dict.keys())`) inside repeated function calls allocates new list objects unnecessarily. Caching `tuple(dict.keys())` at module level and checking exact keys with `if key in dict:` before linear fallback loops significantly reduces selection overhead. Additionally, multiline string interpolation with list comprehensions is ~11% faster than repeated `list.append()` calls followed by `str.join()`.
**Action:** Pre-cache dict key tuples for random selection and construct formatted text outputs using single multiline f-strings with joined comprehensions instead of imperative list appending loops.
