# Import Resources Troubleshooting Guide Alpha

Troubleshoot common issues when importing workspace resources to your CLI project.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __less than a minute

  * 


This guide covers common validation and error handling scenarios you may encounter when importing workspace resources into your CLI project.

## Unsynced changes in project

If your project has unsynced changes, running the `import workspace` command will give you the following error:
    
    
    Error: import not allowed as project has changes to be synced
    

**Solution** : To resolve this issue, apply your existing changes first by running the `apply` command, then run the `import workspace` command again.

## Imported directory already exists

If an `imported` directory already exists in your project, the `import workspace` command will fail with the following error:
    
    
    Error: directory for import: my-project/imported already exists
    

**Solution** : Move the contents of the existing `imported` directory to a different location within your Rudder CLI project directory, remove the `imported` directory, and re-run the `import workspace` command.