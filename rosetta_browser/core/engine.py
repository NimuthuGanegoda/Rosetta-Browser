from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field

@dataclass
class ExtensionData:
    id: str
    name: str
    version: str
    install_url: Optional[str] = None
    enabled: bool = True
    developer: Optional[str] = None

@dataclass
class BrowserData:
    history: List[Dict[str, Any]] = field(default_factory=list)
    cookies: List[Dict[str, Any]] = field(default_factory=list)
    extensions: List[ExtensionData] = field(default_factory=list)
    # Placeholder for session data, bookmarks, login data etc.
    session_data: Dict[str, Any] = field(default_factory=dict)

class BrowserEngine(ABC):
    """Abstract base class for browser engines."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the name of the browser engine (e.g., 'Chrome', 'Firefox')."""
        pass

    @abstractmethod
    def extract_data(self, profile_path: str) -> BrowserData:
        """Extract data from a browser profile."""
        pass

    @abstractmethod
    def inject_data(self, profile_path: str, data: BrowserData) -> None:
        """Inject data into a browser profile."""
        pass
