# SizePolicy

::: ferreus_rbf.config.SizePolicy

Use `SizePolicy.Auto` to calculate a size when building the hierarchy or tree,
or `SizePolicy.Fixed(n)` to retain an explicit positive limit.

```python
from ferreus_rbf.config import DDMParams, SizePolicy

ddm = DDMParams(
    leaf_threshold=256,
    overlap_knn=16,
    coarse_reduction_factor=128,
    coarse_threshold=SizePolicy.Auto,
)
```
