#!/usr/bin/env python3
import importlib
import pkgutil
import sys

from rosetta_browser import engines
from rosetta_browser.cli import parse_args
from rosetta_browser.core.engine import BrowserEngine
from rosetta_browser.features.extension_rosetta import ExtensionRosetta

# Registry for browser engines
ENGINE_REGISTRY: dict[str, BrowserEngine] = {}

def register_engine(engine: BrowserEngine):
    ENGINE_REGISTRY[engine.name] = engine

def load_plugins():
    """
    Dynamically load plugins from the engines directory.
    """
    path = engines.__path__
    prefix = engines.__name__ + "."

    for _, name, _ in pkgutil.iter_modules(path, prefix):
        try:
            # We enforce a convention that the engine implementation is in 'engine.py'
            # inside the plugin package.
            engine_module_name = f"{name}.engine"
            engine_module = importlib.import_module(engine_module_name)

            for attribute_name in dir(engine_module):
                attribute = getattr(engine_module, attribute_name)
                if isinstance(attribute, type) and issubclass(attribute, BrowserEngine) and attribute is not BrowserEngine:
                     register_engine(attribute())
        except ImportError:
            # If engine.py doesn't exist or fails to import, skip it
            continue
        except Exception as e:
            print(f"Failed to load plugin {name}: {e}")

def main():
    args = parse_args()
    load_plugins()

    if args.command == "list-engines":
        print("Supported Engines:")
        for name in ENGINE_REGISTRY:
            print(f"- {name}")

    elif args.command == "migrate":
        if args.source not in ENGINE_REGISTRY:
            print(f"Error: Source engine '{args.source}' not supported.")
            sys.exit(1)
        if args.target not in ENGINE_REGISTRY:
            print(f"Error: Target engine '{args.target}' not supported.")
            sys.exit(1)

        source_engine = ENGINE_REGISTRY[args.source]
        target_engine = ENGINE_REGISTRY[args.target]

        print(f"Migrating from {source_engine.name} to {target_engine.name}...")
        try:
            data = source_engine.extract_data(args.source_profile)
            target_engine.inject_data(args.target_profile, data)
            print("Migration complete.")
        except Exception as e:
            print(f"Error during migration: {e}")
            sys.exit(1)

    elif args.command == "recommend-extensions":
        if args.source not in ENGINE_REGISTRY:
            print(f"Error: Source engine '{args.source}' not supported.")
            sys.exit(1)

        source_engine = ENGINE_REGISTRY[args.source]
        rosetta = ExtensionRosetta()

        if not args.json:
            print(f"Analyzing extensions from {source_engine.name}...")
        try:
            data = source_engine.extract_data(args.source_profile)
            recommendations = rosetta.translate_extensions(data.extensions, args.target)

            if args.json:
                import json
                print(json.dumps(recommendations, indent=2))
            else:
                print("Recommended Extensions:")
                for rec in recommendations:
                    print(f"- {rec['source_name']} -> {rec['recommended_url']}")
        except Exception as e:
            if args.json:
                import json
                print(json.dumps({"error": str(e)}))
            else:
                print(f"Error generating recommendations: {e}")
            sys.exit(1)
    else:
        print("No command specified. Use --help for usage information.")

if __name__ == "__main__":
    main()
