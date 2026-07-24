from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


@dataclass
class ExtensionData:
    id: str
    name: str
    version: str
    install_url: str | None = None
    enabled: bool = True
    developer: str | None = None

@dataclass
class BrowserData:
    history: list[dict[str, Any]] = field(default_factory=list)
    cookies: list[dict[str, Any]] = field(default_factory=list)
    extensions: list[ExtensionData] = field(default_factory=list)
    # Placeholder for session data, bookmarks, login data etc.
    session_data: dict[str, Any] = field(default_factory=dict)

class BrowserEngine(ABC):
    """Abstract base class for browser engines."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the name of the browser engine (e.g., 'Chrome', 'Firefox')."""

    @abstractmethod
    def extract_data(self, profile_path: str) -> BrowserData:
        """Extract data from a browser profile."""

    @abstractmethod
    def inject_data(self, profile_path: str, data: BrowserData) -> None:
        """Inject data into a browser profile."""
