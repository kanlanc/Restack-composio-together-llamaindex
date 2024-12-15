import os
from restack_ai.function import function, log
from llama_index.llms.together import TogetherLLM

@function.defn()
async def email_generate(prompt) -> str:
    try:
        log.info("email_generate function started",api_key=os.environ["TOGETHER_API_KEY"])

        
        log.info("email_generate function started", prompt=prompt)
        llm = TogetherLLM(
            model="meta-llama/Llama-3.3-70B-Instruct-Turbo", api_key=os.environ["TOGETHER_API_KEY"]
        )


        resp = llm.complete(prompt)

        log.info("email_generate function completed", response=resp.text)

        return resp.text
    except Exception as e:
        log.error("email_generate function failed", error=e)
        raise e
    