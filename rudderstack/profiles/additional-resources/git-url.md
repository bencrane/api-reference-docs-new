# Supported Git URLs

> Version: Latest (0.25 — Beta)0.240.230.220.210.200.190.180.170.160.150.140.130.120.110.100.9.40.9.30.9.10.9.00.8.0

# Supported Git URLs

Learn about the supported Git URLs in Profiles.

* * *

  * __less than a minute

  * 


> ![info](/docs/images/info.svg)
> 
> This section is applicable for Profiles CLI project.
> 
> To know about the supported Git URLs in the RudderStack dashboard, see the [Import from Git](<https://www.rudderstack.com/docs/profiles/management/import-from-git/#steps>) guide.

Profiles supports Git URLs for packages in the `ssh://git@host:port/path.git` format.

For private repos, RudderStack only supports SSH Git URLs. You need to add credentials to the [`siteconfig.yaml`](<https://www.rudderstack.com/docs/profiles/dev-docs/site-configuration-file/>) and public SSH key manually to the platforms.

The URL scheme doesn’t depend on individual Git provider host. You can use the below-mentioned Git URLs:

| URL Syntax| Format (Example)  
---|---|---  
URL for the default branch of a repository| `https://<provider-host>/<org-name>/<repo-name>/path/to/project`| **Github** : `https://github.com/rudderlabs/librs360-shopify-features/shopify-features`  
  
**Gitlab** : `https://gitlab.com/rudderlabs/librs360-shopify-features/shopify-features`  
  
**Bitbucket** :`https://bitbucket.org/rudderlabs/librs360-shopify-features/shopify-features`  
SSH URL for the default branch of a private repository| `git@<provider-host>:<org-name>/<repo-name>/path/to/project`| **Github** : `git@github.com:rudderlabs/librs360-shopify-features/shopify-features`  
  
**Gitlab** : `git@gitlab.com:rudderlabs/librs360-shopify-features/shopify-features`  
  
**Bitbucket** :`git@gbitbucket.org:rudderlabs/librs360-shopify-features/shopify-features`  
  
**Azure DevOps** : `git@ssh.dev.azure.com:v3/rudderlabs/profiles-project/librs360-shopify-features`  
URL for a specific branch of a repository| `https://<provider-host>/<org-name>/<repo-name>/tree/<branch-name>/path/to/project`| **Github** : `https://github.com/rudderlabs/librs360-shopify-features/tree/main/shopify-features`  
  
**Gitlab** : `https://gitlab.com/rudderlabs/librs360-shopify-features/tree/main/shopify-features`  
  
**Bitbucket** :`https://bitbucket.org/rudderlabs/librs360-shopify-features/tree/main/shopify-features`  
URL for a specific tag within the repository| `https://<provider-host>/<org-name>/<repo-name>/tag/<tag-name>/path/to/project`| **Github** : `https://github.com/rudderlabs/librs360-shopify-features/tag/wht_test/shopify-features`  
  
**Gitlab** : `https://gitlab.com/rudderlabs/librs360-shopify-features/tag/wht_test/shopify-features`  
  
**Bitbucket** :`https://bitbucket.org/rudderlabs/librs360-shopify-features/tag/wht_test/shopify-features`  
URL for a specific commit within the repository| `https://<provider-host>/<org-name>/<repo-name>/commit/<commit-hash>/path/to/project`| **Github** : `https://github.com/rudderlabs/librs360-shopify-features/commit/b8d49/shopify-features`  
  
**Gitlab** : `https://gitlab.com/rudderlabs/librs360-shopify-features/commit/b8d49/shopify-features`  
  
**Bitbucket** :`https://bitbucket.org/rudderlabs/librs360-shopify-features/commit/b8d49/shopify-features`  
  
  * [![](/docs/images/previous.svg)Previous](</docs/profiles/additional-resources/sample-data/>)
  * [Next ![](/docs/images/next.svg)](</docs/profiles/additional-resources/glossary/>)