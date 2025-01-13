## Aliyun SLS
If you want to use aliyun sls, you should install agentUniverse in this way:
```shell
pip install agentuniverse[log_ext]
```

You will need to make the following configuration in the log configuration file:
```toml
[LOG_CONFIG.EXTEND_MODULE]
# Whether use aliyun simple log server. If value is True, you should fill the ALIYUN_SLS_CONFIG below.
sls_log = "True"

[LOG_CONFIG.ALIYUN_SLS_CONFIG]
# Aliyun sls endpoint.
sls_endpoint = "mock_endpoint"
# Your sls log project name.
sls_project = "mock_project"
# Your sls log store name.
sls_log_store = "mock_log_store"
# Aliyun sls access_key_id.
access_key_id = "mock_key_id"
# Aliyun sls access_key_secret.
access_key_secret = "mock_key_secret"
# Log queue max size, antfinagentframework uses a queue to save the logs to be sent, they will be sent periodically.
sls_log_queue_max_size = 1000
# Interval of sending logs to aliyun sls.
sls_log_send_interval = 3.0
```
- **`sls_log`**: This must be True if you need to use sls.
- **`sls_endpoint`**: The endpoint address for Aliyun sls.
- **`sls_project`**: The project in Aliyun sls.
- **`sls_log_store`**: The log store in Aliyun sls.
- **`access_key_id`**: The access key id for Aliyun sls.
- **`access_key_secret`**: The access key secret for Aliyun sls.
- **`sls_log_queue_max_size`**: The AgentUniverse employs a mechanism for timed batch uploading of logs, where this parameter signifies the maximum number of log entries that can be cached during each upload interval.
- **`sls_log_send_interval`**: The interval for uploading logs to sls, in seconds.

 After configuration, you can directly use the global log component or your custom log components to record logs. AgentUniverse will automatically upload the recorded logs to your specified sls project and log store.