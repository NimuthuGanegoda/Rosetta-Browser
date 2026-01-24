from rosetta_browser.core.engine import BrowserEngine, BrowserData, ExtensionData

class BlinkEngine(BrowserEngine):
    @property
    def name(self) -> str:
        return "Blink"

    def extract_data(self, profile_path: str) -> BrowserData:
        # In a real app, use logging
        # print(f"Blink: Extracting data from {profile_path}")
        # Mock data
        return BrowserData(
            extensions=[
                ExtensionData(id="ext1", name="AdBlock", version="1.0"),
                ExtensionData(id="ext2", name="PasswordManager", version="2.0")
            ]
        )

    def inject_data(self, profile_path: str, data: BrowserData) -> None:
        # print(f"Blink: Injecting data into {profile_path}")
        pass
