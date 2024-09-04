from typing import Dict, List
from .basemodel import ( GenvexNabtoBaseModel, GenvexNabtoDatapointKey, GenvexNabtoDatapoint, GenvexNabtoSetpointKey, GenvexNabtoSetpoint )

class GenvexNabtoCTS602Light(GenvexNabtoBaseModel):
    def __init__(self):
        super().__init__()

        self._datapoints = {
            GenvexNabtoDatapointKey.TEMP_SUPPLY: GenvexNabtoDatapoint(obj=0, address=37, divider=100, offset=0),
            GenvexNabtoDatapointKey.TEMP_OUTSIDE: GenvexNabtoDatapoint(obj=0, address=38, divider=100, offset=0),
            GenvexNabtoDatapointKey.TEMP_EXHAUST: GenvexNabtoDatapoint(obj=0, address=33, divider=100, offset=0),
            GenvexNabtoDatapointKey.TEMP_EXTRACT: GenvexNabtoDatapoint(obj=0, address=34, divider=100, offset=0),
            GenvexNabtoDatapointKey.HUMIDITY: GenvexNabtoDatapoint(obj=0, address=51, divider=100, offset=0),
            GenvexNabtoDatapointKey.FAN_DUTYCYCLE_SUPPLY: GenvexNabtoDatapoint(obj=0, address=98, divider=1, offset=0),
            GenvexNabtoDatapointKey.FAN_DUTYCYCLE_EXTRACT: GenvexNabtoDatapoint(obj=0, address=99, divider=1, offset=0),
            GenvexNabtoDatapointKey.BYPASS_ACTIVE: GenvexNabtoDatapoint(obj=0, address=129, divider=1, offset=0),
            GenvexNabtoDatapointKey.FILTER_REPLACE_TIME_REMAIN: GenvexNabtoDatapoint(obj=0, address=101, divider=1, offset=0),
        }

        self._setpoints = {
            GenvexNabtoSetpointKey.FAN_LEVEL: GenvexNabtoSetpoint(read_obj=0, read_address=135, write_obj=0, write_address=135, divider=1, offset=0, min=0, max=4),
            GenvexNabtoSetpointKey.TEMP_TARGET: GenvexNabtoSetpoint(read_obj=0, read_address=136, write_obj=0, write_address=136, divider=100, offset=0, min=0, max=3000, step=0.5),
            GenvexNabtoSetpointKey.FILTER_REPLACE_RESET: GenvexNabtoSetpoint(read_obj=0, read_address=67, write_obj=0, write_address=67, divider=1, offset=0, min=0, max=1),            
            GenvexNabtoSetpointKey.FILTER_REPLACE_INTERVAL: GenvexNabtoSetpoint(read_obj=0, read_address=153, write_obj=0, write_address=153, divider=1, offset=0, min=0, max=365, step=1)
        }

        self._defaultDatapointRequest = [
            GenvexNabtoDatapointKey.TEMP_SUPPLY,
            GenvexNabtoDatapointKey.TEMP_OUTSIDE,
            GenvexNabtoDatapointKey.TEMP_EXHAUST,
            GenvexNabtoDatapointKey.TEMP_EXTRACT,
            GenvexNabtoDatapointKey.HUMIDITY,
            GenvexNabtoDatapointKey.FAN_DUTYCYCLE_SUPPLY,
            GenvexNabtoDatapointKey.FAN_DUTYCYCLE_EXTRACT,
            GenvexNabtoDatapointKey.BYPASS_ACTIVE,
            GenvexNabtoDatapointKey.FILTER_REPLACE_TIME_REMAIN
        ]

        self._defaultSetpointRequest = [
            GenvexNabtoSetpointKey.FAN_LEVEL,
            GenvexNabtoSetpointKey.TEMP_TARGET,
            GenvexNabtoSetpointKey.FILTER_REPLACE_INTERVAL
        ]
        
        self.setDefaultConfigs()
        

    def getModelName(self):
        return "CTS 602light"
    
    def getManufacturer(self):
        return "Nilan"