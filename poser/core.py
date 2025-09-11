#!/usr/bin/env python3
"""
Poser - A simple Python library
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional

def get_profile_path() -> Path:
    """Get the path to the user's profile file."""
    home_dir = Path.home()
    poser_dir = home_dir / ".poser"
    return poser_dir / "profile.json"

def create_profile_dir() -> Path:
    """Create the ~/.poser directory if it doesn't exist."""
    profile_path = get_profile_path()
    profile_path.parent.mkdir(exist_ok=True)
    return profile_path.parent

def create_default_profile() -> Dict[str, Any]:
    """Create a default profile structure."""
    return {
        "version": "0.1.0",
        "created": datetime.now().strftime("%Y-%m-%d"),
        "samples": [],
        "style_summary": {},
        "preferences": {}
    }

def create_sample_structure(user_label: str, text: str) -> Dict[str, Any]:
    """Create a sample structure with user label and text."""
    sample_id = f"sample_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    word_count = len(text.split())
    
    return {
        "id": sample_id,
        "user_label": user_label,
        "text": text,
        "added_date": datetime.now().strftime("%Y-%m-%d"),
        "word_count": word_count,
        "ai_analysis": {
            "type": None,        # Will be filled by AI analysis
            "tone": None,        # Will be filled by AI analysis
            "audience": None,    # Will be filled by AI analysis
            "purpose": None,     # Will be filled by AI analysis
            "tags": []          # Will be filled by AI analysis
        }
    }

def load_profile() -> Optional[Dict[str, Any]]:
    """Load the user's profile from disk."""
    profile_path = get_profile_path()
    
    if not profile_path.exists():
        return None
    
    try:
        with open(profile_path, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return None

def save_profile(profile: Dict[str, Any]) -> bool:
    """Save the user's profile to disk."""
    try:
        create_profile_dir()
        profile_path = get_profile_path()
        
        with open(profile_path, 'w') as f:
            json.dump(profile, f, indent=2)
        return True
    except IOError:
        return False

def initialize_profile() -> Dict[str, Any]:
    """Initialize a new profile for first-time users."""
    profile = create_default_profile()
    if save_profile(profile):
        return profile
    else:
        raise RuntimeError("Failed to create profile")

def backup_profile() -> bool:
    """
    Create a backup of the current profile.
    
    Returns:
        bool: True if backup was successful, False otherwise
    """
    profile = load_profile()
    if profile is None:
        return False
    
    try:
        create_profile_dir()
        profile_path = get_profile_path()
        backup_path = profile_path.with_suffix('.json.backup')
        
        with open(backup_path, 'w') as f:
            json.dump(profile, f, indent=2)
        return True
    except IOError:
        return False

def delete_profile() -> bool:
    """
    Delete the current profile file.
    
    Returns:
        bool: True if deletion was successful, False otherwise
    """
    profile_path = get_profile_path()
    
    if not profile_path.exists():
        return False
    
    try:
        profile_path.unlink()
        return True
    except IOError:
        return False

def backup_and_delete_profile() -> bool:
    """
    Create a backup of the current profile and then delete it.
    
    Returns:
        bool: True if both operations were successful, False otherwise
    """
    # First create backup
    if not backup_profile():
        return False
    
    # Then delete the original profile
    return delete_profile()

def add_sample_to_profile(user_label: str, text: str) -> bool:
    """
    Add a new writing sample to the user's profile.
    
    Args:
        user_label: User's personal label for the sample
        text: The actual writing sample text
        
    Returns:
        bool: True if sample was added successfully, False otherwise
    """
    profile = load_profile()
    if profile is None:
        return False
    
    # Create new sample structure
    new_sample = create_sample_structure(user_label, text)
    
    # Add to samples list
    profile["samples"].append(new_sample)
    
    # Save updated profile
    return save_profile(profile)

def get_profile_status() -> tuple[bool, Optional[Dict[str, Any]]]:
    """
    Check profile status and return (is_new_user, profile_data).
    
    Returns:
        tuple: (is_new_user, profile_data)
    """
    profile = load_profile()
    is_new_user = profile is None
    
    if is_new_user:
        try:
            profile = initialize_profile()
        except RuntimeError:
            return True, None
    
    return is_new_user, profile

def main():
    """Main entry point when running the script directly"""
    print("Hello World")

if __name__ == "__main__":
    main()
