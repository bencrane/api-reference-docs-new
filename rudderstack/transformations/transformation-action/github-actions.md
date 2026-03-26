# How to Deploy RudderStack Transformations with GitHub Actions

Automate transformation testing and deployment with GitHub Actions.

* * *

  * __2 minute read

  * 


This guide lists the steps to use GitHub Actions to automatically test and deploy transformations whenever you push changes to your repository.

## Prerequisites

Before you begin, ensure you have the following:

  * A RudderStack workspace with existing transformations
  * A GitHub repository for version control
  * Generate a [workspace-level Service Access Token](<https://www.rudderstack.com/docs/access-management/service-access-tokens/#workspace-sat>) with the following permissions:

Resource| Permissions  
---|---  
Transformations| **Edit** , **Connect** , **Create & Delete**  
Transformation Libraries| **Edit**  
  
  * GitHub Actions enabled in your repository


## 1\. Export transformation code to your Git repository

Use the [Transformations API](<https://www.rudderstack.com/docs/api/transformation-api/>) to retrieve your existing transformations and organize them in your repository.

Structure your repository with the following directories:

Directory| Notes  
---|---  
`./transformations/code/`| Store your `.js` or `.py` transformation files here  
`./transformations/meta.json`| Define metadata for all transformations and libraries  
`./transformations/testevents.json` and `expectedoutput.json`| Store test inputs and expected outputs  
  
> ![tip](/docs/images/tip.svg)
> 
> **Tip:** Use the [sample-user-transformers repository](<https://github.com/rudderlabs/sample-user-transformers>) as a reference template for your setup.

## 2\. Create the `meta.json` file

Define your transformations and libraries in a `meta.json` file — this file specifies the location, language, and testing configuration for each transformation.

An example configuration is shown below:
    
    
    {
      "transformations": [
        {
          "file": "./code/my_transform.js",
          "name": "cleanNulls",
          "language": "javascript",
          "description": "Remove null properties",
          "test-input-file": "./code/testevents.json",
          "expected-output": "./code/expectedoutput.json"
        }
      ],
      "libraries": [
        {
          "file": "./code/utils.js",
          "name": "utils",
          "language": "javascript",
          "description": "Reusable utility functions"
        }
      ]
    }
    

## 3\. Configure GitHub Actions workflow

Create a workflow file at `.github/workflows/deploy-transforms.yml` to automate testing and deployment:
    
    
    name: Deploy RudderStack Transformations
    
    on:
      push:
        branches: [ main ]
        paths:
          - 'transformations/**'
    
    jobs:
      test-and-publish:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v4
          
          - name: Test & Publish Transformations
            uses: rudderlabs/rudder-transformation-action@<latest_version>
            with:
              metaPath: './transformations/meta.json'
              email: ${{ secrets.RS_EMAIL }}
              accessToken: ${{ secrets.RS_ACCESS_TOKEN }}
              uploadTestArtifact: true
    

This workflow triggers automatically when you push changes to the `transformations/**` directory on your main branch.

## 4\. Set up GitHub secrets

  1. Navigate to your repository **Settings** > **Secrets and variables** > **Actions**.

  2. Create the following repository secrets:

     * `RS_EMAIL`: Email address associated with your RudderStack workspace
     * `RS_ACCESS_TOKEN`: Workspace-level Service Access Token with **Editor** or **Admin** permissions


Note that:

  * Your GitHub Actions workflow uses these secrets to authenticate with RudderStack and deploy your transformations.
  * For security purposes, RudderStack recommends using [GitHub secrets](<https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository>) to store your Service Access Token.


## See more

  * [Transformations Overview](<https://www.rudderstack.com/docs/transformations/overview/>)
  * [Transformation Action Overview](<https://www.rudderstack.com/docs/transformations/transformation-action/>)
  * [Transformations API Reference](<https://www.rudderstack.com/docs/api/transformation-api/>)
  * [GitHub Actions Overview](<https://docs.github.com/en/actions>)