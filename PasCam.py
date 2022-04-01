# Project PasCam 7 by Alex Arbuckle #


# import <
from random import choice
from json import load, dump
from discord import Intents
from string import printable
from os import path, listdir
from discord.ext import commands

# >


# global <
realpath = path.realpath(__file__).split('/')
directory = '/'.join(realpath[:(len(realpath) - 1)])
PasCam = commands.Bot(command_prefix = '', intents = Intents.all())
token = ''

# >


def jsonLoad(file: str):
    '''  '''

    # get file <
    # get data <
    with open(f'{directory}{file}', 'r') as fin:

        return load(fin)

    # >


def jsonDump(file: str, data: dict):
    '''  '''

    # set file <
    # set data <
    with open(f'{directory}{file}', 'w') as fout:

        dump(data, fout, indent = 3)

    # >


@PasCam.command(aliases = jsonLoad(file = '/setting.json')['alias']['show'])
async def showCommand(ctx):
    '''  '''

    # create output <
    # send to user <
    out = '\n'.join(str(i)[:-4] for i in listdir(f'{directory}/{str(ctx.author)[:-5]}'))
    await ctx.author.send(out, delete_after = 180)

    # >


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

# >

