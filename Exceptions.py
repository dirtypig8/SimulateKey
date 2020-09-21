class OptionFieldUnfilled(Exception):
    def __init__(self, field):
        super().__init__("Field '{}' unfilled".format(field))


class FieldNotExist(Exception):
    def __init__(self, field):
        super().__init__("Filed '{}' not exist".format(field))


class ResponseTimeoutError(Exception):
    def __init__(self):
        super().__init__("Wait for response of device timeout")


class NoLicensePlateMatchError(Exception):
    def __init__(self, license_plate):
        super().__init__("No license plate match '{}' comparing progress".format(license_plate))


class UnknownResponseError(Exception):
    def __init__(self, received_response, expected_response):
        super().__init__("Expected response are '{}', but received '{}'".format(expected_response, received_response))


class CheckDeviceStatusFailedError(Exception):
    def __init__(self):
        super().__init__("Check device status failed.")


class ConfigFileNotExistError(Exception):
    def __init__(self):
        super().__init__("Config file not exist.")


class OptionNotExistError(Exception):
    def __init__(self, section, option):
        super().__init__("Required option, [{}][{}] not set.".format(section, option))


class CommandNotFoundError(Exception):
    pass


class PrintFailedError(Exception):
    def __init__(self):
        pass


class TryToSwitchPrinter(Exception):
    def __inti__(self):
        pass