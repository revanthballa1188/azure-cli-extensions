# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

# from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):  # pylint: disable=unused-argument
    with self.command_group("redisenterprise") as g:
        g.custom_command('create', 'redisenterprise_create', supports_no_wait=True)
        g.custom_command('list', 'redisenterprise_list')
        g.custom_show_command('show', 'redisenterprise_show')
