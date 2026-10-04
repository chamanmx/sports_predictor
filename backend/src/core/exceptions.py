class SportsPredictorError(Exception):
    """Base application exception."""


class ScraperError(SportsPredictorError):
    """Raised when a scraper fails to fetch or parse page data."""


class SportsDataError(SportsPredictorError):
    """Raised when sports data retrieval fails."""


class PredictionError(SportsPredictorError):
    """Raised when feature extraction or prediction fails."""


class DatabaseError(SportsPredictorError):
    """Raised when database operations fail."""


class ModelNotTrainedError(SportsPredictorError):
    """Raised when attempting predictions with untrained model."""
