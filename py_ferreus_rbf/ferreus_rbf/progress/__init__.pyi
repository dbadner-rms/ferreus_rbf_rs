from typing import Callable, Union, Optional

class DuplicatesRemoved:
    """
    Event indicating that duplicate input points were removed.

    Attributes
    ----------
    num_duplicates : int
        Number of points removed as duplicates.
    """
    num_duplicates: int

class SolverIteration:
    """
    Event indicating iteration status for an iterative solver.

    Attributes
    ----------
    iter : int
        Zero-based iteration counter.
    residual : float
        Current residual norm.
    progress : float
        Fraction in ``[0, 1]`` indicating overall progress.
    """
    iter: int
    residual: float
    progress: float

class SurfacingProgress:
    """
    Even indicating progress for isosurface extraction.

    Attributes
    ----------
    isovalue : float
        Isovalue currently being surfaced.
    stage : str
        Human-readable stage name (e.g., ``"Calculating surface intersections"``, ``"Building faces"``).
    progress : float
        Fraction in ``[0, 1]`` for the current isovalue.
    """    
    isovalue: float
    stage: str
    progress: float

class Message:
    """
    Arbitrary informational message.

    Attributes
    ----------
    message : str
        The message text.
    """    
    message: str

class ProgressEvent:
    """Marker exported by the extension; callbacks receive the concrete payload classes above."""

ProgressCallback = Callable[[Union[SolverIteration, DuplicatesRemoved, SurfacingProgress, Message]], None]
"""Callable accepting a concrete event payload and returning ``None``."""

class Progress:
    """
    Wrapper for progress event reporting.

    Parameters
    ----------
    callback : ProgressCallback, optional
        Function invoked with each :data:`ProgressEvent`.

    Notes
    -----
    Use this to receive events from long-running operations such as DDM/FGMRES
    solves and isosurface extraction.
    """    
    def __init__(
        self,
        callback: Optional[ProgressCallback] = None,
    ) -> None: ...
