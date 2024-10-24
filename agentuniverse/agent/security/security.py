import json
from typing import Optional

from agentuniverse.agent.input_object import InputObject

from agentuniverse.agent.output_object import OutputObject

from agentuniverse.agent.security.compliance.compliance_base import ComplianceWorker
from agentuniverse.base.config.application_configer.application_config_manager import ApplicationConfigManager

from agentuniverse.base.component.component_enum import ComponentEnum

from agentuniverse.base.component.component_base import ComponentBase
from agentuniverse.base.config.component_configer.configers.security_configer import SecurityConfiger


class Security(ComponentBase):
    name: Optional[str] = ""
    description: Optional[str] = None
    compliance: ComplianceWorker = None
    desensitization: ComplianceWorker = None

    def __init__(self, **kwargs):
        super().__init__(component_type=ComponentEnum.SECURITY, **kwargs)

    def set_by_agent_model(self, **kwargs):
        """ Assign values of parameters to the Memory model in the agent configuration."""
        # note: default shallow copy
        copied_obj = self.model_copy()
        if 'memory_key' in kwargs and kwargs['memory_key']:
            copied_obj.memory_key = kwargs['memory_key']
        if 'max_tokens' in kwargs and kwargs['max_tokens']:
            copied_obj.max_tokens = kwargs['max_tokens']
        return copied_obj

    def get_instance_code(self) -> str:
        """Return the full name of the tool."""
        appname = ApplicationConfigManager().app_configer.base_info_appname
        return f'{appname}.{self.component_type.value.lower()}.{self.name}'

    def pre_invoke(self, input_object: InputObject):
        if not self.compliance:
            return
        self.compliance_check(input_object.get_data('input'))

    def compliance_check(self, input_text: str):
        compliance_worker = ComplianceWorker()
        compliance_worker.initialize_by_config(self.compliance)
        compliance_worker.execute(input_text)

    def desensitize(self, input_text: str):
        return input_text

    def final_invoke(self, output_object: OutputObject):
        """
        concurrent exec compliance and desentialize
        """
        if self.compliance:
            self.compliance_check(output_object.get_data('output'))
        if self.desensitization:
            self.desensitize(output_object.get_data('output'))
        return

    def compliance_check_stream(self, stream_output: dict):
        if not self.compliance:
            return

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
            # compliance_worker = ComplianceWorker()
            # compliance_worker.initialize_by_config(component_configer.compliance)
            self.compliance = ComplianceWorker(component_configer.compliance)
        if component_configer.desensitization:
            self.desensitization = component_configer.desensitization
        return self
