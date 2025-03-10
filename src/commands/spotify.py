from nextcord.ext.commands import Cog 
import nextcord
from nextcord import Spotify
from nextcord import slash_command, Interaction, Embed
from func.spotifyGet import getSpotifyUrl, getDisplayName, getFollowersCount, getPlaylists
from nextcord.ext import commands
from nextcord import *
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
    async def sp(self, ctx : Message):
        acc = ctx.author.activities
        for i in acc:
            if isinstance(i, Spotify):
                print(searchAlbum(i.album))
                embed = Embed(title = f"{ctx.author.name} 🎶", description=f"[{i.title}]({i.track_url}) Dinleniyor")
                embed.add_field(name='Sanatçı', value=i.artist, inline=True)
                embed.add_field(name='Albüm', value=i.album, inline=True)
                embed.set_thumbnail(url=i.album_cover_url)
                await ctx.channel.send(embed=embed)
def setup( client): client.add_cog( spotify( client ) )

