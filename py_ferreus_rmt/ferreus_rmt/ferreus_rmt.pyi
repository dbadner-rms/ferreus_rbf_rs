"""
/////////////////////////////////////////////////////////////////////////////////////////////
//
// Stubs file that enables type hints and intellisense for the ferreus_rmt Python API.
//
// Created on: 08 Jun 2026     Author: Daniel Owen
//
// Copyright (c) 2026, Maptek Pty Ltd. All rights reserved. Licensed under the MIT License.
//
/////////////////////////////////////////////////////////////////////////////////////////////
"""

from enum import Enum
from typing import Callable, Optional
import numpy as np
import numpy.typing as npt
from ferreus_rmt.progress import Progress

def get_evaluation_extents(
    extents: npt.NDArray[np.float64],
    resolution: float,
    *,
    sampling_transform: npt.NDArray[np.float64] | None = None,
) -> list[float]:
    """Return world-coordinate bounds covering all lattice evaluation points.

    Parameters
    ----------
    extents : npt.NDArray[np.float64]
        Finite clipping bounds [xmin, ymin, zmin, xmax, ymax, zmax], shape (6,).
    resolution : float
        Finite, positive world-space sampling resolution.
    sampling_transform : npt.NDArray[np.float64] | None, optional
        Optional affine transform applied to the sampling lattice to control its
        orientation and relative spacing. Provide the 3 x 3 linear part of the
        transform from world coordinates to sampling coordinates.
        If None, the default lattice is used. The resolution controls the overall
        sampling distance, so uniform scaling of the transform has no effect.

        This is useful for surfaces with a strong directional trend.
        Aligning the lattice with the structure allows
        finer sampling across thin features and coarser sampling along smoother
        directions.

    Returns
    -------
    list[float]
        Six world-coordinate bounds covering the lattice points sampled during
        extraction, which can extend beyond the clipping bounds. Use these bounds
        when preparing an evaluator for the same resolution and transform.

    Raises
    ------
    ValueError
        If the bounds, resolution, or sampling transform are invalid.
    """
    ...

class ClusterMethod(Enum):
    """Vertex clustering mode."""

    None_ = 0
    """No vertex clustering is performed. Raw marching tetrahedra triangles are produced."""
    Average = 1
    """Cluster topology-compatible intersections to their arithmetic mean."""

    CurvatureWeighted = 2
    """Cluster topology-compatible intersections using the local curvature estimate."""

class BoundaryClosure(Enum):
    """Boundary closure mode for isosurfaces."""

    None_ = 0
    """Do not add cap triangles; leave the clipped surface open."""
    ClosePositive = 1
    """Close the surface as if values outside the AABB are above the isovalue."""
    CloseNegative = 2
    """Close the surface as if values outside the AABB are below the isovalue."""


class Mesh:
    """Triangle mesh returned by isosurface extraction."""

    def save_obj(self, path: str, name: str) -> None:
        """Save this mesh to a Wavefront OBJ file.

        Parameters
        ----------
        path : str
            File path to save the obj to.
        name : str
            Object name for the mesh.
        """
        ...

    @property
    def vertices(self) -> npt.NDArray[np.float64]: 
        """Vertex coordinates with shape (V, 3).

        Returns
        -------
        npt.NDArray[np.float64]
            Array of the vertices.
        """    
        ...

    @property
    def facets(self) -> npt.NDArray[np.uintp]: 
        """Triangle vertex indices with shape (F, 3).

        Returns
        -------
        npt.NDArray[np.uintp]
            Array of triangles.
        """
        ...

def build_isosurface(
    seed_points: npt.NDArray[np.float64],
    extents: npt.NDArray[np.float64],
    resolution: float,
    isovalue: float,
    surface_fn: Callable[[npt.NDArray[np.float64]], npt.NDArray[np.float64]],
    *,
    sampling_transform: npt.NDArray[np.float64] | None = None,
    gradient_fn: Optional[
        Callable[
            [npt.NDArray[np.float64]],
            tuple[npt.NDArray[np.float64], npt.NDArray[np.float64]],
        ]
    ] = None,
    cluster_method: ClusterMethod = ClusterMethod.CurvatureWeighted,
    boundary_closure: BoundaryClosure = BoundaryClosure.None_,
    progress_callback: Optional[Progress] = None,
) -> Mesh:
    """Extract an isosurface using regularised marching tetrahedra.

    Parameters
    ----------
    seed_points : npt.NDArray[np.float64]
        Numpy array of points of shape (N, 3), where N is the number of seed points used to
        initialise the surface-following extraction.
    extents : npt.NDArray[np.float64]
        Axis-aligned bounding box limiting the extracted mesh, with shape (6,) and order
        [xmin, ymin, zmin, xmax, ymax, zmax].
    resolution : float
        Sampling resolution used by the extraction lattice.
    isovalue : float
        The value at which to extract the isosurface.
    surface_fn : Callable[[npt.NDArray[np.float64]], npt.NDArray[np.float64]]
        Callable function to evaluate lattice sample points during isosurface extraction.
        Must take in a 2D numpy array of float64 3D point coordinates of shape (N, 3) and
        return a float64 values array of shape (N,) or (N, 1), where N is the number of points
        being evaluated. Single-column scalar values are returned to Python as shape (N,).
    sampling_transform : npt.NDArray[np.float64] | None, optional
        Optional affine transform applied to the sampling lattice to control its
        orientation and relative spacing. Provide the 3 x 3 linear part of the
        transform from world coordinates to sampling coordinates.
        If None, the default lattice is used. The resolution controls the overall
        sampling distance, so uniform scaling of the transform has no effect.

        This is useful for surfaces with a strong directional trend.
        Aligning the lattice with the structure allows
        finer sampling across thin features and coarser sampling along smoother
        directions.
    gradient_fn : Callable | None, optional
        Optional callable function to evaluate values and gradients for seed projection. Values
        may have shape (N,) or (N, 1); gradients must have shape (N, 3).
    cluster_method : ClusterMethod
        [`ClusterMethod`][ferreus_rmt.ClusterMethod] used to combine local vertex candidates.
    boundary_closure : BoundaryClosure
        [`BoundaryClosure`][ferreus_rmt.BoundaryClosure] mode for the extracted mesh.
    progress_callback : Progress | None, optional
        Optional callback for reporting extraction progress.

    Returns
    -------
    Mesh
        Extracted triangle mesh.
    """
    ...

def build_isosurfaces(
    seed_points: npt.NDArray[np.float64],
    extents: npt.NDArray[np.float64],
    resolution: float,
    isovalues: list[float],
    isosurface_fn: Callable[[npt.NDArray[np.float64]], npt.NDArray[np.float64]],
    *,
    sampling_transform: npt.NDArray[np.float64] | None = None,
    gradient_fn: Optional[
        Callable[
            [npt.NDArray[np.float64]],
            tuple[npt.NDArray[np.float64], npt.NDArray[np.float64]],
        ]
    ] = None,
    cluster_method: ClusterMethod = ClusterMethod.CurvatureWeighted,
    boundary_closure: BoundaryClosure = BoundaryClosure.None_,
    progress_callback: Optional[Progress] = None,
) -> list[Mesh]:
    """Convenience wrapper for [`build_isosurface`][ferreus_rmt.build_isosurface] that
    can extract multiple meshes from a list of isovalues at once.

    Parameters
    ----------
    seed_points : npt.NDArray[np.float64]
        Numpy array of points of shape (N, 3), where N is the number of seed points used to
        initialise the surface-following extraction.
    extents : npt.NDArray[np.float64]
        Axis-aligned bounding box limiting the extracted mesh, with shape (6,) and order
        [xmin, ymin, zmin, xmax, ymax, zmax].
    resolution : float
        Sampling resolution used by the extraction lattice.
    isovalues : list[float]
        List of values at which to extract isosurfaces.
    isosurface_fn : Callable[[npt.NDArray[np.float64]], npt.NDArray[np.float64]]
        Callable function to evaluate lattice sample points during isosurface extraction.
        Must take in a 2D numpy array of float64 3D point coordinates of shape (N, 3) and
        return a float64 values array of shape (N,) or (N, 1), where N is the number of points
        being evaluated. Single-column scalar values are returned to Python as shape (N,).
    sampling_transform : npt.NDArray[np.float64] | None, optional
        Optional affine transform applied to the sampling lattice to control its
        orientation and relative spacing. Provide the 3 x 3 linear part of the
        transform from world coordinates to sampling coordinates.
        If None, the default lattice is used. The resolution controls the overall
        sampling distance, so uniform scaling of the transform has no effect.

        This is useful for surfaces with a strong directional trend.
        Aligning the lattice with the structure allows
        finer sampling across thin features and coarser sampling along smoother
        directions.
    gradient_fn : Callable | None, optional
        Optional callable function to evaluate values and gradients for seed projection. Values
        may have shape (N,) or (N, 1); gradients must have shape (N, 3).
    cluster_method: ClusterMethod | ClusterMethod.CurvatureWeighted, optional
        [`ClusterMethod`][ferreus_rmt.ClusterMethod] to use. If not provided,
        `CurvatureWeighted` will be used.
    boundary_closure : BoundaryClosure | BoundaryClosure.None_, optional
        [`BoundaryClosure`][ferreus_rmt.BoundaryClosure] mode to use. If `None_`, leaves clipped
        boundaries open.
    progress_callback : Progress | None, optional
        Optional callback for reporting extraction progress.

    Returns
    -------
    list[Mesh]
        Extracted triangle mesh.
    """
    ...
