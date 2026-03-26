# Migrate Snowflake Authentication to Key-Pair Auth in RudderStack

Migrate to Snowflake’s key-pair authentication mechanism for enhanced security.

* * *

  * __6 minute read

  * 


This guide shows you how to safely migrate from Snowflake’s username/password-based authentication to key-pair authentication across all the product integrations supported by RudderStack.

> ![info](/docs/images/info.svg)
> 
> Reach out to [RudderStack Support](<mailto:support@rudderstack.com>) if you need any help with migrating your Snowflake integrations to key-pair authentication.

## Introduction

RudderStack supports Snowflake’s [key-pair authentication](<https://docs.snowflake.com/en/user-guide/key-pair-auth>) across the following product integrations:

  * [Snowflake Reverse ETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/snowflake/#setting-up-the-snowflake-source-in-rudderstack>)
  * [Snowflake destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake/#connection-settings>)
  * [Snowflake warehouse for creating your Profiles project](<https://www.rudderstack.com/docs/releases/snowflake-key-pair-auth-profiles/>)


> ![warning](/docs/images/warning.svg)
> 
> Snowflake requires that all users have enabled two-factor authentication by April, 2025. At that time, key-pair authentication is required if you plan to authenticate a Snowflake user in RudderStack.

## Migration overview

**Estimated time: 15 minutes**

While completing this migration, you will be able to verify that your pipelines and jobs are functioning properly. Note that even if the key-pair authentication fails, and syncs and/or jobs fail, there will be **no** event loss and any syncs or jobs can be retried.

See below for verifying that your pipelines and jobs are properly authenticating after migrating to key-pair authentication.

## General migration steps

  1. [Generate a key-pair](<https://docs.snowflake.com/en/user-guide/key-pair-auth#configuring-key-pair-authentication>) (private and public key).

  2. Confirm the currently configured user for your RudderStack integration:


  * **Warehouse destination** : Navigate to your warehouse destination in RudderStack. Go to the **Configuration** tab and note the **User** field.

[![](/docs/images/user-guides/snowflake-key-pair-migration/snowflake-warehouse-destination.webp)](</docs/images/user-guides/snowflake-key-pair-migration/snowflake-warehouse-destination.webp>)

  * **Reverse ETL source** : Navigate to your Reverse ETL source in RudderStack. Go to the **Settings** tab and note the **User** field in the credentials box.

[![](/docs/images/user-guides/snowflake-key-pair-migration/snowflake-retl-source.webp)](</docs/images/user-guides/snowflake-key-pair-migration/snowflake-retl-source.webp>)

  * **Profiles project** : Navigate to your Profiles project in RudderStack. Go to the **Settings** tab and note the **User** field in the warehouse information box.

[![](/docs/images/user-guides/snowflake-key-pair-migration/snowflake-profiles.webp)](</docs/images/user-guides/snowflake-key-pair-migration/snowflake-profiles.webp>)

  3. Upload the public key to your Snowflake user.
  4. Update your RudderStack configuration to use the private key.
  5. Verify that the pipelines work correctly.
  6. (**Optional**) Turn on 2FA to disable the password-based login.


## Step 1: Get organized

Go through your RudderStack workspace and gather a list of all the following resources:

  * Snowflake warehouse destinations
  * Snowflake Reverse ETL sources
  * Snowflake Profiles projects


Take note of all the different users (**User** setting) that these different integrations utilize.

## Step 2: Generate a Snowflake key-pair

RudderStack supports both unencrypted and encrypted private keys.

> ![info](/docs/images/info.svg)
> 
> You can generate a Snowflake key-pair in your computer’s terminal. See the [Snowflake documentation](<https://docs.snowflake.com/en/user-guide/key-pair-auth#configuring-key-pair-authentication>) for more details on generating a key-pair.

#### Option 1: Unencrypted private key (no passphrase)
    
    
    # Generate a 2048-bit private key and convert to PKCS8 format
    openssl genrsa 2048 | openssl pkcs8 -topk8 -inform PEM -out rsa_key.p8 -nocrypt
    
    # Extract the public key
    openssl rsa -in rsa_key.p8 -pubout -out rsa_key.pub
    

#### Option 2: Encrypted private key (with passphrase)
    
    
    # Generate the private key
    openssl genrsa 2048 | openssl pkcs8 -topk8 -v2 des3 -inform PEM -out encrypted_rsa_key.p8
    
    # Generate a public key
    openssl rsa -in encrypted_rsa_key.p8 -pubout -out rsa_key.pub
    

Note that you will be prompted a few times to enter a passphrase.

## Step 3: Upload the public key to Snowflake

For every unique user found in Step 1, you will need to ensure that there is a public key assigned to them in Snowflake.

Follow these steps:

  1. Open the public key file (`rsa_key.pub`) and copy the **base64-encoded key block only** and **exclude** the `BEGIN` and `END` lines. A sample terminal code you can run to fetch your public key in the terminal is shown:


    
    
    cat rsa_key.pub
    

  * Then, from this information:


    
    
    -----BEGIN PUBLIC KEY-----
    MIIBIjANBgkq...
    -----END PUBLIC KEY-----
    

  * Use just the following:


    
    
    MIIBIjANBgkq...
    

  2. Run the following query in Snowflake:


    
    
    ALTER USER <your_user_name> SET RSA_PUBLIC_KEY='MIIBIjANBgkq...';
    

  3. (Optional) To rotate keys safely, you can also set a secondary key as shown:


    
    
    ALTER USER your_user_name SET RSA_PUBLIC_KEY_2='...';
    

## Step 4: Update RudderStack configuration

For every destination, source and Profiles project found in Step 1, you will need to update the configuration to use key-pair authentication.

You will need the **private key** and provide it to RudderStack for authenticating the integration.

A sample terminal code you can run to fetch your private key in the terminal:
    
    
    # example for unencrypted
    cat rsa_key.p8
    # example for encrypted
    cat encrypted_rsa_key.p8
    

> ![warning](/docs/images/warning.svg)
> 
> Protect this sensitive private key along with the passphrase (if applicable).

### Warehouse destination

  1. Go to the RudderStack dashboard.
  2. Navigate to your Snowflake warehouse destination and go to the **Configuration** tab.
  3. Turn on the **Use Key Pair Authentication** toggle.
  4. Paste the full contents of your private key file (`rsa_key.p8` or `encrypted_rsa_key.p8`).


> ![warning](/docs/images/warning.svg)
> 
> Include the `----BEGIN PRIVATE KEY-----` and `----END PRIVATE KEY-----` lines.

  5. For an encrypted key, provide the **Passphrase** used during the key generation.


> ![info](/docs/images/info.svg)
> 
> RudderStack requires a non-empty passphrase for encrypted private keys.

### Reverse ETL source

  1. Go to your Snowflake source.
  2. Go to the **Settings** tab and click on the **Edit** button next to the credentials.
  3. Click **Add new credentials** and make sure to choose **Key Pair Authentication**.
  4. Paste the full contents of your private key file (`rsa_key.p8` or `encrypted_rsa_key.p8`).


> ![warning](/docs/images/warning.svg)
> 
> Include the `----BEGIN PRIVATE KEY-----` and `----END PRIVATE KEY-----` lines.

  5. For an encrypted key, provide the **Passphrase** used during the key generation.


> ![info](/docs/images/info.svg)
> 
> RudderStack requires a non-empty passphrase for encrypted private keys.

  6. Save the changes to use the new credentials (existing credentials cannot be edited).


### Profiles project

  1. Go to the RudderStack dashboard.
  2. Navigate to your Snowflake Profiles project and click the **Settings** tab.
  3. Click the edit button in the **Warehouse Info**.
  4. Turn on the **Use Key Pair Authentication** toggle.
  5. Paste the full contents of your private key file (`rsa_key.p8` or `encrypted_rsa_key.p8`).


> ![warning](/docs/images/warning.svg)
> 
> Include the `----BEGIN PRIVATE KEY-----` and `----END PRIVATE KEY-----` lines.

  6. For an encrypted key, provide the **Passphrase** used during the key generation.


> ![info](/docs/images/info.svg)
> 
> RudderStack requires a non-empty passphrase for encrypted private keys.

## Step 5: Verify pipeline functionality

After updating to key-pair authentication, follow these steps to ensure that your pipelines, syncs, and jobs are still functioning properly:

### Warehouse destination

To save any changes to your warehouse destination, RudderStack will verify that the credentials are sufficient and validate access.

After the key-pair auth is configured, you can navigate to the **Configuration** tab for any of your warehouse destinations and select **Edit Configuration** > **Finish**. Doing so causes RudderStack to re-validate access even if no changes were made.

You can also ensure that your warehouse syncs are still happening correctly.

### Reverse ETL source

To save any changes to your Reverse ETL source, RudderStack will verify that the credentials are sufficient and validate access.

After switching your credentials to the new key-pair auth, you can navigate to the **Settings** tab for any of your Reverse ETL sources, and select the edit button for **Credentials** , and then **Verify**. Doing so causes RudderStack to re-validate access even if no changes were made.

You can also ensure that your Reverse ETL syncs are still happening correctly.

### Profiles project

To save the changes when you are configuring the key-pair authentication, press the **Verify Credentials** button. This ensures that the Profiles project is created or edited with sufficient authentication.

After the key-pair auth is configured, you can run a Profiles job and make sure it runs successfully.

## (Optional) Step 6: Enforce 2FA and remove password authentication

Once you have confirmed that all RudderStack pipelines are working correctly, you can enable 2FA in Snowflake for your user.