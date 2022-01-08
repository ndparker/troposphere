# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import boolean, integer
from .validators.elasticsearch import (
    policytypes,
    validate_automated_snapshot_start_hour,
    validate_ebs_options,
    validate_tags_or_list,
    validate_tls_security_policy,
    validate_volume_type,
)


class MasterUserOptions(AWSProperty):
    """
    `MasterUserOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-masteruseroptions.html>`__
    """

    props: PropsDictType = {
        "MasterUserARN": (str, False),
        "MasterUserName": (str, False),
        "MasterUserPassword": (str, False),
    }


class AdvancedSecurityOptionsInput(AWSProperty):
    """
    `AdvancedSecurityOptionsInput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-advancedsecurityoptionsinput.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, False),
        "InternalUserDatabaseEnabled": (boolean, False),
        "MasterUserOptions": (MasterUserOptions, False),
    }


class CognitoOptions(AWSProperty):
    """
    `CognitoOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-cognitooptions.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, False),
        "IdentityPoolId": (str, False),
        "RoleArn": (str, False),
        "UserPoolId": (str, False),
    }


class DomainEndpointOptions(AWSProperty):
    """
    `DomainEndpointOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-domainendpointoptions.html>`__
    """

    props: PropsDictType = {
        "CustomEndpoint": (str, False),
        "CustomEndpointCertificateArn": (str, False),
        "CustomEndpointEnabled": (boolean, False),
        "EnforceHTTPS": (boolean, False),
        "TLSSecurityPolicy": (validate_tls_security_policy, False),
    }


class EBSOptions(AWSProperty):
    """
    `EBSOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-ebsoptions.html>`__
    """

    props: PropsDictType = {
        "EBSEnabled": (boolean, False),
        "Iops": (integer, False),
        "VolumeSize": (integer, False),
        "VolumeType": (validate_volume_type, False),
    }

    def validate(self):
        validate_ebs_options(self)


class ColdStorageOptions(AWSProperty):
    """
    `ColdStorageOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-coldstorageoptions.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, False),
    }


class ZoneAwarenessConfig(AWSProperty):
    """
    `ZoneAwarenessConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-zoneawarenessconfig.html>`__
    """

    props: PropsDictType = {
        "AvailabilityZoneCount": (integer, False),
    }


class ElasticsearchClusterConfig(AWSProperty):
    """
    `ElasticsearchClusterConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-elasticsearchclusterconfig.html>`__
    """

    props: PropsDictType = {
        "ColdStorageOptions": (ColdStorageOptions, False),
        "DedicatedMasterCount": (integer, False),
        "DedicatedMasterEnabled": (boolean, False),
        "DedicatedMasterType": (str, False),
        "InstanceCount": (integer, False),
        "InstanceType": (str, False),
        "WarmCount": (integer, False),
        "WarmEnabled": (boolean, False),
        "WarmType": (str, False),
        "ZoneAwarenessConfig": (ZoneAwarenessConfig, False),
        "ZoneAwarenessEnabled": (boolean, False),
    }


class EncryptionAtRestOptions(AWSProperty):
    """
    `EncryptionAtRestOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-encryptionatrestoptions.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, False),
        "KmsKeyId": (str, False),
    }


class LogPublishingOption(AWSProperty):
    """
    `LogPublishingOption <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-logpublishingoption.html>`__
    """

    props: PropsDictType = {
        "CloudWatchLogsLogGroupArn": (str, False),
        "Enabled": (boolean, False),
    }


class NodeToNodeEncryptionOptions(AWSProperty):
    """
    `NodeToNodeEncryptionOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-nodetonodeencryptionoptions.html>`__
    """

    props: PropsDictType = {
        "Enabled": (boolean, False),
    }


class SnapshotOptions(AWSProperty):
    """
    `SnapshotOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-snapshotoptions.html>`__
    """

    props: PropsDictType = {
        "AutomatedSnapshotStartHour": (validate_automated_snapshot_start_hour, False),
    }


class VPCOptions(AWSProperty):
    """
    `VPCOptions <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-vpcoptions.html>`__
    """

    props: PropsDictType = {
        "SecurityGroupIds": ([str], False),
        "SubnetIds": ([str], False),
    }


class Domain(AWSObject):
    """
    `Domain <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html>`__
    """

    resource_type = "AWS::Elasticsearch::Domain"

    props: PropsDictType = {
        "AccessPolicies": (policytypes, False),
        "AdvancedOptions": (dict, False),
        "AdvancedSecurityOptions": (AdvancedSecurityOptionsInput, False),
        "CognitoOptions": (CognitoOptions, False),
        "DomainEndpointOptions": (DomainEndpointOptions, False),
        "DomainName": (str, False),
        "EBSOptions": (EBSOptions, False),
        "ElasticsearchClusterConfig": (ElasticsearchClusterConfig, False),
        "ElasticsearchVersion": (str, False),
        "EncryptionAtRestOptions": (EncryptionAtRestOptions, False),
        "LogPublishingOptions": (dict, False),
        "NodeToNodeEncryptionOptions": (NodeToNodeEncryptionOptions, False),
        "SnapshotOptions": (SnapshotOptions, False),
        "Tags": (validate_tags_or_list, False),
        "VPCOptions": (VPCOptions, False),
    }
