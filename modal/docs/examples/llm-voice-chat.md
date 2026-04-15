# QuiLLMan: Voice Chat with Moshi

> QuiLLMan is a complete voice chat application built on Modal: you speak and the chatbot speaks back!

Source: [https://modal.com/docs/examples/llm-voice-chat](https://modal.com/docs/examples/llm-voice-chat)

---

QuiLLMan: Voice Chat with Moshi
 
QuiLLMan
 is a complete voice chat application built on Modal: you speak and the chatbot speaks back!
 
At the core is Kyutai Lab’s 
Moshi
 model, a speech-to-speech language model that will continuously listen, plan, and respond to the user.
 
Thanks to bidirectional websocket streaming and 
Opus audio compression
, response times on good internet can be nearly instantaneous, closely matching the cadence of human speech.
 
You can find the demo live 
here
.
 
 
 
Everything — from the React frontend to the model backend — is deployed serverlessly on Modal, allowing it to automatically scale and ensuring you only pay for the compute you use.
 
This page provides a high-level walkthrough of the 
GitHub repo
.
 
Code overview
 
 
Traditionally, building a bidirectional streaming web application as compute-heavy as QuiLLMan would take a lot of work, and it’s especially difficult to make it robust and scale to handle many concurrent users.
 
But with Modal, it’s as simple as writing two different classes and running a CLI command.
 
Our project structure looks like this:
 
Moshi Websocket Server
: loads an instance of the Moshi model and maintains a bidirectional websocket connection with the client.
 
React Frontend
: runs client-side interaction logic.
 
Let’s go through each of these components in more detail.
 
FastAPI Server
 
 
Both frontend and backend are served via a 
FastAPI Server
, which is a popular Python web framework for building REST APIs.
 
On Modal, a function or class method can be exposed as a web endpoint by decorating it with 
@app.asgi_app()
 and returning a FastAPI app. You’re then free to configure the FastAPI server however you like, including adding middleware, serving static files, and running websockets.
 
Moshi Websocket Server
 
 
Traditionally, a speech-to-speech chat app requires three distinct modules: speech-to-text, text-to-text, and text-to-speech. Passing data between these modules introduces bottlenecks, and can limit the speed of the app and forces a turn-by-turn conversation which can feel unnatural.
 
Kyutai Lab’s 
Moshi
 bundles all modalities into one model, which decreases latency and makes for a much simpler app.
 
Under the hood, Moshi uses the 
Mimi
 streaming encoder/decoder model to maintain an unbroken stream of audio in and out. The encoded audio is processed by a 
speech-text foundation model
, which uses an internal monologue to determine when and how to respond.
 
Using a streaming model introduces a few challenges not normally seen in inference backends:
 
The model is 
stateful
, meaning it maintains context of the conversation so far. This means a model instance cannot be shared between user conversations, so we must run a unique GPU per user session, which is normally not an easy feat!
 
The model is 
streaming
, so the interface around it is not as simple as a POST request. We must find a way to stream audio data in and out, and do it fast enough for seamless playback.
 
We solve both of these in 
src/moshi.py
, using a few Modal features.
 
To solve statefulness, we just spin up a new GPU per concurrent user.
That’s easy with Modal!
 
 
With this setting, if a new user connects, a new GPU instance is created! When any user disconnects, the state of their model is reset and that GPU instance is returned to the warm pool for re-use (for up to 300 seconds). Be aware that a GPU per user is not going to be cheap, but it’s the simplest way to ensure user sessions are isolated.
 
For streaming, we use FastAPI’s support for bidirectional websockets. This allows clients to establish a single connection at the start of their session, and stream audio data both ways.
 
Just as a FastAPI server can run from a Modal function, it can also be attached to a Modal class method, allowing us to couple a prewarmed Moshi model to a websocket session.
 
 
To run a 
development server
 for the Moshi module, run this command from the root of the repo.
 
 
In the terminal output, you’ll find a URL for creating a websocket connection.
 
React Frontend
 
 
The frontend is a static React app, found in the 
src/frontend
 directory and served by 
src/app.py
.
 
We use the 
Web Audio API
 to record audio from the user’s microphone and playback audio responses from the model.
 
For efficient audio transmission, we use the 
Opus codec
 to compress audio across the network. Opus recording and playback are supported by the 
opus-recorder
 and 
ogg-opus-decoder
 libraries.
 
To serve the frontend assets, run this command from the root of the repo.
 
 
Since 
src/app.py
 imports the 
src/moshi.py
 module, this 
serve
 command also serves the Moshi websocket server as its own endpoint.
 
Deploy
 
 
When you’re ready to go live, use the 
deploy
 command to deploy the app to Modal.
 
 
Steal this example
 
 
The code for this entire example is 
available on GitHub
, so feel free to fork it and make it your own!
 
QuiLLMan: Voice Chat with Moshi
Code overview
FastAPI Server
Moshi Websocket Server
React Frontend
Deploy
Steal this example
