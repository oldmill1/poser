#!/usr/bin/env python3
"""
Command-line interface for Poser.
"""

import argparse
import sys
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Poser - AI-powered posing and image generation",
        prog="poser"
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version="Poser 0.1.0"
    )
    
    parser.add_argument(
        "--api-key",
        help="OpenAI API key (or set OPENAI_API_KEY environment variable)"
    )
    
    parser.add_argument(
        "--model",
        default=os.getenv("MODEL", "gpt-4o"),
        help="AI model to use (default: gpt-4o)"
    )
    
    parser.add_argument(
        "prompt",
        nargs="?",
        help="Prompt for pose generation"
    )
    
    args = parser.parse_args()
    
    # Get API key
    api_key = args.api_key or os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OpenAI API key is required. Set OPENAI_API_KEY environment variable or use --api-key")
        sys.exit(1)
    
    if args.prompt:
        # Import and use the main functionality
        try:
            from .core import generate_pose
            result = generate_pose(args.prompt, api_key, args.model)
            print(result)
        except ImportError:
            print("Error: Core functionality not yet implemented")
            sys.exit(1)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
