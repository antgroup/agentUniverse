## 阿里云SLS
如果您想使用阿里云SLS的相关功能，你需要安装log_ext相关依赖:
```shell
pip install agentuniverse[log_ext]
```
您需要在日志配置文件中进行以下配置：
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
- **`sls_log`**: 当您需要使用sls的时候该值必须为True
- **`sls_endpoint`**:阿里云sls的endpoint地址
- **`sls_project`**:阿里云sls的project
- **`sls_log_store`**:阿里云sls的log_store
- **`access_key_id`**:阿里云sls的ak
- **`access_key_secret`**:阿里云sls的sk
- **`sls_log_queue_max_size`**:AgentUniverse采用定时批量上送日志的形式，这个参数表示每次上送间隔中能缓存的最大日志条数。
- **`sls_log_send_interval`**:上送日志到sls的间隔，单位为秒

在配置完成后，您可以直接使用全局日志组件或是定制日志组件记录日志，AgentUniverse会自动将记录的内容上送至您的sls。