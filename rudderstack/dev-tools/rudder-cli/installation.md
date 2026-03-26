# Install Rudder CLI Alpha

Install the Rudder CLI tool in your preferred environment.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __2 minute read

  * 


[Rudder CLI](<https://github.com/rudderlabs/rudder-iac>) is a command-line interface tool designed to interact with RudderStack’s services, facilitating tasks like CLI-based configuration, management, and deployment of Tracking Plans and Data Catalog. See [CLI-based Tracking Plan Management](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/>) for more information on this feature.

> ![warning](/docs/images/warning.svg)
> 
> This tool is currently under active development and there may be frequent changes and updates to it.
> 
> Also, backward compatibility is not guaranteed at this stage.

## Install Rudder CLI

This section contains the Rudder CLI installation steps for your preferred platform.

### macOS

You can install the Rudder CLI on macOS devices depending on your chip configuration:
    
    
    curl -L https://github.com/rudderlabs/rudder-iac/releases/latest/download/rudder-cli_Darwin_arm64.tar.gz | tar -xz rudder-cli
    sudo mv rudder-cli /usr/local/bin/
    
    
    
    curl -L https://github.com/rudderlabs/rudder-iac/releases/latest/download/rudder-cli_Darwin_x86_64.tar.gz | tar -xz rudder-cli
    sudo mv rudder-cli /usr/local/bin/
    

### Linux

Run the following command to install Rudder CLI in your Linux machine:
    
    
    curl -L https://github.com/rudderlabs/rudder-iac/releases/latest/download/rudder-cli_Linux_x86_64.tar.gz | tar -xz rudder-cli
    sudo mv rudder-cli /usr/local/bin/
    

### Docker

You can run the Rudder CLI tool directly via Docker by running the following command:
    
    
    docker run rudderlabs/rudder-cli
    

If you need to persist your configuration or provide an external configuration file, you can mount your local configuration directory into the container.

Assuming your configuration directory is located at `~/.rudder`, you can run the following command:
    
    
    docker run -v ~/.rudder:/.rudder rudderlabs/rudder-cli
    

To run commands with the local data catalog files, mount the directory containing your files and use the `-l` flag, as shown:
    
    
    docker run -v ~/.rudder:/.rudder -v ~/my-catalog:/catalog rudderlabs/rudder-cli apply --dry-run -l /catalog
    

The above command uses the access token from your local configuration file and the Catalog files from the `/catalog` directory.

You can also use the `RUDDERSTACK_ACCESS_TOKEN` environment variable to provide the access token, as shown:
    
    
    docker run -v ~/my-catalog:/catalog -e RUDDERSTACK_ACCESS_TOKEN=your-access-token rudderlabs/rudder-cli apply --dry-run -l /catalog
    

## Build Rudder CLI from source

> ![warning](/docs/images/warning.svg)
> 
> Make sure to have Go installed and set up in your environment before following the steps in this section.

Run the following commands in order:
    
    
    git clone https://github.com/rudderlabs/rudder-iac.git
    cd rudder-iac
    make build
    sudo mv bin/rudder-cli /usr/local/bin/
    

The `make build` command is used to run the build process.