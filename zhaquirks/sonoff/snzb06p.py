from zigpy.profiles import zha
from zigpy.quirks import CustomDevice
from zigpy.zcl.clusters.general import (
    Basic,
    Identify,
    Ota,
)
from zigpy.zcl.clusters.measurement import OccupancySensing
from zigpy.zcl.clusters.security import IasZone
from zigpy.zcl.clusters.manufacturer_specific import ManufacturerSpecificCluster
from zhaquirks.const import (
    DEVICE_TYPE,
    ENDPOINTS,
    INPUT_CLUSTERS,
    MODELS_INFO,
    OUTPUT_CLUSTERS,
    PROFILE_ID,
)

SONOFF_CLUSTER_1_ID = 0xFC11
SONOFF_CLUSTER_2_ID = 0xFC57


class SonoffPresenceSenorSNZB06P(CustomDevice):
    """Sonoff human presence senor - model SNZB-06P"""

    signature = {
        # SimpleDescriptor(endpoint=1, profile=260, device_type=263
        # device_version=1
        # input_clusters=[0, 3, 1030, 1280, 64599, 64529]
        # output_clusters=[3, 25])
        MODELS_INFO: [
            ("SONOFF", "SNZB-06P"),
        ],
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.OCCUPANCY_SENSOR,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    OccupancySensing.cluster_id,
                    IasZone.cluster_id,
                    SONOFF_CLUSTER_1_ID,
                    SONOFF_CLUSTER_2_ID,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    Ota.cluster_id,
                ],
            },
        },
    }
    replacement = {
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.OCCUPANCY_SENSOR,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    OccupancySensing.cluster_id,
                    IasZone.cluster_id,
                    SONOFF_CLUSTER_1_ID,
                    SONOFF_CLUSTER_2_ID,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    Ota.cluster_id,
                ],
            },
        },
    }
