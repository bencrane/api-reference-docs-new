# Ingesting tracking events with webhooks

Ingesting tracking events from Lob has been made easy. With List endpoints, `GET` endpoints, and webhooks, you can ingest events for a specific mail piece, run a monthly data pull from Lob's system for mail pieces that don't have a certain event, or get real-time updates as your mail piece goes through the mail stream.

## Why is this important? <a href="#why-is-this-important-0" id="why-is-this-important-0"></a>

Ingesting tracking events from Lob can unlock a slew of functionality for an organization. By ingesting this data from Lob, you can integrate direct mail into your omni-channel workflows, surface data internally for reporting purposes, provide updates to customers to improve their customer experience, and much more.

If someone needs to monitor tracking events in near real-time, and subsequently build additional triggers off of those events, then they have to take a few more steps during integration. That includes setting up an API endpoint for Lob to send data to, as well as developing the logic that each event should follow in their internal systems. For example, “processed for delivery” events could trigger an email to be sent.

## How do we (programmatically) solve this problem? <a href="#how-do-we-programmatically-solve-this-problem-1" id="how-do-we-programmatically-solve-this-problem-1"></a>

First, you need to understand the model by which you want to receive or fetch this data. If you desire to receive data in real time, then you will need to **set up a webhook endpoint for Lob to send data to**. You can subscribe to a list of events in the Lob dashboard and then build on top of these events inside of your application. keep in mind, customers should have systems in place that, in the event their endpoint goes down, that will enable them to backfill the data they need. If they need to retrieve tracking events on-demand, then having the systems in place to do so is imperative.

For the fetch model, systems can be put into place to **programmatically retrieve mail pieces details**, either in batches or per resource, and extract their most up-to-date tracking data. To do this, you can either use our `GET` endpoints to retrieve all of the current information for a specific mail piece, or you can use our `LIST` endpoint to retrieve multiple letters at once based on the desired filtering such as metadata filters, date filters, etc. This model can be used in many ways to help enable your business, but most commonly these are run on a daily/weekly cadence, or they are run ad hoc when the webhook ingestion process has failed to ingest the data.

![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1656696643815-diagram.jpeg)

## Setting up an endpoint to receive data from Lob <a href="#setting-up-an-endpoint-to-receive-data-from-lob-2" id="setting-up-an-endpoint-to-receive-data-from-lob-2"></a>

In this guide, we’ll share the steps and code you’ll need to stand up an endpoint to receive data from Lob. The code is designed to run on your local machine in order to test out receiving webhooks from Lob during development. In order for Lob to reach the endpoint you’ll use ngrok, a cross-platform application that exposes local server ports to the Internet.

To follow along with this guide, you will need:

* A [Lob account](https://dashboard.lob.com/register)
* [ngrok](https://ngrok.com/download) installed on your laptop
* A webhook configured in your Lob.com account (we’ll show you how below)

### Set up a new project <a href="#set-up-a-new-project-3" id="set-up-a-new-project-3"></a>

Let’s start by creating a folder for our project and installing any libraries.

{% tabs %}
{% tab title="TypeScript" %}
Create a new directory, switch to it, and initialize your project from your terminal app with these commands.

{% embed url="<https://gist.github.com/lobot/d1cfe507e47b51611ed90ece6d196296#file-webhook-ts-setup>" %}

For this example, we’ll use KOA an HTTP middleware framework for node.js along with supporting libraries.

{% embed url="<https://gist.github.com/lobot/2fb1353ad8fcb0121282cea660402e6a#file-webhook-ts-koa-npm-install>" %}

Create two directories to hold our typescript file and our compiled javascript file.

{% embed url="<https://gist.github.com/lobot/2f8d1b11158ba6ef13d4169e6f43ab7d#file-webhook-ts-koa-add-dirs>" %}

We’re also going to add nodejs-specific type definitions as a dev dependency. Otherwise, the TS compiler would complain about some globally available objects that it doesn’t know about.

{% embed url="<https://gist.github.com/lobot/7e8dafbf52256a5001587aca9ce6cee4#file-webhook-ts-add-type-definitions>" %}

Let's configure how the compiler works in the project by creating a new file called tsconfig.json and setting some values.

{% embed url="<https://gist.github.com/lobot/529e71e7cd87c67f8a7e91d28a440aa2#file-webhook-ts-tsconfig-json>" %}

Lastly, we’ll update package.json so main equals “/dist/index.js”

{% embed url="<https://gist.github.com/lobot/27dbee0c84635625f836be821072f63d#file-webhook-ts-package-json>" %}
{% endtab %}
{% endtabs %}

### Creating a webhook endpoint <a href="#creating-a-webhook-endpoint-4" id="creating-a-webhook-endpoint-4"></a>

Now all our dependencies are installed on your local machine, we’ll add the code for our endpoint.

Open the text editor of your choice (if you need to download one, we recommend Visual Studio Code) and paste the code in the language of your choice.

{% tabs %}
{% tab title="TypeScript" %}
Open index.ts and copy and paste the following code.

{% embed url="<https://gist.github.com/lobot/f3032563cc8a4ac9d4b37676fb6c930f#file-webhook-ts-index-ts>" %}

Return to your terminal and from the project folder run your code.

{% embed url="<https://gist.github.com/lobot/8f07674dbeed2048ebc5b5ece5e98240#file-webhook-ts-run-code>" %}
{% endtab %}
{% endtabs %}

### Launch ngrok <a href="#launch-ngrok-5" id="launch-ngrok-5"></a>

As mentioned, we’ll use ngrok to expose your webhook endpoint to the internet.

In another terminal window, navigate to the folder where you installed ngrok and run the command

{% embed url="<https://gist.github.com/lobot/5397add2400f6958effeb112807215b2#file-webhook-ts-run-ngrok>" %}

You’ll see a forwarding URL for https connections.  You’ll copy this for use when configuring your webhook in Lob in the next section.

![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1656708170607-Screen%20Shot%202022-07-01%20at%201.42.40%20PM.png)

### Configure your webhook in Lob <a href="#configure-your-webhook-in-lob-6" id="configure-your-webhook-in-lob-6"></a>

Login to your Lob.com account from the dashboard

* Click on Webhooks on the left side navigation.
* Click the Create button
* Give your webhook a description
* Check the boxes for all the events you want to receive notifications.
* Paste the ngrok forward URL and append “/webhooks” for your endpoint. Example: <https://03ed-67-170-227-250.ngrok.io/webhooks>
* Click the Create button

\
![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1656707103606-New-Webhook.png)

### Test using the debugger <a href="#test-using-the-debugger-7" id="test-using-the-debugger-7"></a>

After successfully creating your webhook in Lob, click the Debugger button. Then click the Send button. You should see a 200 OK message in the webhook response window.

![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1656708130880-Screen%20Shot%202022-07-01%20at%201.39.24%20PM.png)

## Further resources <a href="#further-resources-8" id="further-resources-8"></a>

* More about [Webhooks for tracking events](https://help.lob.com/print-and-mail/getting-data-and-results/using-webhooks)