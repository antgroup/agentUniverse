# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/8/27 15:52
# @Author  : wangchongshi
# @Email   : wangchongshi.wcs@antgroup.com
# @FileName: plugin_service.py
import os
from typing import List

from agentuniverse_product.base.product import Product
from agentuniverse_product.base.product_manager import ProductManager
from agentuniverse_product.base.util.yaml_util import write_yaml_file
from agentuniverse_product.service.model.plugin_dto import PluginDTO
from agentuniverse_product.service.model.tool_dto import ToolDTO
from agentuniverse_product.service.tool_service.tool_service import ToolService
from agentuniverse_product.service.util.agent_util import register_product
from agentuniverse_product.service.util.common_util import get_core_path
from agentuniverse_product.service.util.plugin_util import assemble_plugin_product_config_data, \
    parse_openapi_yaml_to_tool_bundle, validate_create_plugin_parameters
from agentuniverse_product.service.util.tool_util import parse_tool_input


class PluginService:
    """Plugin Service for aU-product."""

    @staticmethod
    def get_plugin_list() -> List[PluginDTO]:
        """Get list of plugins."""
        res = []
        product_list: List[Product] = ProductManager().get_instance_obj_list()
        if len(product_list) < 1:
            return res
        for product in product_list:
            if product.type == 'PLUGIN':
                tool_id_list = product.toolset
                tool_dto_list = []
                if len(tool_id_list) > 0:
                    for tool_id in tool_id_list:
                        tool_dto: ToolDTO = ToolService().get_tool_detail(tool_id)
                        if tool_dto is None:
                            continue
                        tool_dto_list.append(tool_dto)
                plugin_dto = PluginDTO(nickname=product.nickname, avatar=product.avatar, id=product.id,
                                       toolset=tool_dto_list, description=product.description,
                                       openapi_desc=product.openapi_desc)
                res.append(plugin_dto)
        return res

    @staticmethod
    def create_plugin_with_openapi(plugin_dto: PluginDTO) -> str:
        """Create a new plugin with OpenAPI schema.

        Args:
            plugin_dto (PluginDTO): Plugin DTO.

        Returns:
            str: Plugin ID.
        """
        # single OpenAPI schema with multiple APIs is parsed into multiple tool bundles.
        validate_create_plugin_parameters(plugin_dto)
        tool_bundles = parse_openapi_yaml_to_tool_bundle(plugin_dto.openapi_desc)
        tool_id_list = []
        index = 1
        for tool in tool_bundles:
            tool_id = plugin_dto.id + '_tool_' + str(index)
            parameters = parse_tool_input(tool)
            tool_dto = ToolDTO(id=tool_id,
                               nickname=plugin_dto.nickname + '_tool_' + str(index) if plugin_dto.nickname else '',
                               avatar=plugin_dto.avatar if plugin_dto.avatar else None,
                               parameters=parameters,
                               openapi_schema=tool
                               )
            ToolService().create_tool(tool_dto)
            tool_id_list.append(tool_id)
            index += 1
        # assemble product config data
        product_config_data = assemble_plugin_product_config_data(plugin_dto, tool_id_list)
        # write product YAML file
        product_file_name = f"{plugin_dto.id}_product"
        path = get_core_path()
        product_file_path = path / 'product' / 'plugin' / f"{product_file_name}.yaml" if path\
            else os.path.join('..', '..', 'platform', 'difizen', 'product', 'plugin', f"{product_file_name}.yaml")
        write_yaml_file(str(product_file_path), product_config_data)
        register_product(str(product_file_path))
        return plugin_dto.id
