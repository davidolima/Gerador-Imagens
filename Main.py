from PIL import Image
import random, os
import pygame as pg

def limparTela ():
    screen.fill((255,255,255))
    pg.display.update()

def gerarRGBAleatorio():
    return (random.randrange(1,256),random.randrange(1,256),random.randrange(1,256))

def salvarImagem (diretorio, nome):
    pg.image.save(screen,f"{diretorio}/{nome}.png")

def mudarCor(imagem, cor1, cor2):
    pa = pg.PixelArray(imagem)
    pa.replace(cor1,cor2,0.5)
    return imagem

def mudarCor(imagem, novaCor):
    imagem.fill(novaCor[0:3] + (255,), None, pg.BLEND_RGB_MULT)
    return imagem

def gerarTartarugas(num):
    global cascoNum, olhoNum, peleNum, fundoNum, chaoNum
    limparTela()
    numeroDeImagens = 0

    for i in range(num):
        fundoNum = random.randrange(1,len([name for name in os.listdir('./Imagens/Camada1')])+1)
        chaoNum = random.randrange(1,len([name for name in os.listdir('./Imagens/Camada2')])+1)
        cascoNum = random.randrange(1,len([name for name in os.listdir('./Imagens/Camada3')])+1)
        peleNum = random.randrange(1,len([name for name in os.listdir('./Imagens/Camada5')])+1)
        olhoNum = random.randrange(1,len([name for name in os.listdir('./Imagens/Camada6')])+1)
        
        acessorioRostoNum = random.randrange(1,len([name for name in os.listdir("./Imagens/Camada7/Acessorio1/")])+1)
        acessorioCorpoNum = random.randrange(1,len([name for name in os.listdir("./Imagens/Camada7/Acessorio2/")])+1)
        acessorioPesNum = random.randrange(1,len([name for name in os.listdir("./Imagens/Camada7/Acessorio3/")])+1)         

        gerarTartarugaAleatoria(cascoNum,olhoNum,peleNum,fundoNum,chaoNum,acessorioRostoNum,acessorioCorpoNum,acessorioPesNum)
        
        pg.display.update()
        salvarImagem("Out", (cascoNum,olhoNum,peleNum,fundoNum,chaoNum))
        numeroDeImagens += 1

    print(numeroDeImagens, 'imagens criadas.')

def gerarTartarugaAleatoria(cascoNum, olhoNum, peleNum, fundoNum, chaoNum,acessorioRostoNum,acessorioCorpoNum,acessorioPesNum):
    global identidade
    #Carregar Imagens com o PIL
    fundoPIL = Image.open(f'./Imagens/Camada1/{fundoNum}.png').convert('RGBA')
    chaoPIL = Image.open(f'./Imagens/Camada2/{chaoNum}.png').convert('RGBA')
    cascoPIL = Image.open(f'./Imagens/Camada3/{cascoNum}.png').convert('RGBA')
    basePIL = Image.open('./Imagens/Camada4/BASE.png').convert('RGBA')
    pelePIL = Image.open(f'./Imagens/Camada5/{peleNum}.png').convert('RGBA')
    olhoPIL = Image.open(f'./Imagens/Camada6/{olhoNum}.png').convert('RGBA')

    acessorioRostoPIL = Image.open(f'./Imagens/Camada7/Acessorio1/{acessorioRostoNum}.png').convert('RGBA')
    acessorioCorpoPIL = Image.open(f'./Imagens/Camada7/Acessorio2/{acessorioCorpoNum}.png').convert('RGBA')
    acessorioPesPIL = Image.open(f'./Imagens/Camada7/Acessorio3/{acessorioPesNum}.png').convert('RGBA')

    #Converter as imagens para Surfaces do Pygame
    base = pg.image.fromstring(basePIL.tobytes(),basePIL.size,basePIL.mode)
    casco = pg.image.fromstring(cascoPIL.tobytes(),cascoPIL.size,cascoPIL.mode)
    olho = pg.image.fromstring(olhoPIL.tobytes(),olhoPIL.size,olhoPIL.mode)
    pele = pg.image.fromstring(pelePIL.tobytes(),pelePIL.size,pelePIL.mode)
    fundo = pg.image.fromstring(fundoPIL.tobytes(),fundoPIL.size,fundoPIL.mode)
    chao = pg.image.fromstring(chaoPIL.tobytes(),chaoPIL.size,chaoPIL.mode)

    acessorioRosto = pg.image.fromstring(acessorioRostoPIL.tobytes(),acessorioRostoPIL.size,acessorioRostoPIL.mode)
    acessorioCorpo = pg.image.fromstring(acessorioCorpoPIL.tobytes(),acessorioCorpoPIL.size,acessorioCorpoPIL.mode)
    acessorioPes = pg.image.fromstring(acessorioPesPIL.tobytes(),acessorioPesPIL.size,acessorioPesPIL.mode)


    #Mudar cor das imagens
    corFundo = gerarRGBAleatorio()
    corChao = gerarRGBAleatorio()

    corCasco = gerarRGBAleatorio()
    corPele = gerarRGBAleatorio()

    corAcessorioRosto =gerarRGBAleatorio()
    corAcessorioCorpo = gerarRGBAleatorio()
    corAcessorioPes = gerarRGBAleatorio()
    
    fundo = mudarCor(fundo, corFundo)
    chao = mudarCor(chao, corChao)

    casco = mudarCor(casco, corCasco)
    pele = mudarCor(pele, corPele)

    acessorioRosto = mudarCor(acessorioRosto, corAcessorioRosto)
    acessorioCorpo = mudarCor(acessorioCorpo, corAcessorioCorpo)
    acessorioPes = mudarCor(acessorioPes, corAcessorioPes)

    #          Background --> Foreground
    camadas = [fundo, chao, casco, base, pele, olho, acessorioRosto, acessorioCorpo, acessorioPes]

    for camada in camadas:
        camada = pg.transform.scale(camada, (tela_width,tela_heigth))
        screen.blit(camada, (0,0))

    #Gerar identidade
    identidade = str(cascoNum)+str(olhoNum)+str(peleNum)+str(fundoNum)+str(chaoNum)\
               + str(corAcessorioCorpo[0])+str(corAcessorioCorpo[1])+str(corAcessorioCorpo[2])\
               + str(corAcessorioPes[0])+str(corAcessorioPes[1])+str(corAcessorioPes[2])\
               + str(corAcessorioRosto[0])+str(corAcessorioRosto[1])+str(corAcessorioRosto[2])\
               + str(corCasco[0])+str(corCasco[1])+str(corCasco[2])\
               + str(corChao[0])+str(corChao[1])+str(corChao[2])\
               + str(corFundo[0])+str(corFundo[1])+str(corFundo[2])\
               + str(corPele[0])+str(corPele[1])+str(corPele[2])

    pg.display.update()



def Main ():
    global tela_heigth, tela_width, screen

    tela_width = 512
    tela_heigth = 512

    screen = pg.display.set_mode((tela_width, tela_heigth))
    pg.display.set_caption("Gerador de NFTs")
    pg.display.init()
    pg.init()
    limparTela()
    running = True

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            elif event.type == pg.KEYDOWN:
                if pg.key.name(event.key) == 'return':
                    fundoNum = random.randrange(1,len([name for name in os.listdir('./Imagens/Camada1')])+1)
                    chaoNum = random.randrange(1,len([name for name in os.listdir('./Imagens/Camada2')])+1)
                    cascoNum = random.randrange(1,len([name for name in os.listdir('./Imagens/Camada3')])+1)
                    peleNum = random.randrange(1,len([name for name in os.listdir('./Imagens/Camada5')])+1)
                    olhoNum = random.randrange(1,len([name for name in os.listdir('./Imagens/Camada6')])+1)
                    
                    acessorioRostoNum = random.randrange(1,len([name for name in os.listdir("./Imagens/Camada7/Acessorio1/")])+1)
                    acessorioCorpoNum = random.randrange(1,len([name for name in os.listdir("./Imagens/Camada7/Acessorio2/")])+1)
                    acessorioPesNum = random.randrange(1,len([name for name in os.listdir("./Imagens/Camada7/Acessorio3/")])+1)

                    
                    gerarTartarugaAleatoria(cascoNum,olhoNum,peleNum,fundoNum,chaoNum,acessorioRostoNum,acessorioCorpoNum,acessorioPesNum)

                elif pg.key.name(event.key) == 'backspace':
                    gerarTartarugas(int(input("Gerar quantas imagens?")))
                elif pg.key.name(event.key) == 's':
                    salvarImagem("Out", identidade)
                elif pg.key.name(event.key) == 'i':
                    print(f"Casco: {cascoNum}\nOlho: {olhoNum}\nPele: {peleNum}\nFundo: {fundoNum}\nChao: {chaoNum}\nAC Cabeça: {acessorioRostoNum}\nAC Pés: {acessorioPesNum}\nAC Corpo: {acessorioCorpoNum}\n")
Main()
