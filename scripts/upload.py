import subprocess
import sys
from pathlib import Path
import argparse

from scripts.common import eprint


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Upload .conda files to a specified channel."
    )
    parser.add_argument(
        "--channel", required=True, help="The channel to upload the .conda files to."
    )
    args = parser.parse_args()

    exit_code = 0

    for conda_file in Path("output").glob("**/*.conda"):
        command = [
            "rattler-build",
            "upload",
            "prefix",
            "--channel",
            args.channel,
            str(conda_file),
        ]
        print(f"Running command: {' '.join(command)}")
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            eprint(f"Error uploading {conda_file}: {result.stderr}")
            exit_code = 1

    sys.exit(exit_code)


if __name__ == "__main__":
    main()