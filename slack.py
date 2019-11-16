from requests_oauthlib import OAuth1Session
import os
import json
import dotenv
import urllib.request

__all__ = ["SlackDealer"]

class SlackDealer:
    """
    スラックを効率よく扱うクラス
    """

    def __init__( self ):
        """
        各情報を初期化する
        """
        dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
        dotenv.load_dotenv(dotenv_path)
        self.OAuthAccessToken = os.environ.get("OAuthAccessToken")
        self.username = os.environ.get("username")
        self.channel_id = os.environ.get("channel_id")
        self.post_status = int( os.environ.get("post_status") )


    def post( self , message ):
        url = 'https://slack.com/api/chat.postMessage'
        params = {
            'token': self.OAuthAccessToken, # token
            'channel': self.channel_id, # channel ID
            'text': message, # text
            'username': self.username,
        }
        request = urllib.request.Request( url )
        request.add_header( 'Content-Type', 'application/x-www-form-urlencoded' )
        params = urllib.parse.urlencode( params ).encode( "utf-8" )

        with urllib.request.urlopen( request, params ) as res:
            data = res.read().decode( "utf-8" )  #投稿
            if self.post_status == 1: print( data )


        return message
