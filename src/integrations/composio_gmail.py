"""
Composio Gmail Integration for Harmony.

This module provides functionality to integrate Composio's Gmail tools with Harmony.
"""

import os
from typing import Dict, List, Optional, Any
import logging

from llama_index.core.llms import ChatMessage
from llama_index.core.agent import FunctionCallingAgentWorker
from composio_llamaindex import App, ComposioToolSet, Action
from llama_index.llms.openai import OpenAI

# Configure logging
logger = logging.getLogger(__name__)

class ComposioGmailIntegration:
    """
    A class to handle Composio Gmail integration with Harmony.
    
    This class provides methods to interact with Gmail using Composio's tools.
    """
    
    def __init__(self, entity_id: str, api_key: Optional[str] = None, openai_api_key: Optional[str] = None):
        """
        Initialize the Composio Gmail integration.
        
        Args:
            entity_id: The entity ID for the user in Composio
            api_key: Optional Composio API key (defaults to environment variable)
            openai_api_key: Optional OpenAI API key (defaults to environment variable)
        """
        self.entity_id = entity_id
        self.api_key = api_key or os.environ.get("COMPOSIO_API_KEY")
        self.openai_api_key = openai_api_key or os.environ.get("OPEN_API_KEY")
        
        if not self.api_key:
            raise ValueError("Composio API key is required. Set it in the environment or pass it to the constructor.")
        
        if not self.openai_api_key:
            raise ValueError("OpenAI API key is required. Set it in the environment or pass it to the constructor.")
        
        # Initialize the LLM
        self.llm = OpenAI(api_key=self.openai_api_key)
        
        # Initialize the Composio tool set
        self.tool_set = ComposioToolSet(entity_id=self.entity_id)
        
        # Get all Gmail tools
        self.gmail_tools = self.tool_set.get_tools(apps=[App.GMAIL])
        
        logger.info(f"Initialized Composio Gmail integration for entity {entity_id}")
    
    def send_email(self, to: str, subject: str, body: str) -> Dict[str, Any]:
        """
        Send an email using Gmail.
        
        Args:
            to: Recipient email address
            subject: Email subject
            body: Email body content
            
        Returns:
            Dict containing the result of the operation
        """
        # Get the send email tool specifically
        send_email_tool = self.tool_set.get_tools(actions=[Action.GMAIL_SEND_EMAIL])
        
        # Set up the agent with Gmail tools
        prefix_messages = [
            ChatMessage(
                role="system",
                content="You are a Gmail Agent, and you can use tools to perform actions on Gmail."
            )
        ]
        
        agent = FunctionCallingAgentWorker(
            tools=send_email_tool,
            llm=self.llm,
            prefix_messages=prefix_messages,
            max_function_calls=10,
            allow_parallel_tool_calls=False,
            verbose=True,
        ).as_agent()
        
        # Construct the prompt for sending an email
        prompt = f"Send an email to {to} with subject '{subject}' and body '{body}'"
        
        try:
            # Send the email
            result = agent.chat(prompt)
            logger.info(f"Email sent successfully to {to}")
            return {"status": "success", "message": "Email sent successfully", "details": result.response}
        except Exception as e:
            logger.error(f"Failed to send email: {str(e)}")
            return {"status": "error", "message": f"Failed to send email: {str(e)}"}
    
    def search_emails(self, query: str, max_results: int = 10) -> Dict[str, Any]:
        """
        Search for emails in Gmail.
        
        Args:
            query: Search query string
            max_results: Maximum number of results to return
            
        Returns:
            Dict containing the search results
        """
        # Get the search email tool specifically
        search_email_tool = self.tool_set.get_tools(actions=[Action.GMAIL_SEARCH])
        
        # Set up the agent with Gmail tools
        prefix_messages = [
            ChatMessage(
                role="system",
                content="You are a Gmail Agent, and you can use tools to perform actions on Gmail."
            )
        ]
        
        agent = FunctionCallingAgentWorker(
            tools=search_email_tool,
            llm=self.llm,
            prefix_messages=prefix_messages,
            max_function_calls=10,
            allow_parallel_tool_calls=False,
            verbose=True,
        ).as_agent()
        
        # Construct the prompt for searching emails
        prompt = f"Search for emails with the query '{query}' and return up to {max_results} results"
        
        try:
            # Search for emails
            result = agent.chat(prompt)
            logger.info(f"Email search completed for query: {query}")
            return {"status": "success", "message": "Email search completed", "details": result.response}
        except Exception as e:
            logger.error(f"Failed to search emails: {str(e)}")
            return {"status": "error", "message": f"Failed to search emails: {str(e)}"}
    
    def get_unread_emails(self, max_results: int = 10) -> Dict[str, Any]:
        """
        Get unread emails from Gmail.
        
        Args:
            max_results: Maximum number of results to return
            
        Returns:
            Dict containing the unread emails
        """
        return self.search_emails("is:unread", max_results)
    
    def get_recent_emails(self, max_results: int = 10) -> Dict[str, Any]:
        """
        Get recent emails from Gmail.
        
        Args:
            max_results: Maximum number of results to return
            
        Returns:
            Dict containing the recent emails
        """
        return self.search_emails("newer_than:2d", max_results)


# Example usage
if __name__ == "__main__":
    # This is just for demonstration purposes
    entity_id = os.environ.get("COMPOSIO_ENTITY_ID", "demo_entity_id")
    
    # Initialize the integration
    gmail_integration = ComposioGmailIntegration(entity_id=entity_id)
    
    # Send a test email
    result = gmail_integration.send_email(
        to="test@example.com",
        subject="Test Email from Harmony",
        body="This is a test email sent from the Harmony platform using Composio Gmail integration."
    )
    
    print(result)
    
    # Get unread emails
    unread_emails = gmail_integration.get_unread_emails(max_results=5)
    print(unread_emails)

