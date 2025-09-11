#!/usr/bin/env python3
"""
Mock test script for request analysis function (shows expected results)
"""

def mock_analyze_request(request):
    """Mock function that shows what the AI would return"""
    
    # Simple mock logic based on keywords
    request_lower = request.lower()
    
    # Determine type
    if "slack" in request_lower or ("team" in request_lower and "email" not in request_lower):
        type_val = "slack"
    elif "email" in request_lower or "boss" in request_lower:
        type_val = "email"
    elif "formal" in request_lower or "document" in request_lower or "client" in request_lower:
        type_val = "formal document"
    else:
        type_val = "text"
    
    # Determine audience
    if "team" in request_lower:
        audience = "team"
    elif "boss" in request_lower or "client" in request_lower:
        audience = "client"
    else:
        audience = "team"  # default
    
    # Determine purpose
    if "announcement" in request_lower or "new app" in request_lower:
        purpose = "announcement"
    elif "update" in request_lower or "progress" in request_lower:
        purpose = "update"
    elif "delay" in request_lower or "bug" in request_lower:
        purpose = "update"
    else:
        purpose = "informational"
    
    # Extract topic
    topic = "communication request"
    if "new app" in request_lower:
        topic = "new app"
    elif "project delay" in request_lower:
        topic = "project delays"
    elif "bug fix" in request_lower:
        topic = "bug fix"
    elif "deployment" in request_lower:
        topic = "deployment status"
    
    return {
        "type": type_val,
        "audience": audience,
        "purpose": purpose,
        "topic": topic
    }

def test_request_analysis():
    """Test the request analysis function with various inputs"""
    
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
    
    print("🧪 Mock Test: Request Analysis Function")
    print("=" * 60)
    
    for i, request in enumerate(test_cases, 1):
        print(f"\n{i}. Request: \"{request}\"")
        print("-" * 40)
        
        analysis = mock_analyze_request(request)
        print("✅ Expected Analysis:")
        print(f"   Type: {analysis['type']}")
        print(f"   Audience: {analysis['audience']}")
        print(f"   Purpose: {analysis['purpose']}")
        print(f"   Topic: {analysis['topic']}")
    
    print("\n" + "=" * 60)
    print("🏁 Mock test completed!")
    print("\n💡 To test with real AI:")
    print("   1. Set OPENAI_API_KEY environment variable")
    print("   2. Run: python test_request_analysis.py")

if __name__ == "__main__":
    test_request_analysis()
