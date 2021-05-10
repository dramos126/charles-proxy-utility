
class Control_URL:
    
    baseURL = "http://control.charles/"
    start_recording = baseURL + "recording/start"
    stop_recording = baseURL + "recording/stop"
    download_session = baseURL + "session/download"
    export_json = baseURL + "session/export-json"
    export_har = baseURL + "session/export-har"
    clear_session = baseURL + "session/clear"
    actiave_throttle_speed = baseURL + "thottiling/activate?preset="
    deactivate_throttle = baseURL + "throttling/deactivate"
    