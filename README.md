# Restack AI - Composio Gmail Integration Example

This repository contains a project that demonstrates how to combine Restack AI with Composio Gmail Integration to create a workflow that sends emails to a list of particular contact that can be easily exapnded.

## Walkthrough video

TBD

## Usage

1. Run Restack local engine with Docker:

   ```bash
   docker run -d --pull always --name restack -p 5233:5233 -p 6233:6233 -p 7233:7233 ghcr.io/restackio/restack:main
   ```

2. Open the web UI to see the workflows:

   ```bash
   http://localhost:5233
   ```

3. Clone this repository:

   ```bash
   git clone https://github.com/restackio/examples-python
   cd examples-python/examples/production_demo
   ```

4. Install dependencies using Poetry:

   ```bash
   poetry env use 3.12
   ```

   ```bash
   poetry shell
   ```

   ```bash
   poetry install
   ```

   ```bash
   poetry env info # Optional: copy the interpreter path to use in your IDE (e.g. Cursor, VSCode, etc.)
   ```

5. Run the services:

   ```bash
   poetry run dev
   ```

   This will start the Restack service with the defined workflows and functions.

6. In a new terminal, schedule the workflow:

   ```bash
   poetry shell
   ```

   Go to schedule_workflow file and add your composio entity id to the input before your run the next step!

   ```bash
   poetry run workflow
   ```

   This will schedule the ExampleWorkflow` and print the result.

7. Optionally, schedule the workflow to run on a interval:

   ```bash
   poetry run interval
   ```

8. Optionally, schedule a parent workflow to run 50 child workflows all at once:

   ```bash
   poetry run scale
   ```

## Project Structure

- `src/`: Main source code directory
  - `client.py`: Initializes the Restack client
  - `functions/`: Contains function definitions
  - `workflows/`: Contains workflow definitions
  - `services.py`: Sets up and runs the Restack services
- `schedule_workflow.py`: Example script to schedule and run a workflow
- `schedule_interval.py`: Example script to schedule and a workflow every second
- `schedule_scale.py`: Example script to schedule and run 100 workflows at once

# Deployment

Create an account on [Restack Cloud](https://console.restack.io)

Create an engine and get the engine id, address and api key.

In .envs add the following:
RESTACK_ENGINE_ID=<your-engine-id>
RESTACK_ENGINE_API_KEY=<your-engine-api-key>
RESTACK_ENGINE_ADDRESS=<your-engine-address>

In Restack Cloud workspace settings, generate a cloud token.

In .envs add the following:
RESTACK_CLOUD_TOKEN=<your-cloud-token>

Then execute restack up:

```bash
python restack_up.py
```

After you link your github to Restack Cloud, you will have a CI/CD pipeline to automatically deploy your changes.
