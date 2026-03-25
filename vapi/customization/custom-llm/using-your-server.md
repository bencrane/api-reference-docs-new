# Connecting Your Custom LLM to Vapi: A Comprehensive Guide

## Overview

This documentation explains how to integrate Vapi with OpenAI's gpt-4.1-mini model using a custom LLM setup. The guide demonstrates "leveraging Ngrok to expose a local development environment for testing and" the interaction between Vapi and your language model.

## Prerequisites

To get started, you'll need:

* Access to a Vapi account dashboard
* An OpenAI API key with gpt-4.1-mini model availability
* Python with the OpenAI library installed
* Ngrok for creating public URLs to local servers
* Reference materials from the Flask example repository

## Step 1: Local Development Setup

Create a Flask application with a `/chat/completions` POST endpoint. The basic structure involves:

1. Setting up a Python script (app.py) that imports Flask and OpenAI libraries
2. Configuring your OpenAI API key
3. Creating a route handler that receives JSON data and processes chat requests
4. Running the Flask server locally on a designated port
5. Exposing the local server via Ngrok to generate a public URL

## Step 2: Vapi Configuration

Configure your integration by:

1. Accessing the Vapi Dashboard's Model section
2. Selecting the Custom LLM option
3. Entering your Ngrok-generated URL as the endpoint
4. Testing the connection with sample messages

## Authentication Methods

Vapi supports two authentication approaches:

**API Key Authentication**: "Vapi sends your API key in the Authorization header to your custom LLM endpoint" where your server validates it before processing requests.

**OAuth2 Authentication**: A more secure option using client credentials flow with automatic token refresh, requiring an OAuth2 endpoint, client ID, and client secret.

## Step 3: Communication Flow

The interaction sequence follows seven steps:

1. Vapi sends a POST request with conversation context
2. Your local server receives and processes the request
3. Relevant data gets extracted and prepared
4. The OpenAI API is called with the constructed prompt
5. The response is formatted according to Vapi's structure
6. The formatted response returns to Vapi
7. Vapi displays the generated text to the user

## Video Tutorial

A video demonstration is available embedding the complete integration workflow.
