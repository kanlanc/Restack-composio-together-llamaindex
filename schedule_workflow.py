import asyncio
import time
from restack_ai import Restack

async def main():

    client = Restack()

    # workflow_id = f"{int(time.time() * 1000)}-ExampleWorkflow"
    # run_id = await client.schedule_workflow(
    #     workflow_name="ChildWorkflow",
    #     workflow_id=workflow_id
    # )

    # await client.get_workflow_result(
    #     workflow_id=workflow_id,
    #     run_id=run_id
    # )

    workflow_id = f"{int(time.time() * 1000)}-EmailSendWorkflow"
    run_id =await client.schedule_workflow(
        workflow_name="EmailSendWorkflow",
        input={
            entity_id=""
        },
        workflow_id=workflow_id
    )


    await client.get_workflow_result(
        workflow_id=workflow_id,
        run_id=run_id
    )
    print(run_id)

    print(workflow_id)

    exit(0)

def run_schedule_workflow():
    asyncio.run(main())

if __name__ == "__main__":
    run_schedule_workflow()
