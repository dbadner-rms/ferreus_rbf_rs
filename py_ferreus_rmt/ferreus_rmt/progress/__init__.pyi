from typing import Callable, Optional, Union

class IsosurfaceProgress:
    """
    Event indicating progress for isosurface extraction.

    Attributes
    ----------
    isovalue : float
        Isovalue currently being surfaced.
    stage : str
        Human-readable extraction stage.
    progress : float
        Fraction in ``[0, 1]`` indicating overall progress.
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
    """Marker exported by the extension; callbacks receive IsosurfaceProgress or Message."""

ProgressCallback = Callable[[Union[IsosurfaceProgress, Message]], None]
"""Callable accepting a concrete event payload and returning ``None``."""

class Progress:
    """
    Wrapper for progress event reporting.

    Parameters
    ----------
    callback : ProgressCallback, optional
        Function invoked with each :data:`ProgressEvent`.
    """
    def __init__(
        self,
        callback: Optional[ProgressCallback] = None,
    ) -> None: ...
