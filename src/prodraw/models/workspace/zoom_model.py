class ZoomModel:
    """Holds the zoom state. Class-level attributes keep zoom global."""

    factor: float = 1.0
    STEP:   float = 0.1
    MIN:    float = 0.1
    MAX:    float = 3.0
