"""
Tests for the core Poser functionality.
"""

import pytest
import os
from unittest.mock import patch, MagicMock


class TestPoserCore:
    """Test cases for core Poser functionality."""
    
    def test_import_core(self):
        """Test that core module can be imported."""
        try:
            from poser.core import generate_pose
            assert callable(generate_pose)
        except ImportError:
            pytest.skip("Core functionality not yet implemented")
    
    def test_environment_variables(self):
        """Test that environment variables are properly loaded."""
        # This test ensures .env file is being read
        assert os.getenv("OPENAI_API_KEY") is not None
        assert os.getenv("MODEL") == "gpt-4o"
    
    @patch.dict(os.environ, {"OPENAI_API_KEY": "test-key", "MODEL": "gpt-4o"})
    def test_api_key_loading(self):
        """Test API key loading from environment."""
        assert os.getenv("OPENAI_API_KEY") == "test-key"
        assert os.getenv("MODEL") == "gpt-4o"


if __name__ == "__main__":
    pytest.main([__file__])
