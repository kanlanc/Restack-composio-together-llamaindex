# Composio Gmail Integration for Harmony

This repository contains the implementation and documentation for integrating Composio's Gmail functionality with the Harmony platform.

## Overview

Composio provides a powerful set of tools for integrating with various services, including Gmail. This integration allows Harmony to send, receive, and process emails through Gmail, enabling automated email workflows and intelligent email processing.

## Features

- Send emails through Gmail
- Search for emails with specific criteria
- Get unread emails
- Process email content with LLMs
- Automate email workflows

## Getting Started

### Prerequisites

- Python 3.9+
- Composio account with API access
- Gmail API credentials
- OpenAI API key (for LLM functionality)

### Installation

1. Install the required packages:

```bash
pip install composio-llamaindex llama-index openai python-dotenv
```

2. Set up environment variables:

Create a `.env` file with the following variables:

```
COMPOSIO_API_KEY=your_composio_api_key
OPEN_API_KEY=your_openai_api_key
COMPOSIO_ENTITY_ID=your_entity_id
```

### Usage

See the `examples/composio_gmail_example.py` file for a complete example of how to use the integration.

Basic usage:

```python
from src.integrations.composio_gmail import ComposioGmailIntegration

# Initialize the integration
gmail_integration = ComposioGmailIntegration(entity_id="your_entity_id")

# Send an email
result = gmail_integration.send_email(
    to="recipient@example.com",
    subject="Hello from Harmony",
    body="This is a test email sent from Harmony using Composio."
)

# Get unread emails
unread_emails = gmail_integration.get_unread_emails(max_results=5)
```

## Testing

Run the integration tests to verify that the Composio Gmail integration is working correctly:

```bash
pytest tests/composio_integration_test.py
```

## Documentation

For detailed documentation on the Composio Gmail integration, see the [docs/composio_gmail_integration.md](docs/composio_gmail_integration.md) file.

## Limitations and Considerations

- Gmail API has rate limits that should be considered for high-volume applications
- OAuth tokens expire and need to be refreshed periodically
- Users must grant specific permissions for different Gmail operations
- There are limitations on email content and attachments

## References

- [Composio Documentation](https://docs.composio.dev)
- [Gmail API Documentation](https://developers.google.com/gmail/api)
- [LlamaIndex Documentation](https://docs.llamaindex.ai)

