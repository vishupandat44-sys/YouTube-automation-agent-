import argparse
import sys
import os
from typing import Optional
from src.generator import ShortsGenerator, PRESET_TOPICS

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="YouTube Cartoon Shorts Automation Generator"
    )
    parser.add_argument(
        "-t", "--topic",
        type=str,
        default=None,
        help=f"Topic or preset theme for the short ({', '.join(PRESET_TOPICS.keys())})"
    )
    parser.add_argument(
        "--title",
        type=str,
        default=None,
        help="Custom title for the Cartoon Short"
    )
    parser.add_argument(
        "-d", "--duration",
        type=float,
        default=45.0,
        help="Target duration in seconds (e.g. 30, 45, 60)"
    )
    parser.add_argument(
        "-f", "--format",
        type=str,
        choices=["markdown", "json", "text"],
        default="markdown",
        help="Output format (markdown, json, text)"
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        default=None,
        help="File path to save the generated output"
    )
    parser.add_argument(
        "--list-topics",
        action="store_true",
        help="List available preset topics"
    )
    return parser

def run_cli(args: Optional[list] = None) -> int:
    parser = create_parser()
    parsed_args = parser.parse_args(args)

    if parsed_args.list_topics:
        print("Available Preset Topics:")
        for topic, data in PRESET_TOPICS.items():
            print(f" - {topic}: {data['title']} (Moral: {data['moral']})")
        return 0

    generator = ShortsGenerator()
    package = generator.generate_short(
        topic=parsed_args.topic,
        custom_title=parsed_args.title,
        duration=parsed_args.duration
    )

    if parsed_args.format == "json":
        output_content = package.to_json()
    elif parsed_args.format == "text":
        output_content = package.to_text()
    else:
        output_content = package.to_markdown()

    if parsed_args.output:
        os.makedirs(os.path.dirname(os.path.abspath(parsed_args.output)), exist_ok=True)
        with open(parsed_args.output, "w", encoding="utf-8") as f:
            f.write(output_content)
        print(f"Cartoon Short package successfully saved to: {parsed_args.output}")
    else:
        print(output_content)

    return 0
