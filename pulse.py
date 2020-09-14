# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Sourced From Online Templates And Guides
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Thanks To: Google Search For This Template
# Modified: Pulse
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.Nadiesabenada'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

xbmc.executebuiltin('Container.SetViewMode(500)')

YOUTUBE_CHANNEL_ID_1 = "PLXrr3O2Jm9feW8ryd7gVRbfbm-M_t2mVz"
YOUTUBE_CHANNEL_ID_2 = "PL2aRcqjw-qSKYuDvL7NGnAgIOEHdcImjB"
YOUTUBE_CHANNEL_ID_3 = "PLXrr3O2Jm9ffQ8acCtJH_jYOyQO-HwVta"
YOUTUBE_CHANNEL_ID_4 = "PLXrr3O2Jm9fdjB4xgF998Kpomw986HrP-"
YOUTUBE_CHANNEL_ID_5 = "PLLk0qb2WLobXuu1ryIVuL0IePwv85xxT3"
YOUTUBE_CHANNEL_ID_6 = "PLMuFXpsA8v_ytmXR_brQMPvUjwt1CvOyz"
YOUTUBE_CHANNEL_ID_7 = "PLMuFXpsA8v_ynxx9rD4f57YpX7uiGfIJS"
YOUTUBE_CHANNEL_ID_8 = "PL-o37YO_uwcLeIm4xJZtTL7b7OXVpVh8x"
YOUTUBE_CHANNEL_ID_9 = "PLBF29177C5D2545EF"
YOUTUBE_CHANNEL_ID_10 = "PLMuFXpsA8v_yvx3DsfUA8e9KIqqYtPDIK"
                      
# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))
	
    plugintools.add_item( 
        #action="", 
        title="Nadie sabe nada Temporada 1",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://i.imgur.com/GMgZMnn.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Nadie sabe nada Temporada 2",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://i.imgur.com/GMgZMnn.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Nadie sabe nada Temporada 3",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://i.imgur.com/GMgZMnn.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Nadie sabe nada Temporada 4",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://i.imgur.com/GMgZMnn.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Nadie sabe nada Temporada 5",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://i.imgur.com/GMgZMnn.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Nadie sabe nada Temporada 6",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://i.imgur.com/GMgZMnn.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Nadie sabe nada Temporada 7",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://i.imgur.com/GMgZMnn.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Nadie sabe nada Temporada 8",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://i.imgur.com/GMgZMnn.jpg",
        folder=True )	
		
    plugintools.add_item( 
        #action="", 
        title="Chris Brown",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://i.imgur.com/zO6NNHV.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Michael Jackson",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://i.imgur.com/kuV3Crg.jpg",
        folder=True )
		
run()
