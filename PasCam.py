# Project PasCam 7 by Alex Arbuckle #


# import <
from random import choice
from json import load, dump
from discord import Intents
from string import printable
from os import path, listdir, mkdir, remove

# >


# global <
backup = False
realpath = path.realpath(__file__).split('/')
directory = '/'.join(realpath[:(len(realpath) - 1)])
PasCam = commands.Bot(command_prefix = '', intents = Intents.all())
token = ''

# >


def jsonLoad(file: str):
    '''  '''

    # get file <
    # get data <
    with open(f'{directory}/{file}', 'r') as fin:

        return load(fin)

    # >


def jsonDump(file: str, data: dict):
    '''  '''

    # set file <
    # set data <
    with open(f'{directory}/{file}', 'w') as fout:

        dump(data, fout, indent = 3)

    # >


def encryptFunction(host: str, file: str, encr: str) -> None:
    '''  '''

    # local <
    char = printable[0:77] + printable[79:85] + printable[86:94]
    strList = [choice(char) for i in range(250000)]
    encrList = [sum([ord(i) for i in host])]

    # >

    # set index list <
    # set value from index <
    [encrList.append(encrList[-1] + ord(i)) for i in encr[:len(encr)]]
    [strList.insert(i, encr[c]) for c, i in enumerate(encrList[:len(encrList) - 1])]

    # >

    # set <
    jsonDump(file = f'{host}/{file}.json', data = strList)

    # >


def decryptFunction(host: str, file: str) -> str:
    '''  '''

    # local <
    decrList = [sum([ord(i) for i in host])]
    strList = jsonLoad(file=f'{host}/{file}.json')

    # >

    # get index list <
    # output str values from indices <
    [decrList.append(decrList[-1] + ord(strList[decrList[-1]])) for i in range(2000)]
    return ''.join([strList[i] for i in decrList])

    # >


async def sendFunction(ctx, content: str):
    '''  '''

    # if (backup) <
    # then (not backup) <
    if (backup is True): pass
    else: await ctx.author.send(f'`{content}`', delete_after = 60)

    # >


@PasCam.command(aliases = jsonLoad(file = 'setting.json')['alias']['encrypt'])
async def encryptCommand(ctx, file: str, *args, encr = None):
    '''  '''

    # if (new host) <
    if (str(ctx.author)[:-5] not in listdir(directory)):

        # set directory <
        # update <
        mkdir(f'{directory}/{str(ctx.author)[:-5]}')
        await encryptCommand(ctx, file, encr = args)

        # >

    # >

    # then (existing host) <
    else:

        # if (new file) <
        if (f'{file}.json' not in listdir(f'{directory}/{str(ctx.author)[:-5]}')):

            # format <
            encr = '::'.join(encr) if (encr) else '::'.join(args)
            encr += ';;' + str(ctx.author)[:-5] + ';;'

            # >

            encryptFunction(

                file = file,
                host = str(ctx.author)[:-5],
                encr = encr

            )

            await sendFunction(ctx, content = f'{file} was encrypted.')

        # >

        # then (existing file) <
        else: await sendFunction(ctx, content = f'{file} already exists.')

        # >

    # >


@PasCam.command(aliases = jsonLoad(file = 'setting.json')['alias']['decrypt'])
async def decryptCommand(ctx, file: str, host = None):
    '''  '''

    # if (existing file) <
    if (f'{file}.json' in listdir(f'{directory}/{str(ctx.author)[:-5]}')):

        decr = decryptFunction(

            file = file,
            host = host if (host) else str(ctx.author)[:-5]

        ).split(';;')

        # if (shared file) <
        if ('SHARE' in decr[0]):

            await decryptCommand(

                ctx,
                file = file,
                host = decr[0].split('::')[1]

            )

        # >

        # elif (has access) <
        elif (str(ctx.author)[:-5] in decr[1]):

            await sendFunction(

                ctx,
                content = decr[0].replace('::', '\n')

            )

        # >

        # then (no access) <
        else: await sendFunction(ctx, f'{file} does not exist.')

        # >

    # >

    # then (new file) <
    else: await sendFunction(ctx, f'{file} does not exist.')

    # >


@PasCam.command(aliases = jsonLoad(file = 'setting.json')['alias']['update'])
async def updateCommand(ctx, file: str, *args):
    '''  '''

    # if (existing file) <
    if (f'{file}.json' in listdir(f'{directory}/{str(ctx.author)[:-5]}')):

        decr = decryptFunction(

            file = file,
            host = str(ctx.author)[:-5]

        ).split(';;')

        encryptFunction(

            host = str(ctx.author)[:-5],
            file = file,
            encr = '::'.join(args) + ';;' + decr[1] + ';;'

        )

        # output <
        await sendFunction(ctx, f'{file} was updated')

        # >

    # >

    # then (new file) <
    else: await sendFunction(ctx, f'{file} does not exist.')

    # >


@PasCam.command(aliases = jsonLoad(file = 'setting.json')['alias']['delete'])
async def deleteCommand(ctx, file: str):
    '''  '''

    # if (existing file) <
    if (f'{file}.json' in listdir(f'{directory}/{str(ctx.author)[:-5]}')):

        # remove file <
        # output update <
        remove(f'{directory}/{str(ctx.author)[:-5]}/{file}.json')
        await ctx.author.send(f'`{file} was removed.`', delete_after = 60)

        # >

    # >

    # then (new file) <
    else: await ctx.author.send(f'`{file} does not exist.`', delete_after = 60)

    # >


@PasCam.command(aliases = jsonLoad(file = 'setting.json')['alias']['share'])
async def shareCommand(ctx, action: str, file: str, user: str):
    '''  '''

    pass


@PasCam.command(aliases = jsonLoad(file = 'setting.json')['alias']['show'])
async def showCommand(ctx):
    '''  '''

    pass


# main <
if (__name__ == '__main__'): PasCam.run(token)

# >