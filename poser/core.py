#!/usr/bin/env python3
"""
Poser - A simple Python library
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional
import openai

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

def create_sample_structure(personality: str, user_label: str, text: str) -> Dict[str, Any]:
    """Create a sample structure with personality, user label and text."""
    sample_id = f"sample_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    word_count = len(text.split())
    
    return {
        "id": sample_id,
        "personality": personality,
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

def analyze_sample_with_ai(text: str, api_key: str) -> Optional[Dict[str, Any]]:
    """
    Send a writing sample to AI for analysis and categorization.
    
    Args:
        text: The writing sample text to analyze
        api_key: OpenAI API key
        
    Returns:
        Dict with analysis results or None if analysis failed
    """
    try:
        client = openai.OpenAI(api_key=api_key)
        
        prompt = f"""Analyze this writing sample and categorize it:

Text: "{text}"

Please return a JSON object with:
- type: email/slack/text/formal document
- tone: casual/formal/frustrated/polite/urgent/neutral
- audience: team/client/personal/external/colleague
- purpose: update/request/complaint/inquiry/response/informational
- tags: array of 2-5 relevant keywords

Return only valid JSON, no other text."""
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Using mini for cost efficiency
            messages=[
                {"role": "system", "content": "You are a writing style analyst. Always return valid JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1,  # Low temperature for consistent categorization
            max_tokens=200
        )
        
        # Parse the JSON response
        analysis_text = response.choices[0].message.content.strip()
        analysis = json.loads(analysis_text)
        
        # Validate the structure
        required_fields = ["type", "tone", "audience", "purpose", "tags"]
        if all(field in analysis for field in required_fields):
            return analysis
        else:
            return None
            
    except Exception as e:
        print(f"AI analysis failed: {e}")
        return None

def analyze_request_with_ai(user_request: str, api_key: str) -> Optional[Dict[str, Any]]:
    """
    Analyze a user's writing request to understand what they want to write.
    
    Args:
        user_request: The user's request (e.g., "write a slack message about my new app")
        api_key: OpenAI API key
        
    Returns:
        Dict with request analysis or None if analysis failed
    """
    try:
        client = openai.OpenAI(api_key=api_key)
        
        prompt = f"""Analyze this writing request and categorize what the user wants to write:

Request: "{user_request}"

The user may specify the communication type explicitly ("write a slack message") or implicitly ("slack: tell team about app" or "email my boss"). Infer the type from context if not explicitly stated.

Please return a JSON object with:
- type: email/slack/text/formal document (infer from context if not explicit)
- audience: team/client/personal/external/colleague
- purpose: update/request/complaint/inquiry/announcement/response/informational
- topic: brief description of what they want to write about

Return only valid JSON, no other text."""
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Using mini for cost efficiency
            messages=[
                {"role": "system", "content": "You are a writing request analyzer. Always return valid JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1,  # Low temperature for consistent categorization
            max_tokens=150
        )
        
        # Parse the JSON response
        analysis_text = response.choices[0].message.content.strip()
        analysis = json.loads(analysis_text)
        
        # Validate the structure
        required_fields = ["type", "audience", "purpose", "topic"]
        if all(field in analysis for field in required_fields):
            return analysis
        else:
            return None
            
    except Exception as e:
        print(f"Request analysis failed: {e}")
        return None

def add_sample_to_profile(personality: str, user_label: str, text: str, api_key: Optional[str] = None) -> bool:
    """
    Add a new writing sample to the user's profile.
    
    Args:
        personality: The personality name for this sample
        user_label: User's personal label for the sample
        text: The actual writing sample text
        api_key: Optional API key for AI analysis
        
    Returns:
        bool: True if sample was added successfully, False otherwise
    """
    profile = load_profile()
    if profile is None:
        return False
    
    # Create new sample structure
    new_sample = create_sample_structure(personality, user_label, text)
    
    # Run AI analysis if API key is provided
    if api_key:
        print("Analyzing writing style...")
        analysis = analyze_sample_with_ai(text, api_key)
        if analysis:
            new_sample["ai_analysis"] = analysis
            print("✓ AI analysis complete")
        else:
            print("⚠ AI analysis failed, sample saved without analysis")
    
    # Add to samples list
    profile["samples"].append(new_sample)
    
    # Save updated profile
    return save_profile(profile)

def remove_sample_from_profile(sample_id: str) -> bool:
    """
    Remove a writing sample from the user's profile by ID.
    
    Args:
        sample_id: The ID of the sample to remove
        
    Returns:
        bool: True if sample was removed successfully, False otherwise
    """
    profile = load_profile()
    if profile is None:
        return False
    
    # Find and remove the sample
    original_count = len(profile["samples"])
    profile["samples"] = [sample for sample in profile["samples"] if sample["id"] != sample_id]
    
    # Check if a sample was actually removed
    if len(profile["samples"]) < original_count:
        # Save updated profile
        return save_profile(profile)
    else:
        return False  # Sample not found

def list_samples() -> Optional[list]:
    """
    List all samples in the user's profile.
    
    Returns:
        List of sample dictionaries or None if no profile exists
    """
    profile = load_profile()
    if profile is None:
        return None
    
    return profile.get("samples", [])

def find_relevant_samples(request_analysis: Dict[str, Any], min_score: int = 4, override: bool = False, personality: Optional[str] = None) -> list[Dict[str, Any]]:
    """
    Find writing samples that match a request analysis based on scoring criteria.
    
    Args:
        request_analysis: Analysis of the user's request (from analyze_request_with_ai)
        min_score: Minimum score required for a sample to be considered relevant (default: 4)
        override: If True, include samples with any score > 0 even if below min_score
        personality: If provided, only include samples from this personality
        
    Returns:
        List of relevant samples with their scores, sorted by score (highest first)
    """
    profile = load_profile()
    if profile is None or not profile.get("samples"):
        return []
    
    scored_samples = []
    
    for sample in profile["samples"]:
        if not sample.get("ai_analysis"):
            continue  # Skip samples without AI analysis
            
        # Filter by personality if specified
        if personality and sample.get("personality") != personality:
            continue  # Skip samples from different personalities
            
        sample_analysis = sample["ai_analysis"]
        score = 0
        score_details = []
        
        # Score based on type match (2 points)
        if sample_analysis.get("type") == request_analysis.get("type"):
            score += 2
            score_details.append("type match (+2)")
        
        # Score based on audience match (2 points)
        if sample_analysis.get("audience") == request_analysis.get("audience"):
            score += 2
            score_details.append("audience match (+2)")
        
        # Score based on purpose match (1 point)
        if sample_analysis.get("purpose") == request_analysis.get("purpose"):
            score += 1
            score_details.append("purpose match (+1)")
        
        # Score based on tone appropriateness (1 point)
        # For casual audiences (team/colleague), prefer casual tone
        # For formal audiences (client/external), prefer formal tone
        request_audience = request_analysis.get("audience", "")
        sample_tone = sample_analysis.get("tone", "")
        
        if request_audience in ["team", "colleague"] and sample_tone == "casual":
            score += 1
            score_details.append("casual tone for team (+1)")
        elif request_audience in ["client", "external"] and sample_tone == "formal":
            score += 1
            score_details.append("formal tone for client (+1)")
        elif request_audience == "personal" and sample_tone in ["casual", "neutral"]:
            score += 1
            score_details.append("appropriate personal tone (+1)")
        
        # Score based on tag overlap (1 point for any overlap)
        request_topic = request_analysis.get("topic", "").lower()
        sample_tags = [tag.lower() for tag in sample_analysis.get("tags", [])]
        
        # Check if any sample tags appear in the request topic
        topic_words = request_topic.split()
        if any(tag in topic_words or any(word in tag for word in topic_words) for tag in sample_tags):
            score += 1
            score_details.append("topic overlap (+1)")
        
        # Only include samples that meet the minimum score threshold
        if score >= min_score:
            scored_samples.append({
                "sample": sample,
                "score": score,
                "score_details": score_details
            })
        elif override and score > 0:  # Override mode: include any sample with score > 0
            scored_samples.append({
                "sample": sample,
                "score": score,
                "score_details": score_details
            })
    
    # Sort by score (highest first)
    scored_samples.sort(key=lambda x: x["score"], reverse=True)
    
    return scored_samples

def generate_text_with_style(request_analysis: Dict[str, Any], relevant_samples: list[Dict[str, Any]], api_key: str) -> Optional[str]:
    """
    Generate text that matches the user's writing style based on relevant samples.
    
    Args:
        request_analysis: Analysis of the user's request (from analyze_request_with_ai)
        relevant_samples: List of relevant samples with scores (from find_relevant_samples)
        api_key: OpenAI API key
        
    Returns:
        Generated text or None if generation failed
    """
    if not relevant_samples:
        return None
    
    try:
        client = openai.OpenAI(api_key=api_key)
        
        # Build style examples from the top 2-3 samples
        top_samples = relevant_samples[:3]  # Use top 3 samples max
        
        style_examples = []
        for scored_sample in top_samples:
            sample = scored_sample["sample"]
            style_examples.append(f'Example: "{sample["text"]}"')
        
        style_examples_text = "\n".join(style_examples)
        
        # Build the prompt
        prompt = f"""Write a {request_analysis.get('type', 'message')} for {request_analysis.get('audience', 'the audience')} with the purpose of {request_analysis.get('purpose', 'communication')}.

Topic: {request_analysis.get('topic', 'the requested topic')}

Match the writing style of these examples:

{style_examples_text}

Requirements:
- Match the tone, style, and communication patterns from the examples
- Keep it natural and authentic to the user's voice
- Be appropriate for the audience and purpose
- Don't copy the examples directly, but write new content in the same style

Write the {request_analysis.get('type', 'message')} now:"""
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Using mini for cost efficiency
            messages=[
                {"role": "system", "content": "You are a writing assistant that matches user's personal writing style. Write naturally and authentically."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,  # Higher temperature for more natural variation
            max_tokens=300
        )
        
        generated_text = response.choices[0].message.content.strip()
        return generated_text
        
    except Exception as e:
        print(f"Text generation failed: {e}")
        return None

def generate_pose(user_request: str, api_key: str, model: str = "gpt-4o-mini", override: bool = False, personality: Optional[str] = None) -> str:
    """
    Complete pipeline: analyze request, find relevant samples, and generate text.
    
    Args:
        user_request: The user's writing request
        api_key: OpenAI API key
        model: AI model to use (default: gpt-4o-mini)
        override: If True, use closest samples even if they don't meet minimum score
        personality: The personality to use for generation (required)
        
    Returns:
        Generated text or error message
    """
    try:
        # Validate personality is provided
        if not personality:
            return "❌ Personality is required. Use --personality <name> to specify which personality to use."
        
        # Step 1: Analyze the request
        print("📊 Analyzing your request...")
        request_analysis = analyze_request_with_ai(user_request, api_key)
        if not request_analysis:
            return "❌ Failed to analyze your request. Please try again."
        
        print(f"   Type: {request_analysis.get('type', 'N/A')}")
        print(f"   Audience: {request_analysis.get('audience', 'N/A')}")
        print(f"   Purpose: {request_analysis.get('purpose', 'N/A')}")
        print(f"   Personality: {personality}")
        
        # Step 2: Find relevant samples
        print("🎯 Finding relevant writing samples...")
        relevant_samples = find_relevant_samples(request_analysis, min_score=4, override=override, personality=personality)
        
        if not relevant_samples:
            if override:
                return "❌ No samples found at all. Add some samples first."
            else:
                return "❌ No relevant writing samples found. Add more samples with 'poser add-sample <label> <text>' to improve matching."
        
        print(f"   Found {len(relevant_samples)} relevant sample(s)")
        
        # Step 3: Generate text
        print("✨ Generating text in your style...")
        generated_text = generate_text_with_style(request_analysis, relevant_samples, api_key)
        
        if not generated_text:
            return "❌ Text generation failed. Please try again."
        
        print("✅ Generated successfully!")
        return generated_text
        
    except Exception as e:
        return f"❌ Error: {e}"

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
