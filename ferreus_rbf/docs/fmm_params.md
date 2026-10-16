Parameters controlling the **Fast Multipole Method (FMM)** evaluator.

These settings configure the [`ferreus_bbfmm`] backend, which performs
fast evaluation of RBF interpolants by hierarchically partitioning space
and approximating long-range interactions through low-rank interpolation
and optional M2L operator compression.

Defaults are provided by [`FmmParams::new_defaults`], which selects
appropriate values based on the chosen kernel type.

### Intended Usage
This configuration is primarily exposed for **developers and advanced users**
who wish to experiment with or tune FMM performance. In most cases, the
defaults provide an excellent balance between accuracy, memory usage, and
computation time across a broad range of problems.

Increasing the interpolation order improves accuracy but also increases
computational cost. Default interpolation order:
- Linear and Spheroidal kernels -> order `7`
- ThinPlateSpline kernel -> order `9`
- Cubic kernel -> order `11`  
Orders that are too low may stall solver convergence.

### Default Values
- `interpolation_order`: *kernel dependent*
- `max_points_per_cell`: [`SizePolicy::Auto`](crate::config::SizePolicy::Auto)
- `compression_type`: [`FmmCompressionType::ACA`]
- `epsilon`: `10^(-interpolation_order)`
- `eval_chunk_size`: `1024`

Maximum number of points per cell before it is subdivided.
For fitting, Auto uses max(256, the largest power of two <= interpolation_order^dimensions).
For evaluation, Auto uses 256. Fixed(n) uses the provided positive limit for both.

# Examples
```
use ferreus_rbf::{
    config::{
        FmmParams, 
        FmmCompressionType, SizePolicy
    }, 
    interpolant_config::RBFKernelType
};
///
// Create FMM parameters with defaults tuned for a Linear kernel
let fmm = FmmParams::new_defaults(RBFKernelType::Linear);
///
assert_eq!(fmm.compression_type, FmmCompressionType::ACA);
assert_eq!(fmm.max_points_per_cell, SizePolicy::Auto);
```