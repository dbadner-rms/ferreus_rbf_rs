import numpy as np
from pathlib import Path
from ferreus_rmt import build_isosurface


# Define a function to evaluate an isosurface from
# In this example we'll create a unit sphere
def sphere(pts: np.ndarray) -> np.ndarray:
    return np.linalg.norm(pts, axis=1) - 1.0


# Define the extents for the isosurfacer
extents = np.array([-1.1, -1.1, -1.1, 1.1, 1.1, 1.1])

# Define the resolution to evaluate at
resolution = 0.2

# Define some seed points on the isosurface
seed_points = np.array(
    [
        [1.0, 0.0, 0.0],
        [-1.0, 0.0, 0.0],
    ]
)

# Define the isovalue at which to surface
isovalue = 0.0

# Extract the isosurface
mesh = build_isosurface(
    seed_points,
    extents,
    resolution,
    isovalue,
    sphere,
)

# Check that extraction produced a valid mesh
assert len(mesh.vertices) > 0 and np.isfinite(mesh.vertices).all()
assert len(mesh.facets) > 0 and mesh.facets.max() < len(mesh.vertices)

# Save the isosurface out to an obj file
surface_name = f"isosurface_sphere_{resolution}m"
outpath = Path(f"{surface_name}.obj")
mesh.save_obj(str(outpath), surface_name)
