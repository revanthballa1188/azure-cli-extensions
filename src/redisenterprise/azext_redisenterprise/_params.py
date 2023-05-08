# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: disable=too-many-lines
# pylint: disable=too-many-statements
from azure.cli.core.commands.validators import (
    get_default_location_from_resource_group,
    validate_file_or_dict
)
from azure.cli.core.commands.parameters import (
    tags_type,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)
import argparse
from collections import defaultdict
from knack.util import CLIError

def load_arguments(self, _):

    with self.argument_context('redisenterprise operation-status show') as c:
        c.argument('location', arg_type=get_location_type(self.cli_ctx), id_part='name')
        c.argument('operation_id', type=str, help='The operation\'s unique identifier.', id_part='child_name_1')

    with self.argument_context('redisenterprise list') as c:
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('redisenterprise show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cluster_name', options_list=['--cluster-name', '--name', '-n'], type=str, help='The name of the '
                   'RedisEnterprise cluster.', id_part='name')

    with self.argument_context('redisenterprise create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cluster_name', options_list=['--cluster-name', '--name', '-n'], type=str, help='The name of the '
                   'RedisEnterprise cluster.')
        c.argument('tags', tags_type)
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('sku', arg_type=get_enum_type(['Enterprise_E10', 'Enterprise_E20', 'Enterprise_E50',
                                                  'Enterprise_E100', 'EnterpriseFlash_F300', 'EnterpriseFlash_F700',
                                                  'EnterpriseFlash_F1500']), help='The type of RedisEnterprise cluster '
                   'to deploy. Possible values: (Enterprise_E10, EnterpriseFlash_F300 etc.)')
        c.argument('capacity', type=int, help='The size of the RedisEnterprise cluster. Defaults to 2 or 3 depending '
                   'on SKU. Valid values are (2, 4, 6, ...) for Enterprise SKUs and (3, 9, 15, ...) for Flash SKUs.')
        c.argument('zones', options_list=['--zones', '-z'], nargs='+', help='The Availability Zones where this cluster '
                   'will be deployed.')
        c.argument('minimum_tls_version', arg_type=get_enum_type(['1.0', '1.1', '1.2']), help='The minimum TLS version '
                   'for the cluster to support, e.g. \'1.2\'')
        c.argument('key_encryption_key_url', options_list=['--key-encryption-key-url'], 
                   type=str, help='Key encryption key Url, versioned only.' 
                   'Ex: https://contosovault.vault.azure.net/keys/contosokek/562a4bb76b524a1493a6afe8e536ee78'
                   ,arg_group='Encryption')
        c.argument('identity_type', options_list=['--identity-type'], 
                   arg_type=get_enum_type(['None', 'SystemAssigned', 'UserAssigned', 'SystemAssigned, UserAssigned']),
                   help='Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).'
                   ,arg_group='Identity')
        c.argument('key_encryption_identity_type', options_list=['--key-encryption-identity-type'], 
                   arg_type=get_enum_type(['systemAssignedIdentity', 'userAssignedIdentity']), 
                   help='Only userAssignedIdentity is supported in this API version; other types may be supported in the future.'
                   ,arg_group='KeyEncryptionKeyIdentity')
        c.argument('user_assigned_identity_resource_id', options_list=['--user-assigned-identity-resource-id'], 
                   type=str , help='User assigned identity to use for accessing key encryption key Url. '
                   'Ex: /subscriptions/<sub uuid>/resourceGroups/<resource group>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myId.'
                   ,arg_group='KeyEncryptionKeyIdentity')
        c.argument('user_assigned_identities', options_list=['--user-assigned-identities'], 
                   type=validate_file_or_dict, help='The set of user assigned identities associated with the resource. '
                   'The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '
                   '\'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. '
                   'The dictionary values can be empty objects ({}) in requests'
                   , arg_group='Identity')

        # Add database create arguments
        c.argument('client_protocol', arg_type=get_enum_type(['Encrypted', 'Plaintext']), help='Specifies whether redis clients '
                   'can connect using TLS-encrypted or plaintext redis protocols. Default is TLS-encrypted.')
        c.argument('port', type=int, help='TCP port of the database endpoint. Specified at create time. Defaults to an '
                   'available port.')
        c.argument('clustering_policy', arg_type=get_enum_type(['EnterpriseCluster', 'OSSCluster']), help='Clustering policy - default '
                   'is OSSCluster. Specified at create time.')
        c.argument('eviction_policy', arg_type=get_enum_type(['AllKeysLFU', 'AllKeysLRU', 'AllKeysRandom',
                                                              'VolatileLRU', 'VolatileLFU', 'VolatileTTL',
                                                              'VolatileRandom', 'NoEviction']), help='Redis eviction policy - default '
                   'is VolatileLRU')
        c.argument('persistence', action=AddPersistence, nargs='+', help='Persistence settings')
        c.argument('modules', action=AddModules, nargs='+', options_list=['--modules', '--module'], help='Optional set of redis modules to enable in this '
                   'database - modules can only be added at creation time.')
        # Add new argument
        c.argument('no_database', action='store_true', help='Advanced. Do not automatically create a '
                   'default database. Warning: the cache will not be usable until you create a database.')
        c.argument('group_nickname', type=str, help='Name for the group of linked database resources', arg_group='Geo '
                   'Replication')
        c.argument('linked_databases', action=AddLinkedDatabases, nargs='+', help='List of database resources to link '
                   'with this database', arg_group='Geo Replication')

    with self.argument_context('redisenterprise update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cluster_name', options_list=['--cluster-name', '--name', '-n'], type=str, help='The name of the '
                   'RedisEnterprise cluster.', id_part='name')
        c.argument('sku', arg_type=get_enum_type(['Enterprise_E10', 'Enterprise_E20', 'Enterprise_E50',
                                                  'Enterprise_E100', 'EnterpriseFlash_F300', 'EnterpriseFlash_F700',
                                                  'EnterpriseFlash_F1500']), help='The type of RedisEnterprise cluster '
                   'to deploy. Possible values: (Enterprise_E10, EnterpriseFlash_F300 etc.)')
        c.argument('capacity', type=int, help='The size of the RedisEnterprise cluster. Defaults to 2 or 3 depending '
                   'on SKU. Valid values are (2, 4, 6, ...) for Enterprise SKUs and (3, 9, 15, ...) for Flash SKUs.')
        c.argument('tags', tags_type)
        c.argument('minimum_tls_version', arg_type=get_enum_type(['1.0', '1.1', '1.2']), help='The minimum TLS version '
                   'for the cluster to support, e.g. \'1.2\'')
        c.argument('key_encryption_key_url', options_list=['--key-encryption-key-url'], type=str,
                   help='Key encryption key Url, versioned only. '
                   'Ex: https://contosovault.vault.azure.net/keys/contosokek/562a4bb76b524a1493a6afe8e536ee78' 
                   , arg_group='Encryption')
        c.argument('identity_type', options_list=['--identity-type'],
                   arg_type=get_enum_type(['None', 'SystemAssigned', 'UserAssigned', 'SystemAssigned, UserAssigned']),
                   help='Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).' 
                   , arg_group='Identity')
        c.argument('key_encryption_identity_type', options_list=['--key-encryption-identity-type'],
                   arg_type=get_enum_type(['systemAssignedIdentity', 'userAssignedIdentity']),
                   help='Only userAssignedIdentity is supported in this API version; other types may be supported in the future.' 
                   , arg_group='KeyEncryptionKeyIdentity')
        c.argument('user_assigned_identity_resource_id', options_list=['--user-assigned-identity-resource-id'], type=str 
                  , help='User assigned identity to use for accessing key encryption key Url. '
                       'Ex: /subscriptions/<sub uuid>/resourceGroups/<resource group>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myId.' 
                   , arg_group='KeyEncryptionKeyIdentity')
        c.argument('user_assigned_identities', options_list=['--user-assigned-identities']
                   , type=validate_file_or_dict, help='The set of user assigned identities associated with the resource. '
                   'The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '
                   '\'/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. '
                   'The dictionary values can be empty objects ({}) in requests', arg_group='Identity')

    with self.argument_context('redisenterprise delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cluster_name', options_list=['--cluster-name', '--name', '-n'], type=str, help='The name of the '
                   'RedisEnterprise cluster.', id_part='name')

    with self.argument_context('redisenterprise wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cluster_name', options_list=['--cluster-name', '--name', '-n'], type=str, help='The name of the '
                   'RedisEnterprise cluster.', id_part='name')

    with self.argument_context('redisenterprise database list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cluster_name', options_list=['--cluster-name', '--name', '-n'], type=str, help='The name of the '
                   'RedisEnterprise cluster.')

    with self.argument_context('redisenterprise database show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cluster_name', options_list=['--cluster-name', '--name', '-n'], type=str, help='The name of the '
                   'RedisEnterprise cluster.', id_part='name')

    with self.argument_context('redisenterprise database create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cluster_name', options_list=['--cluster-name', '--name', '-n'], type=str, help='The name of the '
                   'RedisEnterprise cluster.')
        c.argument('client_protocol', arg_type=get_enum_type(['Encrypted', 'Plaintext']), help='Specifies whether '
                   'redis clients can connect using TLS-encrypted or plaintext redis protocols. Default is '
                   'TLS-encrypted.')
        c.argument('port', type=int, help='TCP port of the database endpoint. Specified at create time. Defaults to an '
                   'available port.')
        c.argument('clustering_policy', arg_type=get_enum_type(['EnterpriseCluster', 'OSSCluster']), help='Clustering '
                   'policy - default is OSSCluster. Specified at create time.')
        c.argument('eviction_policy', arg_type=get_enum_type(['AllKeysLFU', 'AllKeysLRU', 'AllKeysRandom',
                                                              'VolatileLRU', 'VolatileLFU', 'VolatileTTL',
                                                              'VolatileRandom', 'NoEviction']), help='Redis eviction '
                   'policy - default is VolatileLRU')
        c.argument('persistence', action=AddPersistence, nargs='+', help='Persistence settings', is_preview=True)
        c.argument('modules', action=AddModules, nargs='+', options_list=['--modules', '--module'], help='Optional set of redis modules to enable in this '
                   'database - modules can only be added at creation time.')
        c.argument('group_nickname', type=str, help='Name for the group of linked database resources', arg_group='Geo '
                   'Replication')
        c.argument('linked_databases', action=AddLinkedDatabases, nargs='+', help='List of database resources to link '
                   'with this database', arg_group='Geo Replication')

    with self.argument_context('redisenterprise database update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cluster_name', options_list=['--cluster-name', '--name', '-n'], type=str, help='The name of the '
                   'RedisEnterprise cluster.', id_part='name')
        c.argument('client_protocol', arg_type=get_enum_type(['Encrypted', 'Plaintext']), help='Specifies whether '
                   'redis clients can connect using TLS-encrypted or plaintext redis protocols. Default is '
                   'TLS-encrypted.')
        c.argument('eviction_policy', arg_type=get_enum_type(['AllKeysLFU', 'AllKeysLRU', 'AllKeysRandom',
                                                              'VolatileLRU', 'VolatileLFU', 'VolatileTTL',
                                                              'VolatileRandom', 'NoEviction']), help='Redis eviction '
                   'policy - default is VolatileLRU')
        c.argument('persistence', action=AddPersistence, nargs='+', help='Persistence settings', is_preview=True)
        c.argument('group_nickname', type=str, help='Name for the group of linked database resources', arg_group='Geo '
                   'Replication')
        c.argument('linked_databases', action=AddLinkedDatabases, nargs='+', help='List of database resources to link '
                   'with this database', arg_group='Geo Replication')
        # Update help
        c.argument('client_protocol', arg_type=get_enum_type(['Encrypted', 'Plaintext']), help='Specifies whether redis clients '
                   'can connect using TLS-encrypted or plaintext redis protocols.')
        c.argument('eviction_policy',arg_type=get_enum_type(['AllKeysLFU', 'AllKeysLRU', 'AllKeysRandom', 
                    'VolatileLRU', 'VolatileLFU', 'VolatileTTL', 'VolatileRandom', 'NoEviction']), help='Redis eviction policy.')

    with self.argument_context('redisenterprise database delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cluster_name', options_list=['--cluster-name', '--name', '-n'], type=str, help='The name of the '
                   'RedisEnterprise cluster.', id_part='name')

    with self.argument_context('redisenterprise database export') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cluster_name', options_list=['--cluster-name', '--name', '-n'], type=str, help='The name of the '
                   'RedisEnterprise cluster.', id_part='name')
        c.argument('sas_uri', type=str, help='SAS URI for the target directory to export to')

    with self.argument_context('redisenterprise database force-unlink') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cluster_name', options_list=['--cluster-name', '--name', '-n'], type=str, help='The name of the '
                   'RedisEnterprise cluster.', id_part='name')
        c.argument('unlink_ids', nargs='+', help='The resource IDs of the database resources to be unlinked.')

    with self.argument_context('redisenterprise database import') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cluster_name', options_list=['--cluster-name', '--name', '-n'], type=str, help='The name of the '
                   'RedisEnterprise cluster.', id_part='name')
        c.argument('sas_uris', nargs='+', help='SAS URIs for the target blobs to import from')

    with self.argument_context('redisenterprise database list-keys') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cluster_name', options_list=['--cluster-name', '--name', '-n'], type=str, help='The name of the '
                   'RedisEnterprise cluster.')

    with self.argument_context('redisenterprise database regenerate-key') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cluster_name', options_list=['--cluster-name', '--name', '-n'], type=str, help='The name of the '
                   'RedisEnterprise cluster.', id_part='name')
        c.argument('key_type', arg_type=get_enum_type(['Primary', 'Secondary']),
                   help='Which access key to regenerate.')

    with self.argument_context('redisenterprise database wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('cluster_name', options_list=['--cluster-name', '--name', '-n'], type=str, help='The name of the '
                   'RedisEnterprise cluster.', id_part='name')


class AddPersistence(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.persistence = action

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == 'aof-enabled':
                d['aof_enabled'] = bool(v[0])

            elif kl == 'rdb-enabled':
                d['rdb_enabled'] = bool(v[0])

            elif kl == 'aof-frequency':
                d['aof_frequency'] = v[0]

            elif kl == 'rdb-frequency':
                d['rdb_frequency'] = v[0]

            else:
                raise CLIError(
                    'Unsupported Key {} is provided for parameter persistence. All possible keys are: aof-enabled,'
                    ' rdb-enabled, aof-frequency, rdb-frequency'.format(k)
                )

        return d


class AddModules(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddModules, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == 'name':
                d['name'] = v[0]

            elif kl == 'args':
                d['args'] = v[0]

            else:
                raise CLIError(
                    'Unsupported Key {} is provided for parameter modules. All possible keys are: name, args'.format(k)
                )
        return d


class AddLinkedDatabases(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddLinkedDatabases, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == 'id':
                d['id'] = v[0]

            else:
                raise CLIError(
                    'Unsupported Key {} is provided for parameter linked-databases. All possible keys are: id'.format(k)
                )

        return d
