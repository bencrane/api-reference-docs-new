# Profiles Tutorials - Additional Concepts

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Profiles Tutorials - Additional Concepts

Additional concepts related to Profiles.

* * *

  * __less than a minute

  * 


## Best schema version (tags)

It is recommended to use git-tags instead of the latest commit on main branch of your library projects. For example, `https://github.com/org-name/lib-name/tag/schema_{{best_schema_version}}`. The selection of compatible git tags is done by PB, that is it will figure out the best compatible version for the lib package.

A sample project file:
    
    
    packages:
      - name: shopify_features
        url: https://github.com/org-name/lib-names/tag/schema_{{best_schema_version}}
        inputsMap:
          rsCartUpdate: inputs/rsCartUpdate
          rsIdentifies: inputs/rsIdentifies
    

Using this will make Profiles use the best compatible version of the library project in case of any schema updates.

> ![info](/docs/images/info.svg)
> 
> You don’t have to replace the placeholder `{{best_schema_version}}`. For instance, if `https://github.com/org-name/lib-names/tags/` has a tag for schema_44, then `https://github.com/org-name/lib-names/tag/schema_44` will be automatically used. In any case, if you replace the placeholder with actual tag name, the project will work without any issues.

## Using private Git repos via CLI

To use private Git repos using CLI, follow these steps:

  1. Generate the SSH Key. To do so, [refer this page](<https://git-scm.com/book/en/v2/Git-on-the-Server-Generating-Your-SSH-Public-Key>).
  2. Associate the SSH Key to your Git Project. Check the section on [Profile Builder CLI](<https://www.rudderstack.com/docs/archive/profiles/0.10/get-started/quickstart-ui/>)
  3. Add private keys as credentials, in the `siteconfig.yaml` file:


    
    
    gitcreds:
      - reporegex: git@<provider-host>:<org-name>/*
        key: |
        -----BEGIN OPENSSH PRIVATE KEY-----
        b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEb..........
        -----END OPENSSH PRIVATE KEY-----    
    

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.10/developer-guides/yaml-refresher/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.10/developer-guides/commands/>)