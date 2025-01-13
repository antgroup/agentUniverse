# Service Information Storage

agentUniverse utilizes a system-level database to store various types of information generated during application runtime, including the results of asynchronous service requests, which are stored within this database.

## System Database Configuration
You can configure the system database address in the `config.toml` file:
```toml
[DB]
# A sqlalchemy db uri used for storing various info, for example, service request, generated during application running.
# If it's empty, agentUniverse will create a local sqlite db as default choice.
system_db_uri = ''
```
Please note that this URI must comply with the URI format specification required by SQLAlchemy. If this value is left empty, a DB folder will be created in the project's root directory, and within that folder, a SQLite database file named `agent_universe.db` will be created to serve as the default system database. If you wish to obtain more information on how to use the system database, you can refer to the [SQLDB_WRAPPER](../Storage/SQLDB_WRAPPER.md) section, where the system database is registered with the name `__system_db__`.



## Service Information Table Format
agentUniverse uses the following ORM to store request information:
```text
class RequestORM(Base):
    """SQLAlchemy ORM Model for RequestDO."""
    __tablename__ = 'request_task'
    id = Column(Integer, primary_key=True, autoincrement=True)
    request_id = Column(String(20), nullable=False)
    query = Column(Text)
    session_id = Column(String(50))
    state = Column(String(20))
    result = Column(JSON)
    steps = Column(JSON)
    additional_args = Column(JSON)
    gmt_create = Column(DateTime, default=datetime.datetime.now)
    gmt_modified = Column(DateTime, default=datetime.datetime.now,
                          onupdate=datetime.datetime.now)
```
● id: An auto-incremented primary key.
● request_id: A unique identifier for each request.
● state: Represents the execution state of the agent task associated with the request.
● result: The execution result of the task.
● steps: Intermediate outputs generated during the execution process.
● session_id and additional_args: Reserved fields in the current version of the framework.