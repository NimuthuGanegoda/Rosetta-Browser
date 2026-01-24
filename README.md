# Rosetta-Browser

Rosetta-Browser is a "next-level" browser data migration tool designed to bridge the gap between different browser engines (Blink, Gecko, WebKit).

## Core Features

*   **Cross-Engine Translation**: Intelligently migrate data from Chromium-based browsers (Chrome, Brave, Edge) to Firefox-based browsers (Firefox, Librewolf) and vice-versa.
*   **Extension Rosetta**: Identifies extensions by name/developer and finds the equivalent install URL for the target browser.
*   **Engine Abstraction Layer**: Modular architecture for Blink, Gecko, and WebKit engines.
*   **Forensic Continuity**: Migrates the "Current Session" (open tabs and windows).
*   **Security**: Handles OS-level encryption (DPAPI/Libsecret) securely.

## Architecture

Rosetta-Browser uses a plugin-based architecture. New browser support can be added by implementing the `BrowserEngine` interface in the `engines` directory.

### Directory Structure

*   `rosetta_browser/`: Main package
    *   `core/`: Core logic and abstractions
    *   `engines/`: Browser engine implementations (plugins)
    *   `features/`: Feature implementations (Extension Rosetta, Crypto, Session)
    *   `utils/`: Utility functions

## Usage

(To be implemented)

Run the tool using the CLI:

```bash
python -m rosetta_browser --help
```
