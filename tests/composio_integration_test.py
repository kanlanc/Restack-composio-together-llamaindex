import os
import pytest
from unittest.mock import patch, MagicMock
from composio_llamaindex import App, ComposioToolSet, Action
from llama_index.core.agent import FunctionCallingAgentWorker
from llama_index.core.llms import ChatMessage

# Mock environment variables for testing
os.environ["COMPOSIO_API_KEY"] = "test_api_key"
os.environ["OPEN_API_KEY"] = "test_openai_key"

class TestComposioGmailIntegration:
    """Test suite for verifying Composio Gmail integration."""
    
    @pytest.fixture
    def mock_llm(self):
        """Mock LLM for testing."""
        mock = MagicMock()
        mock.chat.return_value = MagicMock(response="Email sent successfully")
        return mock
    
    @pytest.fixture
    def mock_tool_set(self):
        """Mock Composio tool set for testing."""
        mock = MagicMock()
        mock.get_tools.return_value = [
            {
                "name": "gmail_send_email",
                "description": "Send an email using Gmail",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "to": {"type": "string"},
                        "subject": {"type": "string"},
                        "body": {"type": "string"}
                    },
                    "required": ["to", "subject", "body"]
                }
            }
        ]
        return mock
    
    @patch("composio_llamaindex.ComposioToolSet")
    def test_gmail_send_email_integration(self, mock_composio_toolset, mock_llm, mock_tool_set):
        """Test that Gmail send email integration works correctly."""
        # Arrange
        mock_composio_toolset.return_value = mock_tool_set
        entity_id = "test_entity_id"
        
        # Act
        tool_set = ComposioToolSet(entity_id=entity_id)
        tools = tool_set.get_tools(actions=[Action.GMAIL_SEND_EMAIL])
        
        prefix_messages = [
            ChatMessage(
                role="system",
                content="You are a Gmail Agent, and you can use tools to perform actions on Gmail."
            )
        ]
        
        agent = FunctionCallingAgentWorker(
            tools=tools,
            llm=mock_llm,
            prefix_messages=prefix_messages,
            max_function_calls=10,
            allow_parallel_tool_calls=False,
            verbose=True,
        ).as_agent()
        
        result = agent.chat("Send an email to test@example.com with subject 'Test Email' and body 'This is a test email'")
        
        # Assert
        mock_tool_set.get_tools.assert_called_once_with(actions=[Action.GMAIL_SEND_EMAIL])
        mock_llm.chat.assert_called_once()
        assert "Email sent successfully" in result.response
    
    @patch("composio_llamaindex.ComposioToolSet")
    def test_gmail_authentication_flow(self, mock_composio_toolset, mock_tool_set):
        """Test that Gmail authentication flow works correctly."""
        # Arrange
        mock_composio_toolset.return_value = mock_tool_set
        entity_id = "test_entity_id"
        
        # Act
        tool_set = ComposioToolSet(entity_id=entity_id)
        
        # Assert
        mock_composio_toolset.assert_called_once_with(entity_id=entity_id)
        
    @patch("composio_llamaindex.ComposioToolSet")
    def test_multiple_gmail_actions(self, mock_composio_toolset, mock_tool_set):
        """Test that multiple Gmail actions can be configured."""
        # Arrange
        mock_composio_toolset.return_value = mock_tool_set
        entity_id = "test_entity_id"
        
        # Act
        tool_set = ComposioToolSet(entity_id=entity_id)
        tools = tool_set.get_tools(apps=[App.GMAIL])
        
        # Assert
        mock_tool_set.get_tools.assert_called_once_with(apps=[App.GMAIL])

