import asyncio
from datetime import timedelta

from restack_ai.workflow import workflow, log, workflow_info, import_functions

with import_functions():
    from src.functions.emailGenerate import email_generate
    from src.functions.emailValidation import email_validation
    from src.functions.emailSend import email_send



@workflow.defn()
class EmailSendWorkflow:
    @workflow.run
    async def run(self,input):


        log.info("The workflow is getting events !!")
        user_id = workflow_info().input.get("user_id")
        reciever_id = workflow_info().input.get("reciever_id")
        email_content = workflow_info().input.get("email_content")

     

        generated_text = await workflow.step(
            email_generate,
            f"Generate an email response to the user based on the email content. {email_content}",
            start_to_close_timeout=timedelta(seconds=120)
        )


    

        validated_response = await workflow.step(
            email_validation,
            f"""Validate the following email response:

        Original Question: {email_content}
        Generated Response: {generated_text}

        Instructions:
        1. Check if the response is appropriate and professional
        2. Ensure there is no offensive language
        3. Verify it sounds natural and human-like
        4. If the response is acceptable, return it as-is
        5. If the response needs changes, generate and return a new response

        Please return only the final response text without any additional commentary.""",
            start_to_close_timeout=timedelta(seconds=120)
        )

        input = {
            "promptMessage": f"Send the email response to the user {reciever_id} from {user_id} based on the email content. {validated_response}",
            "entity_id": user_id,
        }

        email_send_response = await workflow.step(
            email_send,
            input,
            start_to_close_timeout=timedelta(seconds=120)
        )

        return {
            "email_response": validated_response,
            "email_send_status": "success",
        }


@workflow.defn()
class EmailCheckWorkflow:
    @workflow.run
    async def run(self):
        # email_content = workflow_info().input
        log.info("The recieveworkflow is getting events !!")


        

        return {
            # "email_response": generated_text,
        }
