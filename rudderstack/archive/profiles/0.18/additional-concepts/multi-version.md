# Multi-version Support

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Multi-version Support

Define constraints on your Profiles project to run on specific version(s).

* * *

  * __less than a minute

  * 


> ![info](/docs/images/info.svg)
> 
> This feature is supported for the Profiles versions 0.10.8, 0.11.5, 0.12.0, and all versions after 0.12.0.

You can constraint your Profiles project to run only on specific version(s) by specifying it in the `pb_project.yaml` file, under `python_requirements` key. For example, use the below snippet to run your project on v0.10.8:
    
    
    python_requirements:
      - profiles-rudderstack==0.10.8
    

Use the below snippet to stay on any minor version between 0.12.0 and 0.13.0. If a new minor version is released, your project will be auto-migrated to that version:
    
    
    python_requirements:
      - profiles-rudderstack>=0.12.0,<0.13.0
    

If you do not specify any version in `pb_project.yaml`, the latest Profiles version is used by default. The version constraints follow the same syntax as those of [Python dependency specifiers](<https://packaging.python.org/en/latest/specifications/dependency-specifiers/>).

Make sure that the version of Profiles project is the same in your environment and the `pb_project.yaml` file. Otherwise, RudderStack will throw an error.

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.18/additional-concepts/manage-models/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.18/additional-concepts/macros-window-functions/>)