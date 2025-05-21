# Composio Gmail Integration Guide

This document provides information on how to set up and use the Composio Gmail integration with Harmony.

## Overview

Composio provides a set of tools that allow integration with various services, including Gmail. This integration enables Harmony to:

- Send emails through Gmail
- Read and process emails from Gmail
- Manage Gmail labels and folders
- Search for specific emails

## Prerequisites

Before using the Composio Gmail integration, you need:

1. A Composio account with API access
2. Gmail API credentials
3. Proper authentication setup for Gmail

## Setup

### 1. Install Required Packages

```bash
pip install composio-llamaindex llama-index
```

### 2. Configure Environment Variables

Set the following environment variables:

```bash
COMPOSIO_API_KEY=your_composio_api_key
OPEN_API_KEY=your_openai_api_key  # Used for LLM functionality
```

### 3. Gmail Authentication

The user needs to authenticate with Gmail to allow Composio to access their account. This is typically done through OAuth:

1. Redirect the user to the Gmail authentication page
2. User grants permission
3. Receive and store the authentication token
4. Use the token for subsequent API calls

## Usage

### Initializing the Composio Tool Set

```python
from composio_llamaindex import App, ComposioToolSet, Action
from llama_index.core.agent import FunctionCallingAgentWorker
from llama_index.llms.openai import OpenAI

# Initialize the LLM
llm = OpenAI(api_key=os.environ['OPEN_API_KEY'])

# Initialize the Composio tool set with the user's entity ID
entity_id = "user_entity_id"
tool_set = ComposioToolSet(entity_id=entity_id)

# Get Gmail-specific tools
gmail_tools = tool_set.get_tools(apps=[App.GMAIL])

# Or get specific Gmail actions
send_email_tool = tool_set.get_tools(actions=[Action.GMAIL_SEND_EMAIL])
```

### Sending an Email

```python
from llama_index.core.llms import ChatMessage

# Set up the agent with Gmail tools
prefix_messages = [
    ChatMessage(
        role="system",
        content="You are a Gmail Agent, and you can use tools to perform actions on Gmail."
    )
]

agent = FunctionCallingAgentWorker(
    tools=send_email_tool,
    llm=llm,
    prefix_messages=prefix_messages,
    max_function_calls=10,
    allow_parallel_tool_calls=False,
    verbose=True,
).as_agent()

# Send an email using natural language
result = agent.chat("Send an email to john@example.com with subject 'Meeting Tomorrow' and body 'Hi John, just confirming our meeting tomorrow at 2pm. Best regards, Jane'")
```

## Limitations and Considerations

1. **Rate Limits**: Gmail API has rate limits that should be considered for high-volume applications.
2. **Authentication Expiry**: OAuth tokens expire and need to be refreshed periodically.
3. **Permissions**: Users must grant specific permissions for different Gmail operations.
4. **Content Restrictions**: There are limitations on email content and attachments.

## Troubleshooting

### Common Issues

1. **Authentication Failures**
   - Check that the OAuth flow is completed correctly
   - Verify that tokens are being stored and refreshed properly

2. **Rate Limit Exceeded**
   - Implement exponential backoff for retries
   - Batch operations when possible

3. **Permission Issues**
   - Ensure the correct scopes are requested during authentication
   - Check that the user has granted all necessary permissions

## Testing

Run the integration tests to verify that the Composio Gmail integration is working correctly:

```bash
pytest tests/composio_integration_test.py
```

## References

- [Composio Documentation](https://docs.composio.dev)
- [Gmail API Documentation](https://developers.google.com/gmail/api)
- [LlamaIndex Documentation](https://docs.llamaindex.ai)

