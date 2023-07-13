#!/usr/bin/python

import os
import xbmc
import xbmcaddon
import xbmcgui
from xbmcaddon import Addon

class OSDonPlayback(xbmc.Player):
    
    def __init__(self, *args, **kwargs):
        xbmc.Player.__init__(self)
        self.run = True

    def onAVStarted(self):            
        if self.isPlayingVideo():
            video = (xbmc.getInfoLabel("Player.Title()"))
            if Addon().getSettingBool("osdonplayback_enable"):                       
                if not xbmc.getCondVisibility("Player.ShowTime"):
                    xbmc.executebuiltin('Action(ShowTime)')
                    xbmc.log('----OSD-on-Playback: Displaying Video OSD for ('f'{video})', xbmc.LOGINFO)
                    while video == (xbmc.getInfoLabel("Player.Title()")) and not monitor.abortRequested():                  
                        if xbmcgui.getCurrentWindowId() == 12005:
                            if (int(xbmc.getInfoLabel("Player.Time(secs)"))) >= (Addon().getSettingInt("osdonplayback_seconds")):
                                xbmc.executebuiltin('Action(ShowTime)')
                                xbmc.log('----OSD-on-Playback: Closing Video OSD for ('f'{video})', xbmc.LOGINFO)
                                break
                        else:
                            while video == (xbmc.getInfoLabel("Player.Title()")) and not monitor.abortRequested():
                                if xbmcgui.getCurrentWindowId() == 12005:
                                    time = (int(xbmc.getInfoLabel("Player.Time(secs)")) + (Addon().getSettingInt("osdonplayback_seconds")))
                                    while video == (xbmc.getInfoLabel("Player.Title()")) and not monitor.abortRequested():
                                        if int(xbmc.getInfoLabel("Player.Time(secs)")) >= (int(time)):
                                            xbmc.executebuiltin('Action(ShowTime)')
                                            xbmc.log('----OSD-on-Playback: Closing Video OSD for ('f'{video})', xbmc.LOGINFO)
                                            break
                                else:
                                    continue
                                break
                    else:
                        xbmc.log("----'OSD'onPlayback: video has changed", xbmc.LOGINFO)
                        while not video == (xbmc.getInfoLabel("Player.Title()")) and not monitor.abortRequested():                      
                            if xbmcgui.getCurrentWindowId() == 12005:
                                if (int(xbmc.getInfoLabel("Player.Time(secs)"))) >= (Addon().getSettingInt("osdonplayback_seconds")):
                                    xbmc.executebuiltin('Action(ShowTime)')
                                    xbmc.log('----OSD-on-Playback: Closing Video OSD for ('f'{video})', xbmc.LOGINFO)
                                    break
                else:
                    while video == (xbmc.getInfoLabel("Player.Title()")) and not monitor.abortRequested():                  
                        if xbmcgui.getCurrentWindowId() == 12005:
                            if (int(xbmc.getInfoLabel("Player.Time(secs)"))) >= (Addon().getSettingInt("osdonplayback_seconds")):
                                xbmc.executebuiltin('Action(ShowTime)')
                                xbmc.log('----OSD-on-Playback: Closing Video OSD for ('f'{video})', xbmc.LOGINFO)
                                break
                    else:
                        xbmc.log("----'OSD'onPlayback: video has changed", xbmc.LOGINFO)
                        while not video == (xbmc.getInfoLabel("Player.Title()")) and not monitor.abortRequested():                      
                            if xbmcgui.getCurrentWindowId() == 12005:
                                if (int(xbmc.getInfoLabel("Player.Time(secs)"))) >= (Addon().getSettingInt("osdonplayback_seconds")):
                                    xbmc.executebuiltin('Action(ShowTime)')
                                    xbmc.log('----OSD-on-Playback: Closing Video OSD for ('f'{video})', xbmc.LOGINFO)
                                    break
        try:
            monitor.waitForAbort(3)
        except:
            pass
            
monitor = xbmc.Monitor()
class OSDonPlayback:
    player = OSDonPlayback()
    while not monitor.abortRequested():
        monitor.waitForAbort(1)
    del player         