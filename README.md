# Poser

Poser (short for "composer") is an AI-powered writing assistant that learns your personal writing style and helps you communicate more effectively.

## What It Does

Poser analyzes your writing samples, understands your communication patterns, and generates text that sounds authentically like you. Instead of generic AI responses, you get text that matches your personal style.

## Quick Start

```bash
# Install Poser
pip install -e .

# Set up your OpenAI API key
export OPENAI_API_KEY="your-api-key-here"

# Check your profile status
poser

# Generate text in your style
poser "write a slack message about my new app deployment"
```

## How It Works

1. **Add Writing Samples**: You provide examples of your writing
2. **AI Analysis**: Poser analyzes each sample to understand your style
3. **Smart Matching**: When you request text, it finds relevant samples
4. **Style Generation**: It generates new text that matches your voice

## Basic Usage

```bash
# Generate text
poser "write a slack message about my new app"
poser "email my boss about project delays"

# Manage samples
poser add-sample "slack update" "Hey team, quick update on the project..."
poser list-samples
poser remove-sample sample_20250911_185212

# Profile management
poser --backup
poser --backup-and-delete
```

## Example Output

**Request**: `"write a slack message about my new app deployment"`

**Generated**:
```
hey team,

just a heads up that we've deployed the new version of the app! 🎉 
the commit hash is `b8f3e2c1d7a9c4e8a1c9e0f1b2c3d4e5f6a7890b`, 
and it includes a bunch of tweaks we talked about in the last sprint.

i've tested the main features in staging, and everything seems to be 
functioning as expected. however, i did notice a slight delay in some 
API responses—might be worth keeping an eye on.

let me know if you encounter any issues or if something feels off. 
happy testing!
```

## Requirements

- Python 3.8+
- OpenAI API key
- Writing samples to train the system

## Installation

```bash
# Clone and install
git clone <repository-url>
cd poser
python3 -m venv venv
source venv/bin/activate
pip install -e .

# Set up API key
echo "OPENAI_API_KEY=your-api-key-here" > .env
```

## Documentation

For detailed usage instructions, see [USAGE.md](USAGE.md).

## The Goal

Eliminate the time spent crafting messages while maintaining your authentic voice. Poser learns your writing style so you can communicate more effectively across any context or audience.

**Poser: Your AI writing assistant that actually sounds like you.**
