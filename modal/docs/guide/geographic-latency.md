# Geographic Latency

Modal’s container cluster is multi-cloud and multi-region. The vast majority of containers are located in the continental USA, but we do run containers across the globe.

By default, all inputs to Modal containers go through our control plane in Virginia, USA (us-east) before being sent to a container for execution. Cloudping.co provides good estimates of the latency between regions. For example, the round-trip latency between AWS us-east (Virginia, USA) and us-west (California, USA) is around 60ms.

You can observe the location identifier of a container via an environment variable. Logging this environment variable alongside latency information can reveal when geography is impacting your application performance.

Optimizing latency 

Modal has a variety of tools to optimize network latency, even down to ~10ms in extreme cases like real-time robotics. One such tool is region selection, which tells Modal to only schedule your container in a certain region, e.g. us-east. Note that inputs still go through our control plane in this setting.

To optimize latency further, please contact us on Slack or at support@modal.com.
