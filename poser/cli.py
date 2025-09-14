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
        description="Poser - AI-powered writing and communication assistant",
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
        "--backup-and-delete",
        action="store_true",
        help="Create a backup of your profile and delete it (start fresh)"
    )
    
    parser.add_argument(
        "--override",
        action="store_true",
        help="Use closest samples even if they don't meet minimum score threshold"
    )
    
    parser.add_argument(
        "--personality",
        help="Specify which personality to use for text generation (required)"
    )
    
    # Handle add-sample as a special case
    if len(sys.argv) > 1 and sys.argv[1] == "add-sample":
        if len(sys.argv) < 5:
            print("Usage: poser add-sample <personality> <label> <text>")
            print("Example: poser add-sample 'casual' 'slack message' 'hey team, quick update...'")
            sys.exit(1)
        personality = sys.argv[2]
        user_label = sys.argv[3]
        text = " ".join(sys.argv[4:])
        
        # Get API key for AI analysis
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            print("Warning: No OPENAI_API_KEY found. Sample will be saved without AI analysis.")
            print("Set OPENAI_API_KEY environment variable to enable AI analysis.")
        
        try:
            from .core import add_sample_to_profile
            if add_sample_to_profile(personality, user_label, text, api_key):
                print(f"Sample added successfully with personality: '{personality}' and label: '{user_label}'")
                print(f"Text: {text[:50]}{'...' if len(text) > 50 else ''}")
            else:
                print("Error: Failed to add sample to profile")
                sys.exit(1)
        except Exception as e:
            print(f"Error adding sample: {e}")
            sys.exit(1)
        return
    
    # Handle remove-sample as a special case
    if len(sys.argv) > 1 and sys.argv[1] == "remove-sample":
        if len(sys.argv) < 3:
            print("Usage: poser remove-sample <sample_id>")
            print("Use 'poser list-samples' to see available sample IDs")
            sys.exit(1)
        sample_id = sys.argv[2]
        
        try:
            from .core import remove_sample_from_profile
            if remove_sample_from_profile(sample_id):
                print(f"Sample {sample_id} removed successfully")
            else:
                print(f"Error: Sample {sample_id} not found")
                sys.exit(1)
        except Exception as e:
            print(f"Error removing sample: {e}")
            sys.exit(1)
        return
    
    # Handle list-samples as a special case
    if len(sys.argv) > 1 and sys.argv[1] == "list-samples":
        try:
            from .core import list_samples
            samples = list_samples()
            if samples is None:
                print("No profile found")
                sys.exit(1)
            elif not samples:
                print("No samples found in profile")
            else:
                print(f"Found {len(samples)} samples:")
                print()
                for sample in samples:
                    print(f"ID: {sample['id']}")
                    print(f"Label: {sample['user_label']}")
                    print(f"Text: {sample['text'][:60]}{'...' if len(sample['text']) > 60 else ''}")
                    print(f"Analysis: {sample['ai_analysis']['type']} | {sample['ai_analysis']['tone']} | {sample['ai_analysis']['audience']} | {sample['ai_analysis']['purpose']}")
                    print("-" * 50)
        except Exception as e:
            print(f"Error listing samples: {e}")
            sys.exit(1)
        return
    
    parser.add_argument(
        "prompt",
        nargs="?",
        help="Writing prompt or text to process"
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
    
    # Handle backup-and-delete command
    if args.backup_and_delete:
        try:
            from .core import backup_and_delete_profile
            if backup_and_delete_profile():
                print("Profile backed up and deleted successfully. Next run will create a fresh profile.")
            else:
                print("Error: No profile found to backup and delete")
                sys.exit(1)
        except Exception as e:
            print(f"Error backing up and deleting profile: {e}")
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
            result = generate_pose(args.prompt, api_key, args.model, args.override, args.personality)
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
