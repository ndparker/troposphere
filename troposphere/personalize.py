# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import boolean


class DatasetImportJob(AWSProperty):
    """
    `DatasetImportJob <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-dataset-datasetimportjob.html>`__
    """

    props: PropsDictType = {
        "DataSource": (dict, False),
        "DatasetArn": (str, False),
        "DatasetImportJobArn": (str, False),
        "JobName": (str, False),
        "RoleArn": (str, False),
    }


class Dataset(AWSObject):
    """
    `Dataset <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-dataset.html>`__
    """

    resource_type = "AWS::Personalize::Dataset"

    props: PropsDictType = {
        "DatasetGroupArn": (str, True),
        "DatasetImportJob": (DatasetImportJob, False),
        "DatasetType": (str, True),
        "Name": (str, True),
        "SchemaArn": (str, True),
    }


class DatasetGroup(AWSObject):
    """
    `DatasetGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-datasetgroup.html>`__
    """

    resource_type = "AWS::Personalize::DatasetGroup"

    props: PropsDictType = {
        "Domain": (str, False),
        "KmsKeyArn": (str, False),
        "Name": (str, True),
        "RoleArn": (str, False),
    }


class Schema(AWSObject):
    """
    `Schema <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-schema.html>`__
    """

    resource_type = "AWS::Personalize::Schema"

    props: PropsDictType = {
        "Domain": (str, False),
        "Name": (str, True),
        "Schema": (str, True),
    }


class SolutionConfig(AWSProperty):
    """
    `SolutionConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-personalize-solution-solutionconfig.html>`__
    """

    props: PropsDictType = {
        "AlgorithmHyperParameters": (dict, False),
        "AutoMLConfig": (dict, False),
        "EventValueThreshold": (str, False),
        "FeatureTransformationParameters": (dict, False),
        "HpoConfig": (dict, False),
    }


class Solution(AWSObject):
    """
    `Solution <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-personalize-solution.html>`__
    """

    resource_type = "AWS::Personalize::Solution"

    props: PropsDictType = {
        "DatasetGroupArn": (str, True),
        "EventType": (str, False),
        "Name": (str, True),
        "PerformAutoML": (boolean, False),
        "PerformHPO": (boolean, False),
        "RecipeArn": (str, False),
        "SolutionConfig": (SolutionConfig, False),
    }