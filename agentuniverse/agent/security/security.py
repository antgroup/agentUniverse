from typing import Optional


from agentuniverse.base.config.application_configer.application_config_manager import ApplicationConfigManager

from agentuniverse.base.component.component_enum import ComponentEnum

from agentuniverse.base.component.component_base import ComponentBase
from agentuniverse.base.config.component_configer.configers.security_configer import SecurityConfiger


class Security(ComponentBase):
    name: Optional[str] = ""
    description: Optional[str] = None
    compliance: ComponentBase = None
    desensitization: ComponentBase = None

    def __init__(self, **kwargs):
        super().__init__(component_type=ComponentEnum.SECURITY, **kwargs)

    def get_instance_code(self) -> str:
        """Return the full name of the tool."""
        appname = ApplicationConfigManager().app_configer.base_info_appname
        return f'{appname}.{self.component_type.value.lower()}.{self.name}'

    def input_process(self, kwargs: dict):
        """
        check compliance for input text
        """
        if self.compliance.run(**kwargs):
            raise Exception('Compliance check failed')

    def output_process(self, kwargs: dict):
        """
        check compliance and de for output text
        """
        if self.compliance.run(**kwargs):
            raise Exception('Compliance check failed')
        return self.desensitization.run(**kwargs)

    def content_process(self, kwargs: dict):
        """
        check of compliance for output text
        """
        if not self.compliance.run(**kwargs):
            raise Exception('Compliance check failed')
        return self.desensitization.run(**kwargs)

    def initialize_by_component_configer(self, component_configer: SecurityConfiger) -> 'Security':
        """Initialize the memory by the ComponentConfiger object.
        Args:
            component_configer(MemoryConfiger): the ComponentConfiger object
        Returns:
            Memory: the Memory object
        """
        if component_configer.name:
            self.name = component_configer.name
        if component_configer.description:
            self.description = component_configer.description
        if component_configer.compliance:
            self.compliance = self.init_executor(component_configer.compliance)
        if component_configer.desensitization:
            self.desensitization = self.init_executor(component_configer.desensitization)
        return self

    def init_executor(self, config: dict):
        from agentuniverse.base.component.component_configer_util import ComponentConfigerUtil
        component_manager_clz = ComponentConfigerUtil.get_component_manager_clz_by_type(
            ComponentEnum.from_value(config.get('type')))
        return component_manager_clz().get_instance_obj(config.get('name'))