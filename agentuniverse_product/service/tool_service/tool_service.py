# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/7/25 23:16
# @Author  : wangchongshi
# @Email   : wangchongshi.wcs@antgroup.com
# @FileName: tool_service.py
import os
from typing import List

from agentuniverse.agent.action.tool.tool import Tool
from agentuniverse.agent.action.tool.tool_manager import ToolManager
from agentuniverse.base.component.component_enum import ComponentEnum
from agentuniverse_product.base.product import Product
from agentuniverse_product.base.product_manager import ProductManager
from agentuniverse_product.base.util.yaml_util import write_yaml_file
from agentuniverse_product.service.model.tool_dto import ToolDTO
from agentuniverse_product.service.util.agent_util import register_product
from agentuniverse_product.service.util.common_util import get_core_path
from agentuniverse_product.service.util.tool_util import assemble_api_tool_config_data, \
    assemble_tool_product_config_data, register_tool, validate_create_api_tool_parameters


class ToolService:
    """Tool Service for aU-product."""

    @staticmethod
    def get_tool_list() -> List[ToolDTO]:
        """Get list of tools."""
        res = []
        product_list: List[Product] = ProductManager().get_instance_obj_list()
        if len(product_list) < 1:
            return res
        for product in product_list:
            if product.type == ComponentEnum.TOOL.value:
                tool_dto = ToolDTO(nickname=product.nickname, avatar=product.avatar, id=product.id)
                tool = product.instance
                tool_dto.description = tool.description
                tool_dto.parameters = tool.input_keys
                res.append(tool_dto)
        return res

    @staticmethod
    def get_tool_detail(tool_id: str) -> ToolDTO | None:
        """Get the tool detail.

        Args:
            tool_id (str): The id of the tool.

        Returns:
            ToolDTO | None: The tool detail.
        """
        if tool_id is None:
            return None
        tool: Tool = ToolManager().get_instance_obj(tool_id)
        if tool is None:
            return None
        product: Product = ProductManager().get_instance_obj(tool_id)
        tool_dto = ToolDTO(nickname=product.nickname if product else '',
                           avatar=product.avatar if product else '',
                           id=tool_id, description=tool.description, parameters=tool.input_keys)
        if hasattr(tool, 'openapi_spec'):
            tool_dto.openapi_schema = tool.openapi_spec
        return tool_dto

    @staticmethod
    def create_tool(tool_dto: ToolDTO) -> str:
        """Create a new tool instance.

        Args:
            tool_dto (ToolDTO): The tool DTO.

        Returns:
            str: The id of the tool.
        """
        # validate parameters
        validate_create_api_tool_parameters(tool_dto)

        # assemble product config data
        product_config_data = assemble_tool_product_config_data(tool_dto)

        # write product YAML file
        product_file_name = f"{tool_dto.id}_product"
        path = get_core_path()
        product_file_path = path / 'product' / 'tool' / f"{product_file_name}.yaml" if path \
            else os.path.join('..', '..', 'platform', 'difizen', 'product', 'tool', f"{product_file_name}.yaml")
        write_yaml_file(str(product_file_path), product_config_data)

        # assemble tool config data
        tool_config_data = assemble_api_tool_config_data(tool_dto)

        # write tool YAML file
        tool_file_path = path / 'tool' / f"{tool_dto.id}.yaml" if path \
            else os.path.join('..', '..', 'intelligence', 'agentic', 'tool', f"{tool_dto.id}.yaml")
        write_yaml_file(str(tool_file_path), tool_config_data)

        # register product and tool instance
        register_tool(str(tool_file_path))
        register_product(str(product_file_path))
        return tool_dto.id
