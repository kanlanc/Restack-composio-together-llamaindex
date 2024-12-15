from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from dataclasses import dataclass
import time
from src.client import client
import uvicorn
import os
from composio import ComposioToolSet, App



# Define request model
@dataclass
class PromptRequest:
    prompt: str

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return "Welcome to the TogetherAI LlamaIndex FastAPI App!"



@app.post("/api/webhook")
async def webhook(request: Request):
    # Keep pinging this endpoint perioidically to monitor for new emails or better is to scheduled a workflow to run every 10 minutes
    try:
        print("Webhook called")
        request = await request.json()

        user_id = request.get("user_id")
        reciever_id = request.get("reciever_id")
        email_content = request.get("email_content")

        user_id = "saivicky2015@gmail.com"
        reciever_id = "vk326@cornell.edu"
        email_content = "Hello, I am a user and I am having a problem with my account. Please help me."
        

        workflow_id = f"{int(time.time() * 1000)}-EmailSendWorkflow"

        run_id =await client.schedule_workflow(
            workflow_name="EmailSendWorkflow",
            workflow_id=workflow_id,
            input={
                "user_id": user_id,
                "reciever_id": reciever_id,
                "email_content": email_content,
            }
        )


        result = await client.get_workflow_result(
            workflow_id=workflow_id,
            run_id=run_id
        )
        print(run_id)

        print(workflow_id)
        
        return {"result": result}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/api/schedule")
async def schedule_workflow(request: PromptRequest):
    try:
        

        workflow_id = f"{int(time.time() * 1000)}-EmailSendWorkflow"

        run_id =await client.schedule_workflow(
            workflow_name="EmailSendWorkflow",
            workflow_id=workflow_id,
        )


        result = await client.get_workflow_result(
            workflow_id=workflow_id,
            run_id=run_id
        )
        print(run_id)

        print(workflow_id)
        
        return {"result": result}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/api/gmail_auth")
async def gmail_auth(request: Request):

    request = await request.json()
    user_id = request.get("user_id")  # user_id is the email of the user

    app_name = "gmail"
    auth_scheme = "OAUTH2"


    #FIXME: Change this to start the gmail auth workflow, and also find how to add input(user_id) to the workflow


    toolset = ComposioToolSet()

    connection_request = toolset.initiate_connection(
        app=app_name,
        redirect_url = os.getenv("REDIRECT_URL_ON_SUCCESSFUL_OAUTH"), # user comes here after oauth flow
        entity_id=user_id,
        auth_scheme=auth_scheme,
    )

    print(connection_request.connectedAccountId,connection_request.connectionStatus)

    return { "status_code": 303, "message": "Gmail authentication initiated", "status": "initiated","redirect_url":connection_request.redirectUrl}


# @app.get("/api/gmail_auth_callback")
# async def gmail_auth_callback():
#     # Redirect user to the dashboard
#     response = {"message": "Gmail authentication successful", "status": "success","redirect_url":"http://localhost:3000/dashboard"}
#     return response

def run_app():
    uvicorn.run("src.app:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == '__main__':
    run_app()
