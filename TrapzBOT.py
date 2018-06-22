import discord
import asyncio
import random
import Token
import json
import os.path
import re

client = discord.Client()

AZUL =0x1abc9c
token = Token.seu_token()
msg_id = None
msg_user = None



@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):
#########################COMANDO GERAL#########################
    if message.content.lower().startswith('!moeda'):
        if message.author.id == '335932146986516481':
            choice = random.randint(1,2)
            if choice == 1:
                await client.add_reaction(message,'💩')
            if choice == 2:
                await client.add_reaction(message,'👽')
        else:
            await client.send_message(message.channel, 'Você não tem permissão')

    if message.content.lower().startswith('!r6'):

        embed = discord.Embed(
            title='Escolha seu cargo!',
            color=0x1abc9c,
            description='-Diamante = 💎\n'
                        '-Platina = 🔘\n'
                        '-Ouro = 📀\n'
                        '-Prata = 💿\n'
                        '-Bronze = 🛢 \n'
                        '-Cobre = 🔑',
        )
        botmsg = await client.send_message(message.channel,embed=embed)

        await client.add_reaction(botmsg, '💎')
        await client.add_reaction(botmsg, '🔘')
        await client.add_reaction(botmsg, '📀')
        await client.add_reaction(botmsg, '💿')
        await client.add_reaction(botmsg, '🛢')
        await client.add_reaction(botmsg, '🔑')

        global msg_id
        msg_id = botmsg.id

        global msg_user
        msg_user = message.author

    if message.content.startswith('!user'):
        await client.delete_message(message)
        try:
            user = message.mentions[0]
            userjoinedat = str(user.joined_at).split('.', 1)[0]
            usercreatedat = str(user.created_at).split('.', 1)[0]
            userbot = str(user.bot).split('.', 1)[0]

            userembed = discord.Embed(
                title="Nome:",
                description=user.name,
                color=0x1abc9c
            )
            userembed.set_author(
                name="User Info"
            )
            userembed.add_field(
                name="Membro desde:",
                value=userjoinedat
            )
            userembed.add_field(
                name="User ID:",
                value=user.id
            )
            userembed.add_field(
                name="User bot?",
                value=userbot
            )

            await client.send_message(message.channel, embed=userembed)
        except IndexError:
            await client.send_message(message.channel, "Defina o user ex !user @ex")
        except:
            await client.send_message(message.channel, "Desculpe houve um erro")
        finally:
            pass

    if message.content.lower().startswith('!prices'):
        await client.delete_message(message)
        embed = discord.Embed(
            title='💰**Prices**💰',
            color=0x1abc9c,
            description='**Prices list**                    BRL|USD\n'
                        '*MD10    to  diamond*  R$70|$19\n'
                        '*Platina to  diamond*    R$60|$16\n'
                        '*Gold    to  diamond*     R$80|$22\n'
                        '*Silver  to  diamond*      R$90|$24\n'
                        '*Bronze  to  diamond*   R$120|$32\n'
                        '*Copper  to  diamond*  R$150|$40\n'
        )
        embed.add_field(
            name="⚠AVISO⚠",
            value="O preço varia de acordo com os pontos que está ganhando por partida.",
            inline=False
        )
        embed.add_field(
            name="💰Pagamento💰",
            value="Pagamento via Mercado Pago ou GiftCard Steam. ",
            inline=False
        )

        embed.set_footer(
            text="Trapz™",
            icon_url="https://cdn.pixabay.com/photo/2017/05/16/21/24/gorilla-2318998_960_720.jpg"
        )
        embed.set_image(
            url="https://cdn.awsli.com.br/656/656248/arquivos/Trapz_Banner.jpg"
        )
        embed.set_author(
            name="R6BoosTrapz",
            icon_url="https://cdn.pixabay.com/photo/2017/05/16/21/24/gorilla-2318998_960_720.jpg",
            url="http://grewoss.com/"
        )
        await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('!pag'):
        await client.delete_message(message)
        embed = discord.Embed(
            title='💰**Pagamento**💰',
            color=0x1abc9c,
            description='Pagamento via Mercado Pago ou GiftCard Steam.\n'
        )

        await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('!nov'):
        await client.delete_message(message)
        embed = discord.Embed(
            title='🏷**Novidades**🏷',
            color=0x1abc9c,
            description=' Agora temos Boost de K/D sem risco de ban!\n'
        )

        await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('!help'):
        await client.delete_message(message)
        embed = discord.Embed(
            title='⚙**Bot Comands**⚙',
            color=0x1abc9c,
            description='!pag\n'
                        '!nov\n'
                        '!prices\n'
                        '!user @nome do usuario\n'
        )
        await client.send_message(message.channel, embed=embed)


################COMANDOS DE ADM################################
    if message.content.startswith('!cheat-on'):
        ids = ['386867442221056003', '411191673419333634', '409485469513023489', '380125797513691136', '383025608415772672', '434880079924035595', '389481957022629898', '335932146986516481']
                        # kibes                  #capri              #dropz              #Lmr.toiss          #randon1996             #rolyNoly           #Alo                    #st.dzk
        if not message.author.id in ids:
            return await client.send_message(message.channel, 'Você não tem permissão')
        await client.delete_message(message)
        aviso = discord.Embed(
            title='⚠AVISO CHEAT⚠',
            color=0x1abc9c,
            description='O cheat foi atualizado!'
        )
        await client.send_message(message.channel, embed=aviso)

    if message.content.startswith('!cheato-ff'):
        ids = ['386867442221056003', '411191673419333634', '409485469513023489', '380125797513691136', '383025608415772672', '434880079924035595', '389481957022629898', '335932146986516481']
                    # kibes                  #capri              #dropz              #Lmr.toiss          #randon1996             #rolyNoly           #Alo                    #st.dzk
        if not message.author.id in ids:
            return await client.send_message(message.channel, 'Você não tem permissão')
        await client.delete_message(message)
        aviso = discord.Embed(
            title='⚠AVISO CHEAT⚠',
            color=0x1abc9c,
            description='Cheat está sendo atualizado, parem de pergunta, assim que voltar voces serão avisados!'
        )
        await client.send_message(message.channel, embed=aviso)

    if message.content.startswith('!bost'):
        ids = ['386867442221056003', '411191673419333634', '409485469513023489', '380125797513691136','383025608415772672', '434880079924035595', '389481957022629898', '335932146986516481', '327491351723900948']
                    # kibes                  #capri              #dropz              #Lmr.toiss          #randon1996             #rolyNoly           #Alo                    #st.dzk                #trapz
        if not message.author.id in ids:
            return await client.send_message(message.channel, 'Você não tem permissão')
        await client.delete_message(message)
        aviso = discord.Embed(
            title='⚠AVISO⚠',
            color=0x1abc9c,
            description='GALERA,QUEM VAI BOOSTAR VOCÊS SÃO: O DIVINO E O RANDOM'
        )
        await client.send_message(message.channel, embed=aviso)

    if message.content.startswith('!feedback'):
        ids = ['386867442221056003', '411191673419333634', '409485469513023489','380125797513691136','383025608415772672','434880079924035595','389481957022629898','335932146986516481']
                    #kibes                  #capri              #dropz              #Lmr.toiss          #randon1996             #rolyNoly           #Alo                    #st.dzk
        if not message.author.id in ids:
            return await client.send_message(message.channel, 'Você não tem permissão')
        await client.delete_message(message)
        aviso = discord.Embed(
            title=':thumbup::skin-tone-2:Feedback:thumbdown::skin-tone-2:',
            color=0x1abc9c,
            description='Deixe sua recomendação do Boost no canal de feedback'
        )
        await client.send_message(message.channel, embed=aviso)

    if message.content.lower().startswith('!vote'):
        ids = ['386867442221056003', '411191673419333634', '409485469513023489', '380125797513691136', '383025608415772672', '434880079924035595', '389481957022629898', '335932146986516481']
                    # kibes                  #capri              #dropz              #Lmr.toiss          #randon1996             #rolyNoly           #Alo                    #st.dzk
        if not message.author.id in ids:
            return await client.send_message(message.channel, 'Você não tem permissão')
        await client.delete_message(message)
        vote = discord.Embed(
            title="Votação",
            color=0x1abc9c,
            description='O que vocês acham sobre:{} '.format(message.content[5:])
        )

        vote = await client.send_message(message.channel, embed=vote)
        await client.add_reaction(vote, "✅")
        await client.add_reaction(vote, "❎")

    if message.content.lower().startswith('!adm'):
        ids = ['386867442221056003', '411191673419333634', '409485469513023489', '380125797513691136', '383025608415772672', '434880079924035595', '389481957022629898', '335932146986516481','327491351723900948']
                    # kibes                  #capri              #dropz              #Lmr.toiss          #randon1996             #rolyNoly           #Alo                    #st.dzk                #trapz
        if not message.author.id in ids:
            return await client.send_message(message.channel, 'Você não tem permissão')
        await client.delete_message(message)
        embed = discord.Embed(
            title='⚙**Bot Comands ADM**⚙',
            color=0x1abc9c,
            description='!cheat-on\n'
                        '!cheat-off\n'
                        '!bost\n'
                        '!feedback\n'
                        '!clear x(x=numero de mensagens)\n'
                        '!vote\n'
                        '!say (mais mensagem que quer enviar)\n'
                        '!ban @user'
                        '!unban @user'
                        '!mute @user'
                        '!unmute @user'
        )
        await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('!clear'):
        ids = ['386867442221056003', '411191673419333634', '409485469513023489', '380125797513691136', '383025608415772672', '434880079924035595', '389481957022629898', '335932146986516481','327491351723900948']
                    # kibes                  #capri              #dropz              #Lmr.toiss          #randon1996             #rolyNoly           #Alo                    #st.dzk                #trapz
        if not message.author.id in ids:
            return await client.send_message(message.channel, 'Você não tem permissão')
        if not message.author.server_permissions.manage_messages:
            await client.send_message(message.channel, ":no_good:**Sem permissão!**")
        if message.author.server_permissions.manage_messages:
            try:
                lim = int(message.content[7:]) + 1
                await client.purge_from(message.channel, limit=lim)
                await client.send_message(message.channel, '{} mensagens foram deletadas com sucesso ,por {}'.format(lim,
                                                                                                             message.author.mention))
            finally:
                pass

    try:
        if message.content.lower().startswith('!say'):
            ids = ['386867442221056003', '411191673419333634', '409485469513023489', '380125797513691136', '383025608415772672', '434880079924035595', '389481957022629898', '335932146986516481','327491351723900948']
                        # kibes                  #capri              #dropz              #Lmr.toiss          #randon1996             #rolyNoly           #Alo                    #st.dzk                #trapz
            if not message.author.id in ids:
                return await client.send_message(message.channel, 'Você não tem permissão')
            await client.send_message(message.channel, '{}'.format(message.content[5:]))
            await client.delete_message(message)
    finally:
        pass


    if message.content.lower().startswith('!ban'):
        if message.content.lower().startswith('!say'):
            ids = ['386867442221056003', '411191673419333634', '409485469513023489', '380125797513691136', '383025608415772672', '434880079924035595', '389481957022629898', '335932146986516481','327491351723900948']
                        # kibes                  #capri              #dropz              #Lmr.toiss          #randon1996             #rolyNoly           #Alo                    #st.dzk                #trapz
            if not message.author.id in ids:
                return await client.send_message(message.channel, 'Você não tem permissão')
        if not message.author.server_permissions.ban_members:
            return await client.send_message(message.channel,"** Você precisa da permissão de banir membros!**")
        try:
            user = message.mentions[0]
            await client.send_message(message.channel, "**O usuario foi banido com sucesso do servidor.**")
            await client.ban(user, delete_message_days=7)
        except:
            await client.send_message(message.channel, "**Você deve especificar um usuario!**")
        finally:
            pass


    if message.content.lower().startswith('!unban'):
        if message.content.lower().startswith('!say'):
            ids = ['386867442221056003', '411191673419333634', '409485469513023489', '380125797513691136', '383025608415772672', '434880079924035595', '389481957022629898', '335932146986516481','327491351723900948']
                        # kibes                  #capri              #dropz              #Lmr.toiss          #randon1996             #rolyNoly           #Alo                    #st.dzk                #trapz
            if not message.author.id in ids:
                return await client.send_message(message.channel, 'Você não tem permissão')
        if not message.author.server_permissions.ban_members:
            return await client.send_message(message.channel, "** Você precisa da permissão de banir membros!**")
        try:
            uid = message.content[7:]
            user = await client.get_user_info(uid)
            await client.send_message(message.channel, "**O usuario foi desbanido com sucesso do servidor.**")
            return await client.unban(message.server, user)
        except:
            await client.send_message(message.channel, "**Você deve especificar um usuario!**")
        finally:
            pass


    if message.content.lower().startswith('!mute'):
        if message.content.lower().startswith('!say'):
            ids = ['386867442221056003', '411191673419333634', '409485469513023489', '380125797513691136', '383025608415772672', '434880079924035595', '389481957022629898', '335932146986516481','327491351723900948']
                        # kibes                  #capri              #dropz              #Lmr.toiss          #randon1996             #rolyNoly           #Alo                    #st.dzk                #trapz
            if not message.author.id in ids:
                return await client.send_message(message.channel, 'Você não tem permissão')
        if not message.author.server_permissions.manage_roles:
            return await client.send_message(message.channel, "** Você precisa da permissão de gerenciar cargos!**")
        try:
            user = message.mentions[0]
            await client.send_message(message.channel, "**O usuario <@{}> foi mutado com sucesso do servidor.**".format(user.id))
            role = discord.utils.find(lambda r: r.name == "Muted", message.server.roles)
            await client.add_roles(user, role)
        except:
            await client.send_message(message.channel, "**Você deve especificar um usuario!**")
        finally:
            pass


    if message.content.lower().startswith('!unmute'):
        if message.content.lower().startswith('!say'):
            ids = ['386867442221056003', '411191673419333634', '409485469513023489', '380125797513691136', '383025608415772672', '434880079924035595', '389481957022629898', '335932146986516481','327491351723900948']
                        # kibes                  #capri              #dropz              #Lmr.toiss          #randon1996             #rolyNoly           #Alo                    #st.dzk                #trapz
            if not message.author.id in ids:
                return await client.send_message(message.channel, 'Você não tem permissão')
        if not message.author.server_permissions.manage_roles:
            return await client.send_message(message.channel, "** Você precisa da permissão de gerenciar cargos!**")
        try:
            user = message.mentions[0]
            await client.send_message(message.channel, "**O usuario <@{}> foi desmutado com sucesso do servidor.**".format(user.id))
            role = discord.utils.find(lambda r: r.name == "Muted", message.server.roles)
            await client.remove_roles(user, role)
        except:
            await client.send_message(message.channel, "**Você deve especificar um usuario!**")
        finally:
            pass
##########################################################################


#########################reaction###################################
@client.event
async def on_reaction_add(reaction, user):
    msg= reaction.message

    if reaction.emoji == '🔑' and msg_id == msg_id:
     role = discord.utils.find(lambda r: r.name == 'cobre', msg.server.roles)
     await client.add_roles(user, role)

    if reaction.emoji == '💎' and msg_id == msg_id:
     role = discord.utils.find(lambda r: r.name == 'diamante', msg.server.roles)
     await client.add_roles(user, role)

    if reaction.emoji == '🔘' and msg_id == msg_id:
     role = discord.utils.find(lambda r: r.name == 'platina', msg.server.roles)
     await client.add_roles(user, role)

    if reaction.emoji == '📀' and msg_id == msg_id:
     role = discord.utils.find(lambda r: r.name == 'ouro', msg.server.roles)
     await client.add_roles(user, role)

    if reaction.emoji == '💿' and msg_id == msg_id:
     role = discord.utils.find(lambda r: r.name == 'prata', msg.server.roles)
     await client.add_roles(user, role)

    if reaction.emoji == '🛢' and msg_id == msg_id:
     role = discord.utils.find(lambda r: r.name == 'bronze', msg.server.roles)
     await client.add_roles(user, role)

@client.event
async def on_reaction_remove(reaction, user):
    msg = reaction.message

    if reaction.emoji == '🔑' and msg_id == msg_id:
        role = discord.utils.find(lambda r: r.name == 'cobre', msg.server.roles)
        await client.remove_roles(user, role)

    if reaction.emoji == '💎' and msg_id == msg_id:
        role = discord.utils.find(lambda r: r.name == 'diamante', msg.server.roles)
        await client.remove_roles(user, role)

    if reaction.emoji == '🔘' and msg_id == msg_id:
        role = discord.utils.find(lambda r: r.name == 'platina', msg.server.roles)
        await client.remove_roles(user, role)

    if reaction.emoji == '📀' and msg_id == msg_id:
        role = discord.utils.find(lambda r: r.name == 'ouro', msg.server.roles)
        await client.remove_roles(user, role)

    if reaction.emoji == '💿' and msg_id == msg_id:
        role = discord.utils.find(lambda r: r.name == 'prata', msg.server.roles)
        await client.remove_roles(user, role)

    if reaction.emoji == '🛢' and msg_id == msg_id:
        role = discord.utils.find(lambda r: r.name == 'bronze', msg.server.roles)
        await client.remove_roles(user, role)
####################################################################

###########member join/leave/ban####################################
@client.event
async def on_member_join(member):
    canal = client.get_channel('454768178329944094')
    pagamento = client.get_channel('454771241291874324')
    msg = 'Seja bem vindo {}!Entre no canal de {}'.format(member.mention, pagamento.mention)
    await client.send_message(canal, msg)

@client.event
async def on_member_remove(member):
    canal = client.get_channel('454768178329944094')
    msg2 = 'Tchau tchau {}'.format(member.mention)
    await client.send_message(canal, msg2)

@client.event
async def on_member_ban(member):
    canal = client.get_channel('454768178329944094')
    msg3 = 'o {} foi banido'.format(member.mention)
    await client.send_message(canal, msg3)
####################################################################










client.run(token)
