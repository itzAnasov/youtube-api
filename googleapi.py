import requests
import json


class GoogleApi:
    def __init(self, api_key):
        self.api_key = api_key

    def setVideoID(self, video_id):
        self.video_id = video_id

    def getVideoID(self):
        if hasattr(self, 'video_id') and self.video_id != None:
            return self.video_id
        else:
            return None
        
    def downloadVideo(self):
        vidID = self.getVideoID()
        if vidID != None:
# {"Accept": "application/json, text/plain, */*","Content-Type": "application/json"}
#self.data = """{"videoId": "tb8gHvYlCFs","params": "2AMBCgIQBg","playbackContext": {"contentPlaybackContext": {"html5Preference": "HTML5_PREF_WANTS"}},"contentCheckOk": true,"racyCheckOk": true,"context": {"client": {"hl": "en","gl": "US","clientName": "ANDROID","clientVersion": "18.06.35","userAgent": "com.google.android.youtube/18.06.35 (Linux; U; Android 10; US)","androidSdkVersion": 31}}}"""