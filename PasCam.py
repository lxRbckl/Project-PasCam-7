# Project PasCam 7 by Alex Arbuckle #


# import <
from os import path
from json import load
from discord import Intents
from discord.ext import commands

# >


# global <
realpath = path.realpath(__file__).split('/')
directory = '/'.join(realpath[:(len(realpath) - 1)])
token = ''
PasCam = commands.Bot(

    command_prefix = '',
    intents = Intents.all()

)

# >


def jsonLoad(file: str):
    '''  '''

    # get file <
    # get data <
    with open(f'{directory}{file}', 'r') as fin:

        return load(fin)

    # >


@PasCam.command(aliases = jsonLoad(file = '/setting.json')['alias']['show'])
async def showCommand(ctx):
    '''  '''

    pass


@PasCam.command(aliases = jsonLoad(file = '/setting.json')['alias']['encrypt'])
async def encryptCommand(ctx, file: str, *args):
    '''  '''

    pass


@PasCam.command(aliases = jsonLoad(file = '/setting.json')['alias']['decrypt'])
async def decryptCommand(ctx, file: str):
    '''  '''

    pass


@PasCam.command(aliases = jsonLoad(file = '/setting.json')['alias']['update'])
async def updateCommand(ctx, file: str, *args):
    '''  '''

    pass


@PasCam.command(aliases = jsonLoad(file = '/setting.json')['alias']['delete'])
async def deleteCommand(ctx, file: str):
    '''  '''

    pass


@PasCam.command(aliases = jsonLoad(file = '/setting.json')['alias']['share'])
async def shareCommand(ctx, file: str, user: str):
    '''  '''

    pass


# main <
if (__name__ == '__main__'):

    pass

    # print(realpath)
    # print(directory)
    # print(path.exists(f'{directory}/setting.json'))

# >

