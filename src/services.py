import asyncio
import os

from watchfiles import run_process
from src.client import client
from restack_ai.restack import ServiceOptions
from restack_ai.function import log

from src.functions.emailGenerate import email_generate
from src.workflows.EmailWorkflow import EmailSendWorkflow
from src.functions.emailValidation import email_validation
from src.functions.emailSend import email_send


async def main():

    await asyncio.gather(
        # Email service is starting as reported in the logs.
        client.start_service(
            # workflows=[EmailReceiveWorkflow, EmailSendWorkflow],
            workflows=[EmailSendWorkflow],
            functions=[email_generate,email_validation,email_send],

        ),     
    )

def run_services():
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Service interrupted by user. Exiting gracefully.")

def watch_services():
    watch_path = os.getcwd()
    print(f"Watching {watch_path} and its subdirectories for changes...")
    run_process(watch_path, recursive=True, target=run_services)

