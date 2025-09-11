# Poser Usage Guide

This guide covers all the features and detailed usage instructions for Poser.

## 📚 Table of Contents

- [Quick Start](#-quick-start)
- [Command Reference](#-command-reference)
- [Writing Samples](#-writing-samples)
- [Request Formats](#-request-formats)
- [Sample Matching System](#-sample-matching-system)
- [Profile Management](#-profile-management)
- [Configuration](#-configuration)
- [Tips for Best Results](#-tips-for-best-results)
- [Troubleshooting](#-troubleshooting)
- [Examples](#-examples)

## 🚀 Quick Start

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

## 📋 Command Reference

### Basic Commands

```bash
# Check profile status
poser
# Output: "Profile loaded with 4 writing samples"

# Generate text in your style
poser "write a slack message about my new app deployment"
poser "slack: tell the team about the bug fix I just pushed"
poser "update my colleague about the sentry configuration changes"

# List all your writing samples
poser list-samples

# Add a new writing sample
poser add-sample "email to client" "Dear Client, I wanted to update you on our project progress..."

# Remove a sample by ID
poser remove-sample sample_20250911_185212

# Backup your profile
poser --backup

# Start fresh (backup and reset)
poser --backup-and-delete
```

### Command Line Options

```bash
poser [OPTIONS] [PROMPT]

Options:
  --version              Show version number
  --api-key API_KEY      OpenAI API key (or set OPENAI_API_KEY env var)
  --model MODEL          AI model to use (default: gpt-4o)
  --backup               Create a backup of your profile
  --backup-and-delete    Create backup and reset profile
  -h, --help             Show help message

Commands:
  add-sample <label> <text>     Add a writing sample
  list-samples                  List all samples with analysis
  remove-sample <id>            Remove a sample by ID
```

## 📝 Writing Samples

### Adding Samples

The more diverse samples you add, the better Poser becomes at matching your style:

```bash
# Slack messages
poser add-sample "slack review" "i just tagged you and matthew there for review edit: ah, you already saw, thanks :gpeace:"

# Technical discussions  
poser add-sample "technical discussion" "@Marvin Emechebe yep yep, i did see it..."

# Email communications
poser add-sample "email to boss" "Hi Sarah, I wanted to update you on the project status..."

# Formal documents
poser add-sample "client proposal" "Dear Client, We are pleased to present our proposal..."
```

### Sample Analysis

Each sample is automatically analyzed by AI to understand:
- **Type**: email/slack/text/formal document
- **Tone**: casual/formal/frustrated/polite/urgent/neutral
- **Audience**: team/client/personal/external/colleague
- **Purpose**: update/request/complaint/inquiry/response/informational
- **Tags**: 2-5 relevant keywords

### Viewing Samples

```bash
poser list-samples
```

Output:
```
Found 4 samples:

ID: sample_20250911_185212
Label: slack review
Text: i just tagged you and matthew there for review edit: ah, you...
Analysis: slack | casual | colleague | response
--------------------------------------------------
ID: sample_20250911_185217
Label: technical discussion
Text: @Marvin Emechebe yep yep, i did see it...
Analysis: slack | casual | colleague | update
--------------------------------------------------
```

## 🎨 Request Formats

Poser understands various request formats:

### Explicit Formats
```bash
poser "write a slack message about my new app"
poser "draft an email to my team about project delays"
poser "write a formal document for the client meeting"
```

### Implicit Formats with Colons
```bash
poser "slack: tell the team about my new app"
poser "slack message: new app announcement"
poser "email: update my boss on progress"
```

### Context-Inferred Formats
```bash
poser "tell my team about the new app"
poser "update the team on progress"
poser "email my boss about project delays"
```

## 🔍 Sample Matching System

### How It Works

When you run: `poser "write a slack message about my new app deployment"`

**1. Request Analysis** 📊
```
Analyzes your request to understand:
- Type: slack/email/formal document
- Audience: team/colleague/client/external
- Purpose: update/response/announcement/informational
- Topic: what you want to write about
```

**2. Smart Sample Matching** 🎯
```
Finds your writing samples that best match the request:
- Type match (2 points)
- Audience match (2 points)  
- Purpose match (1 point)
- Tone appropriateness (1 point)
- Topic overlap (1 point)

Only uses samples with 4+ points (acceptable match)
```

**3. Style-Based Generation** ✨
```
Creates dynamic prompts using your top samples:
"Write a slack message for team with purpose of update.
Topic: new app deployment

Match the writing style of these examples:
Example: 'seems like providing the sentry auth token...'
Example: 'I recall setting up source maps for...'

Requirements:
- Match the tone, style, and communication patterns
- Keep it natural and authentic to your voice
- Be appropriate for the audience and purpose"
```

**4. AI Generation** 🤖
```
Generates text that sounds authentically like YOU
```

### Scoring Criteria

Poser uses a sophisticated scoring system to find relevant samples:

- **Type Match**: 2 points (slack request → slack samples)
- **Audience Match**: 2 points (team request → team samples)
- **Purpose Match**: 1 point (update request → update samples)
- **Tone Appropriateness**: 1 point (casual for team, formal for client)
- **Topic Overlap**: 1 point (keywords like "sentry", "deployment", "CI")

**Minimum Score**: 4 points (acceptable match)

### Example Matching

Request: `"write a slack message about my new app deployment"`

Analysis: `slack | team | update | new app deployment`

Matching Samples:
1. "deployment update" (Score: 7) - Perfect match
2. "technical memory" (Score: 6) - Good match  
3. "technical discussion" (Score: 4) - Acceptable match

## 📊 Profile Management

### Profile Structure

Your profile is stored at `~/.poser/profile.json`:

```json
{
  "version": "0.1.0",
  "created": "2025-09-11",
  "samples": [
    {
      "id": "sample_20250911_185212",
      "user_label": "slack review",
      "text": "i just tagged you and matthew there for review...",
      "added_date": "2025-09-11",
      "word_count": 16,
      "ai_analysis": {
        "type": "slack",
        "tone": "casual",
        "audience": "colleague",
        "purpose": "response",
        "tags": ["tagging", "review", "communication", "thanks", "casual"]
      }
    }
  ],
  "style_summary": {},
  "preferences": {}
}
```

### Backup and Recovery

```bash
# Create backup
poser --backup
# Creates: ~/.poser/profile.json.backup

# Start fresh (backup and reset)
poser --backup-and-delete
# Backs up current profile and creates new one
```

## 🔧 Configuration

### Environment Variables

```bash
# Required
export OPENAI_API_KEY="sk-proj-..."

# Optional
export MODEL="gpt-4o-mini"  # Default: gpt-4o
```

### API Key Setup

1. Get your OpenAI API key from [platform.openai.com](https://platform.openai.com/account/api-keys)
2. Set it as an environment variable:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```
3. Or create a `.env` file:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd poser

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install in development mode
pip install -e .

# Set up environment variables
echo "OPENAI_API_KEY=your-api-key-here" > .env
```

### Dependencies

- `openai>=1.0.0` - OpenAI API client
- `python-dotenv>=1.0.0` - Environment variable loading
- `requests>=2.25.0` - HTTP requests
- `Pillow>=8.0.0` - Image processing
- `numpy>=1.20.0` - Numerical computing

## 📈 Tips for Best Results

### 1. Add Diverse Samples
- Include different communication types (slack, email, formal)
- Cover various audiences (team, colleague, client, external)
- Add samples for different purposes (update, response, announcement)

### 2. Use Descriptive Labels
```bash
# Good labels
poser add-sample "slack team update" "Hey team, quick update..."
poser add-sample "email to client" "Dear Client, I wanted to..."

# Less helpful labels  
poser add-sample "message" "Hey team, quick update..."
poser add-sample "text" "Dear Client, I wanted to..."
```

### 3. Regular Maintenance
- Review and remove outdated samples
- Add new samples as your style evolves
- Backup your profile regularly

### 4. Understand Limitations
- Works best with 4+ diverse samples
- Requires samples similar to your request type
- May not work well for completely new communication types

## 🐛 Troubleshooting

### Common Issues

**"No relevant writing samples found"**
- Add more samples with `poser add-sample`
- Try different request formats
- Check if you have samples for the communication type

**"Failed to analyze your request"**
- Check your OpenAI API key
- Ensure you have internet connection
- Try a simpler request format

**"Text generation failed"**
- Verify API key is valid
- Check OpenAI account has credits
- Try again with a different request

### Getting Help

- Check your profile: `poser list-samples`
- Verify API key: `echo $OPENAI_API_KEY`
- Test with simple request: `poser "write a slack message"`

## 🎯 Examples

### Real Generated Text

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

**Request**: `"slack: tell my colleague about the sentry bug fix"`

**Generated**:
```
@Team just wanted to give a quick update on the Sentry bug fix! 

I wrapped up the changes to ensure that we're using the correct 
environment variables for Sentry. I went ahead and updated the DSN 
and release info to follow the NEXT_PUBLIC_ pattern too—should keep 
everything consistent across both server and client.

Also, I made sure the source maps are being uploaded properly from CI 
during deploy, so we should be getting clearer stack traces for any 
new errors in staging and production.

Let me know if you run into any issues or if there's anything else 
we should tackle next!
```

**Request**: `"update the team about our new CI pipeline setup"`

**Generated**:
```
Hey team! 

Just wanted to loop everyone in on the new CI pipeline setup we've been 
working on. I've been digging into the configuration, and it looks like 
we're on track to streamline the entire process.

So, I've set up the initial stages to handle our builds, and we're 
incorporating the necessary steps for artifact uploads. I've also added 
a step to ensure that we're generating our source maps correctly — 
similar to what we did with the last project.

One thing I noticed is that we'll need to pass the environment variables 
properly to make sure everything's tagged right in Sentry. I'm planning 
to use the same pattern we established with the `NEXT_PUBLIC_...` naming 
convention. This should help keep things consistent whether we're running 
in staging or production.

I've pushed my recent changes to the branch, so if you want to take a look, 
it's all there: `abc12345xyz`. Would love any feedback or thoughts on this— 
especially around the source map generation.

Let's keep the convo going as we finalize this. Cheers!
```

### Sample Coverage Analysis

**Current samples (4):**
- slack | colleague | response
- slack | colleague | update  
- slack | team | update
- slack | team | update

**Coverage Test:**
- ✅ slack for team (update): 3 samples
- ✅ slack for colleague (response): 2 samples
- ✅ slack for colleague (update): 2 samples
- ❌ email for client (update): 0 samples
- ❌ email for external (informational): 0 samples
- ❌ formal document for client (informational): 0 samples

This shows that Poser works excellently for Slack communications but would need email samples to handle email requests effectively.

---

**Poser: Your AI writing assistant that actually sounds like you.**
