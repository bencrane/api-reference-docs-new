# Python Multi-version Support

> Version: Latest (0.25 — Beta)0.240.230.220.210.200.190.180.170.160.150.140.130.120.110.100.9.40.9.30.9.10.9.00.8.0

# Python Multi-version Support

Define constraints on your Profiles project to run on specific versions of Python.

* * *

  * __less than a minute

  * 


> ![info](/docs/images/info.svg)
> 
> This feature is supported for the Profiles versions 0.10.8, 0.11.5, 0.12.0, and all versions after 0.12.0.

You can constraint your Profiles project to run only on specific version(s) by specifying it in the [`pb_project.yaml`](<https://www.rudderstack.com/docs/profiles/dev-docs/pb-project-yaml/>) file, under the `python_requirements` key.

For example, the following snippet shows how to run your project on v0.10.8:
    
    
    python_requirements:
      - profiles-rudderstack==0.10.8
    

Use the following snippet to stay on any minor version between 0.12.0 and 0.13.0. If a new minor version is released, your project will be auto-migrated to that version:
    
    
    python_requirements:
      - profiles-rudderstack>=0.12.0,<0.13.0
    

If you do not specify any version in [`pb_project.yaml`](<https://www.rudderstack.com/docs/profiles/dev-docs/pb-project-yaml/>), the latest Profiles version is used by default. The version constraints follow the same syntax as those of [Python dependency specifiers](<https://packaging.python.org/en/latest/specifications/dependency-specifiers/>).

> ![warning](/docs/images/warning.svg)
> 
> Make sure that the version of Profiles project is the same in your environment and the [`pb_project.yaml`](<https://www.rudderstack.com/docs/profiles/dev-docs/pb-project-yaml/>) file. Otherwise, RudderStack will throw an error.

  * [![](/docs/images/previous.svg)Previous](</docs/profiles/additional-resources/run-process/>)
  * [Next ![](/docs/images/next.svg)](</docs/profiles/additional-resources/sample-data/>)