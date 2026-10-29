"""Grounded Q&A entrypoint (stub)."""

from __future__ import annotations
import argparse


def answer(query: str) -> str:
    return (
        f"Stub answer for: {query}\n"
        "Wire retrieve.py + your LLM provider to return cited responses."
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", required=True)
    args = parser.parse_args()
    print(answer(args.query))


if __name__ == "__main__":
    main()
