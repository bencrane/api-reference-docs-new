# Server-Transformer Compatibility

* * *

  *  __less than a minute

  * 


Before October 30, 2024, [`rudder-server`](<https://github.com/rudderlabs/rudder-server/>) was compatible with **any** version of `rudder-transformer`.

Going forward, the `rudder-server` releases will have a dependency on specific minimum required versions of `rudder-transformer` and vice versa - allowing the team to focus on releasing high quality integrations and reducing the maintenance of older implementations.

> ![warning](/docs/images/warning.svg)
> 
> To avoid any breaking changes to your pipelines, use the latest **minor** releases of [`rudder-server`](<https://github.com/rudderlabs/rudder-server/releases>) and [`rudder-transformer`](<https://github.com/rudderlabs/rudder-transformer/releases>).

See the below table for more information:

Date| Server version| Transformer version| Details  
---|---|---|---  
Till October 30, 2024| Any| Any| -  
October 30, 2024| v1.37| v1.50.0 and above| [Here](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/server-transformer-compatibility/oct-2024/>)  
April 9, 2025| v1.41 and above| v1.97.0| [Here](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/server-transformer-compatibility/april-2025/>)