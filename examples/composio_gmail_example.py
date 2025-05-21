"""
Example script demonstrating how to use the Composio Gmail integration with Harmony.
"""

import os
import sys
import logging
from dotenv import load_dotenv

# Add the src directory to the path so we can import our modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Import the Composio Gmail integration
from src.integrations.composio_gmail import ComposioGmailIntegration

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

def main():
    """
    Main function to demonstrate the Composio Gmail integration.
    """
    # Check if required environment variables are set
    required_vars = ["COMPOSIO_API_KEY", "OPEN_API_KEY", "COMPOSIO_ENTITY_ID"]
    missing_vars = [var for var in required_vars if not os.environ.get(var)]
    
    if missing_vars:
        logger.error(f"Missing required environment variables: {', '.join(missing_vars)}")
        logger.error("Please set these variables in your .env file or environment.")
        return
    
    # Get the entity ID from environment variables
    entity_id = os.environ.get("COMPOSIO_ENTITY_ID")
    
    try:
        # Initialize the Composio Gmail integration
        logger.info("Initializing Composio Gmail integration...")
        gmail_integration = ComposioGmailIntegration(entity_id=entity_id)
        
        # Example 1: Send an email
        logger.info("Sending a test email...")
        send_result = gmail_integration.send_email(
            to="test@example.com",
            subject="Test Email from Harmony",
            body="This is a test email sent from the Harmony platform using Composio Gmail integration."
        )
        logger.info(f"Send email result: {send_result}")
        
        # Example 2: Get unread emails
        logger.info("Getting unread emails...")
        unread_emails = gmail_integration.get_unread_emails(max_results=5)
        logger.info(f"Unread emails result: {unread_emails}")
        
        # Example 3: Search for specific emails
        logger.info("Searching for emails...")
        search_result = gmail_integration.search_emails("important", max_results=3)
        logger.info(f"Search result: {search_result}")
        
        logger.info("Composio Gmail integration examples completed successfully!")
        
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        import traceback
        logger.error(traceback.format_exc())

if __name__ == "__main__":
    main()

