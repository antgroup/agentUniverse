# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2024/10/18 17:30
# @Author  : jijiawei
# @Email   : jijiawei.jjw@antgroup.com
# @FileName: security_configer.py


from typing import Optional

from agentuniverse.base.config.component_configer.component_configer import ComponentConfiger
from agentuniverse.base.config.configer import Configer


class SecurityConfiger(ComponentConfiger):
    """The MemoryConfiger class, which is used to load and manage the Memory configuration."""

    def __init__(self, configer: Optional[Configer] = None):
        """Initialize the MemoryConfiger."""
        super().__init__(configer)
        self.__name: Optional[str] = None
        self.__description: Optional[str] = None
        self.__compliance: Optional[dict] = None
        self.__desensitization: Optional[dict] = None

    @property
    def name(self) -> Optional[str]:
        """Return the name of the Security."""
        return self.__name

    @property
    def description(self) -> Optional[str]:
        """Return the description of the Security."""
        return self.__description

    @property
    def compliance(self) -> Optional[dict]:
        """Return the compliance of the Security."""
        return self.__compliance

    @property
    def desensitization(self) -> Optional[dict]:
        """Return the desensitization of the Security."""
        return self.__desensitization

    def load(self) -> 'SecurityConfiger':
        """Load the configuration by the Configer object.
        Returns:
            MemoryConfiger: the MemoryConfiger object
        """
        return self.load_by_configer(self.__configer)

    def load_by_configer(self, configer: Configer) -> 'SecurityConfiger':
        """Load the configuration by the Configer object.
        Args:
            configer(Configer): the Configer object
        Returns:
            MemoryConfiger: the MemoryConfiger object
        """
        super().load_by_configer(configer)

        try:
            self.__name = configer.value.get('name')
            self.__description = configer.value.get('description')
            self.__compliance = configer.value.get('compliance')
            self.__desensitization = configer.value.get('desensitization')
        except Exception as e:
            raise Exception(f"Failed to parse the Security configuration: {e}")
        return self
