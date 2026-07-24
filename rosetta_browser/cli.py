import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Rosetta-Browser: Cross-Engine Browser Data Migration Tool")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # List command
    list_parser = subparsers.add_parser("list-engines", help="List supported browser engines")

    # Migrate command
    migrate_parser = subparsers.add_parser("migrate", help="Migrate data between browsers")
    migrate_parser.add_argument("--source", required=True, help="Source browser engine")
    migrate_parser.add_argument("--source-profile", required=True, help="Path to source profile")
    migrate_parser.add_argument("--target", required=True, help="Target browser engine")
    migrate_parser.add_argument("--target-profile", required=True, help="Path to target profile")

    # Extension command
    ext_parser = subparsers.add_parser("recommend-extensions", help="Generate extension recommendations")
    ext_parser.add_argument("--source", required=True, help="Source browser engine")
    ext_parser.add_argument("--source-profile", required=True, help="Path to source profile")
    ext_parser.add_argument("--target", required=True, help="Target browser engine")
    ext_parser.add_argument("--json", action="store_true", help="Output recommendations as JSON")

    return parser.parse_args()
