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
        "--backup",
        action="store_true",
        help="Create a backup of your profile"
    )
    
    parser.add_argument(
        "prompt",
        nargs="?",
        help="Prompt for pose generation"
    )
    
    args = parser.parse_args()
    
    # Handle backup command
    if args.backup:
        try:
            from .core import backup_profile
            if backup_profile():
                print("Profile backed up successfully to profile.json.backup")
            else:
                print("Error: No profile found to backup")
                sys.exit(1)
        except Exception as e:
            print(f"Error creating backup: {e}")
            sys.exit(1)
        return
    
    # Check profile status first
    try:
        from .core import get_profile_status
        is_new_user, profile = get_profile_status()
        
        if is_new_user:
            print("Hey, you're new! Let me set you up!")
            print("Welcome! Creating your profile...")
        else:
            sample_count = len(profile.get("samples", []))
            print(f"Profile loaded with {sample_count} writing samples")
            
    except Exception as e:
        print(f"Error initializing profile: {e}")
        sys.exit(1)
    
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
            print("I'd generate text but that's not built yet")
            sys.exit(1)
    else:
        # Just show the profile status and exit gracefully
        # The profile message was already shown above
        pass

if __name__ == "__main__":
    main()
