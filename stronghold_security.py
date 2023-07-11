from camera_capture import CameraCapture
from window_monitoring import WindowMonitoring

class StrongholdSecurity:
    def __init__(self) -> None:
        print('Inited')
        CameraCapture()
        WindowMonitoring()
