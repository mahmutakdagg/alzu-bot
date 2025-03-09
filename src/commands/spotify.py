from nextcord.ext.commands import Cog 
import nextcord
from nextcord import Spotify
from nextcord import slash_command, Interaction, Embed
from func.spotifyGet import getSpotifyUrl, getDisplayName, getFollowersCount, getPlaylists
from nextcord.ext import commands

class spotify( Cog ):
    def __init__( self, client ):
        self.client = client

    @slash_command( name = 'spotify', description = 'Girdiğiniz kişinin spotify profil fotoğrafını gösterir')
    async def spotify( self, interaction : Interaction, hesap):
        try:
            playlists = getPlaylists( hesap )
            Mesaj = Embed( title=f"{ getDisplayName( hesap ) } Adlı kişinin Spotify'ı")
            Mesaj.set_image( url = getSpotifyUrl( hesap ) )
            for playlist in playlists:
                Mesaj.add_field( name = playlist['name'], value = f"[Playlist'i aç]({ playlist[ 'external_urls' ][ 'spotify' ] })")
            await interaction.response.send_message( embed = Mesaj )
            
        except nextcord.errors.ApplicationInvokeError:

            ErrorEmbed  = Embed( title = f'Token geçerliliğini yitirdi ve yenilendi, komutu yeniden dene' )
            await interaction.response.send_message( embed = ErrorEmbed )

    @commands.command()
    async def one( self, ctx, hesap):
        playlists = getPlaylists(hesap)
        Mesaj = Embed(title=f"{hesap}'s playlists", description="Here are the playlists:")
    
        for playlist in playlists:
            Mesaj.add_field(name=playlist['name'], value=f"[Open in Spotify]({playlist['external_urls']['spotify']})", inline=False)



    @commands.command()
    async def sp(self, interaction : Interaction, kisi : nextcord.Member = None):
        if kisi is None:
            kisi == interaction.user
        acc = kisi.activities
        for i in acc:
            if isinstance(i, Spotify):
                embed = Embed(title = f"{interaction.user.name} 🎶")
                embed.add_field(name=i.title, value="dinliyor")
                embed.add_field(name='Sanatçı', value=i.artist, inline=False)
                embed.add_field(name='Albüm', value=i.album, inline=False)
                embed.set_image(url=i.album_cover_url)
def setup( client): client.add_cog( spotify( client ) )

