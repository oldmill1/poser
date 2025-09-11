#!/usr/bin/env python3
"""
Test script for request analysis function
"""

import os
import json
from poser.core import analyze_request_with_ai

def test_request_analysis():
    """Test the request analysis function with various inputs"""
    
    # Get API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ No OPENAI_API_KEY found in environment")
        print("Set OPENAI_API_KEY to test the function")
        return
    
    # Test cases
    test_cases = [
        # Explicit formats
        "write a slack message about my new app",
        "draft an email to my team about project delays",
        "write a formal document for the client meeting",
        
        # Implicit formats with colons
        "slack: tell the team about my new app",
        "slack message: new app announcement", 
        "email: update my boss on progress",
        
        # Context-inferred formats
        "tell my team about the new app",
        "update the team on progress",
        "email my boss about project delays",
        "draft something for the client meeting",
        
        # Edge cases
        "help me write something about the bug fix",
        "I need to communicate the deployment status",
    ]
    
    print("🧪 Testing Request Analysis Function")
    print("=" * 60)
    
    for i, request in enumerate(test_cases, 1):
        print(f"\n{i}. Request: \"{request}\"")
        print("-" * 40)
        
        try:
            analysis = analyze_request_with_ai(request, api_key)
            if analysis:
                print("✅ Analysis successful:")
                print(f"   Type: {analysis.get('type', 'N/A')}")
                print(f"   Audience: {analysis.get('audience', 'N/A')}")
                print(f"   Purpose: {analysis.get('purpose', 'N/A')}")
                print(f"   Topic: {analysis.get('topic', 'N/A')}")
            else:
                print("❌ Analysis failed - returned None")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print("\n" + "=" * 60)
    print("🏁 Test completed!")

if __name__ == "__main__":
    test_request_analysis()
