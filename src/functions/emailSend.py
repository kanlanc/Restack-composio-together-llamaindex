from llama_index.core.llms import ChatMessage
from llama_index.core.agent import FunctionCallingAgentWorker
from composio_llamaindex import App, ComposioToolSet,Action
import os
from restack_ai.function import function, log
from llama_index.llms.together import TogetherLLM
from llama_index.llms.openai import OpenAI


import openai


@function.defn()
async def email_send(input) -> str:
    try:
        log.info("email_send function started",entity_id=input["entity_id"])

        # llm = TogetherLLM(
        #     model="meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo", api_key=os.environ["TOGETHER_API_KEY"]
        # )

        llm = OpenAI(api_key=os.environ['OPEN_API_KEY'])

        entity_id = input["entity_id"]

        tool_set = ComposioToolSet(entity_id=entity_id)
        # tools = tool_set.get_tools(apps=[App.GMAIL])
        tools = tool_set.get_tools(actions=[Action.GMAIL_SEND_EMAIL])

        prefix_messages = [

            ChatMessage(
                    role="system",
                    content=(
                        "You are a Gmail Agent, and you can use tools to perform actions on Gmail."
                    ),
                )
            ]

        agent = FunctionCallingAgentWorker(
            tools=tools,
            llm=llm,
            prefix_messages=prefix_messages,
            max_function_calls=10,
            allow_parallel_tool_calls=False,
            verbose=True,
        ).as_agent()

        result = agent.chat(input["promptMessage"])

        # log.info("result",result=result)
        log.info("email_send function completed")

        return "Email sent successfully"
    except Exception as e:
        log.error("email_send function failed", error=e)
        raise e
    