import json
from morphing_control.python_bridge.serial_comm import MorphingSerialBridge

# Example mapping: terrain type to actuator angles
MORPH_PATTERNS = {
    'road':    [90, 90, 90, 90],
    'sand':    [120, 120, 60, 60],
    'gravel':  [100, 80, 100, 80],
    'grass':   [110, 110, 70, 70],
    'flood':   [60, 60, 120, 120],
}

MISSION_MODES = ['normal', 'stealth', 'rescue']

class MorphLogic:
    def __init__(self, port='COM3'):
        self.bridge = MorphingSerialBridge(port=port)
    def decide_and_morph(self, terrain, mission_mode='normal'):
        pattern = MORPH_PATTERNS.get(terrain, [90, 90, 90, 90])
        # Optionally adjust pattern based on mission_mode
        if mission_mode == 'stealth':
            pattern = [min(180, a+10) for a in pattern]
        elif mission_mode == 'rescue':
            pattern = [max(0, a-10) for a in pattern]
        self.bridge.send_morph_command(pattern)
    def reset(self):
        self.bridge.reset()
    def close(self):
        self.bridge.close()

if __name__ == '__main__':
    logic = MorphLogic(port='COM3')
    try:
        logic.decide_and_morph('sand', 'rescue')
    finally:
        logic.close() 