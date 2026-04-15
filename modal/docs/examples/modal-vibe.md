# Modal Vibe: A scalable AI coding platform

> The Modal Vibe repo demonstrates how you can build a scalable AI coding platform on Modal.

Source: [https://modal.com/docs/examples/modal-vibe](https://modal.com/docs/examples/modal-vibe)

---

Modal Vibe: A scalable AI coding platform
 
 
 
The 
Modal Vibe repo
 demonstrates how you can build
a scalable AI coding platform on Modal.
 
Users of the application can prompt an LLM to create sandboxed applications that service React through a UI.
 
Each application lives on a 
Modal Sandbox
 and contains a webserver accessible through 
Modal Tunnels
.
 
For a high-level overview of Modal Vibe, including performance numbers and why they matter, see 
the accompanying blog post
.
For details on the implementation, read on.
 
How it’s structured
 
 
 
 
main.py
 is the entrypoint that runs the FastAPI controller that serves the web app and manages the sandbox apps.
 
core
 contains the logic for 
SandboxApp
 model and LLM logic.
 
sandbox
 contains a small HTTP server that gets put inside every Sandbox that’s created, as well as some sandbox lifecycle management code.
 
web
 contains the Modal Vibe website that users see and interact with, as well as the api server that manages Sandboxes.
 
How to run
 
 
First, set up the local environment:
 
 
Deploy
 
 
To deploy to Modal, copy 
.env.example
 to a file called 
.env
 and add your 
ANTHROPIC_API_KEY
.
Also, create a 
Modal Secret
 called 
anthropic-secret
 so our applications can access it.
 
Then, deploy the application with Modal:
 
 
Local Development
 
 
Run a load test:
 
 
Delete a sandbox:
 
 
Run an example sandbox HTTP server:
 
 
Modal Vibe: A scalable AI coding platform
How it’s structured
How to run
Deploy
Local Development
