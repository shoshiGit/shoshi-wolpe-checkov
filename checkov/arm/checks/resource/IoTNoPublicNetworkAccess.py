from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.arm.base_resource_value_check import BaseResourceValueCheck


class IoTNoPublicNetworkAccess(BaseResourceValueCheck):
    def __init__(self):
        name = "Ensure that Azure IoT Hub disables public network access"
        id = "CKV_AZURE_108"
        supported_resources = ['Microsoft.Devices/IotHubs']
        categories = [CheckCategories.NETWORKING]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources,
                         missing_block_result=CheckResult.PASSED)

    def get_inspected_key(self) -> str:
        return 'properties/publicNetworkAccess'

    def get_expected_value(self) -> str:
        return "Disabled"


check = IoTNoPublicNetworkAccess()
