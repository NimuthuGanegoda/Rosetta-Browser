from rosetta_browser.core.engine import BrowserData, BrowserEngine


class GeckoEngine(BrowserEngine):
    @property
    def name(self) -> str:
        return "Gecko"

    def extract_data(self, profile_path: str) -> BrowserData:
        # print(f"Gecko: Extracting data from {profile_path}")
        # Mock data
        return BrowserData()

    def inject_data(self, profile_path: str, data: BrowserData) -> None:
        # print(f"Gecko: Injecting data into {profile_path}")
        pass
