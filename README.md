# Poser

Poser (short for "composer") is an AI-powered writing assistant that learns any writing style and helps you communicate more effectively.

## The Vision

Move beyond simple AI API calls to build something that actually learns and adapts. Poser can capture any writing style - your own, a colleague's, a brand's voice, or even a specific author's tone - and use it to generate text that sounds authentically like that style.

## How It Works

### The Complete Flow

When you run: `poser "write an email to my team about project delays"`

**1. Request Analysis**
```
Type: "email"
Context: "team communication about project updates"
```

**2. Smart Sample Search**
```
Looks through your stored writing samples
Finds emails you've written before
Especially looks for project-related emails
```

**3. Dynamic Prompt Building**
```
You write like this user. Here are examples of their email style:

Example 1: "Hey team, quick update on the API project..."
Example 2: "Morning everyone, just a heads up that we're..."

Their style: [casual tone, uses "hey team", direct, brief]

Now write their email about: project delays
```

**4. AI Generation**
```
Sends to OpenAI API and gets back text that sounds like YOU
```

### Key Features

- **Style Learning**: Collects writing samples from any source
- **Intelligent Retrieval**: Only uses relevant examples (100-400 tokens max)
- **Context Awareness**: Detects communication type and pulls matching samples
- **Multiple Styles**: Can learn and switch between different writing patterns

## Examples

### Personal Style
**Style Profile**: Casual, direct, uses examples, asks rhetorical questions

**Relevant Sample**: "So I was thinking about this project - why are we making it so complicated? Here's what I'd do instead..."

**Request**: "Help me write an email about project delays"

**Result**: Text that sounds authentically like you.

### Brand Voice
**Style Profile**: Professional, concise, data-driven, uses bullet points

**Relevant Sample**: "Q3 Results: Revenue up 15% • User engagement increased 23% • Key metrics exceeded targets"

**Request**: "Write a product update announcement"

**Result**: Text that matches the established brand voice.

### Author Style
**Style Profile**: Descriptive, uses metaphors, formal tone, complex sentences

**Relevant Sample**: "The morning sun cast long shadows across the bustling marketplace, where vendors hawked their wares with the persistence of merchants who had weathered countless seasons..."

**Request**: "Write about a busy office environment"

**Result**: Text that captures the author's distinctive style.

## Technical Approach

- **Smart Prompting with Memory**: SQLite database stores user profiles and samples
- **Dynamic Context**: Only includes relevant examples, not everything
- **Feedback Loop**: Learns from your preferences and corrections
- **Cost-Efficient**: Uses 100-400 tokens for context instead of thousands

## Getting Started

```bash
# Install and run
poser

# First time setup
Hey, you're new! Let me set you up!
Welcome! Creating your profile...

# Backup your profile
poser --backup

# Start fresh (backup and reset)
poser --backup-and-delete
```

## The Goal

Eliminate the time spent crafting messages while maintaining authentic voice - whether it's your own style, a brand's voice, or any other writing pattern. Poser learns any writing style, so you can adapt your communication to any context or audience.
