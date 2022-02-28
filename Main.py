from PIL import Image
import random, os
import pygame as pg

def gerarRGBAleatorio():
    return (random.randrange(1,256),random.randrange(1,256),random.randrange(1,256))

def salvarImagem (diretorio, nome):
    pg.image.save(screen,f"{diretorio}/{nome}.png")

def mudarCor(imagem, novaCor):
    imagem.fill(novaCor[0:3] + (255,), None, pg.BLEND_RGB_MULT)
    return imagem

def gerarImagens(num):
    global camada_4_num,camada_3_num, camada_6_num, camada_5_num, camada_1_num, camada_2_num
    numeroDeImagens = 0

    for i in range(num):
        screen.fill((255,255,255))
        camada_1_num = random.randrange(1,len([name for name in os.listdir('./Imagens/Camada1')])+1)
        camada_2_num = random.randrange(1,len([name for name in os.listdir('./Imagens/Camada2')])+1)
        camada_3_num = random.randrange(1,len([name for name in os.listdir('./Imagens/Camada3')])+1)
        camada_4_num = random.randrange(1,len([name for name in os.listdir('./Imagens/Camada4')])+1)
        camada_5_num = random.randrange(1,len([name for name in os.listdir('./Imagens/Camada5')])+1)
        camada_6_num = random.randrange(1,len([name for name in os.listdir('./Imagens/Camada6')])+1)
        
        camada_7_1_num = random.randrange(1,len([name for name in os.listdir("./Imagens/Camada7/Acessorio1/")])+1)
        camada_7_2_num = random.randrange(1,len([name for name in os.listdir("./Imagens/Camada7/Acessorio2/")])+1)
        camada_7_3_num = random.randrange(1,len([name for name in os.listdir("./Imagens/Camada7/Acessorio3/")])+1)         

        gerarImagemAleatoria(camada_1_num,camada_2_num,camada_3_num,camada_4_num,\
                             camada_5_num,camada_6_num,camada_7_1_num,camada_7_2_num,\
                             camada_7_3_num)
        
        pg.display.update()
        salvarImagem("Out", identidade)
        numeroDeImagens += 1

    print(numeroDeImagens, 'imagens criadas.')

def gerarImagemAleatoria(camada_1_num, camada_2_num, camada_3_num, camada_4_num, camada_5_num, camada_6_num,camada_7_1_num,camada_7_2_num,camada_7_3_num):
    global identidade

    screen.fill((255,255,255))

    #Carregar Imagens com o PIL
    camada_1_pil = Image.open(f'./Imagens/Camada1/{camada_1_num}.png').convert('RGBA')
    camada_2_pil = Image.open(f'./Imagens/Camada2/{camada_2_num}.png').convert('RGBA')
    camada_3_pil = Image.open(f'./Imagens/Camada3/{camada_3_num}.png').convert('RGBA')
    camada_4_pil = Image.open(f'./Imagens/Camada4/{camada_4_num}.png').convert('RGBA')
    camada_5_pil = Image.open(f'./Imagens/Camada5/{camada_5_num}.png').convert('RGBA')
    camada_6_pil = Image.open(f'./Imagens/Camada6/{camada_6_num}.png').convert('RGBA')

    camada_7_1_pil = Image.open(f'./Imagens/Camada7/Acessorio1/{camada_7_1_num}.png').convert('RGBA')
    camada_7_2_pil = Image.open(f'./Imagens/Camada7/Acessorio2/{camada_7_2_num}.png').convert('RGBA')
    camada_7_3_pil = Image.open(f'./Imagens/Camada7/Acessorio3/{camada_7_3_num}.png').convert('RGBA')

    #Converter as imagens para Surfaces do Pygame
    camada_1 = pg.image.fromstring(camada_1_pil.tobytes(),camada_1_pil.size,camada_1_pil.mode)
    camada_2 = pg.image.fromstring(camada_2_pil.tobytes(),camada_2_pil.size,camada_2_pil.mode)
    camada_3 = pg.image.fromstring(camada_3_pil.tobytes(),camada_3_pil.size,camada_3_pil.mode)
    camada_4 = pg.image.fromstring(camada_4_pil.tobytes(),camada_4_pil.size,camada_4_pil.mode)
    camada_5 = pg.image.fromstring(camada_5_pil.tobytes(),camada_5_pil.size,camada_5_pil.mode)
    camada_6 = pg.image.fromstring(camada_6_pil.tobytes(),camada_6_pil.size,camada_6_pil.mode)

    camada_7_1 = pg.image.fromstring(camada_7_1_pil.tobytes(),camada_7_1_pil.size,camada_7_1_pil.mode)
    camada_7_2 = pg.image.fromstring(camada_7_2_pil.tobytes(),camada_7_2_pil.size,camada_7_2_pil.mode)
    camada_7_3 = pg.image.fromstring(camada_7_3_pil.tobytes(),camada_7_3_pil.size,camada_7_3_pil.mode)

    #Mudar cor das imagens
    camada_1_cor = gerarRGBAleatorio()
    camada_2_cor = gerarRGBAleatorio()

    camada_3_cor = gerarRGBAleatorio()
    camada_5_cor = gerarRGBAleatorio()

    camada_7_1_cor =gerarRGBAleatorio()
    camada_7_2_cor = gerarRGBAleatorio()
    camada_7_3_cor = gerarRGBAleatorio()
    
    camada_1 = mudarCor(camada_1, camada_1_cor)
    camada_2 = mudarCor(camada_2, camada_2_cor)

    camada_3 = mudarCor(camada_3, camada_3_cor)
    camada_5 = mudarCor(camada_5, camada_5_cor)

    camada_7_1 = mudarCor(camada_7_1, camada_7_1_cor)
    camada_7_2 = mudarCor(camada_7_2, camada_7_2_cor)
    camada_7_3 = mudarCor(camada_7_3, camada_7_3_cor)

    #          Background                                   -->                                    Foreground
    camadas = [camada_1, camada_2, camada_3, camada_4, camada_5, camada_6, camada_7_1, camada_7_2, camada_7_3]

    for camada in camadas:
        camada = pg.transform.scale(camada, (tela_width,tela_heigth))
        screen.blit(camada, (0,0))

    #Gerar identidade
    identidade = str(camada_1_num)+str(camada_2_num)+str(camada_2_num)+str(camada_3_num)+str(camada_4_num)+str(camada_5_num) + str(camada_6_num)\
               + str(camada_7_2_cor[0])+str(camada_7_2_cor[1])+str(camada_7_2_cor[2])\
               + str(camada_7_3_cor[0])+str(camada_7_3_cor[1])+str(camada_7_3_cor[2])\
               + str(camada_7_1_cor[0])+str(camada_7_1_cor[1])+str(camada_7_1_cor[2])\
               + str(camada_3_cor[0])+str(camada_3_cor[1])+str(camada_3_cor[2])\
               + str(camada_2_cor[0])+str(camada_2_cor[1])+str(camada_2_cor[2])\
               + str(camada_1_cor[0])+str(camada_1_cor[1])+str(camada_1_cor[2])\
               + str(camada_5_cor[0])+str(camada_5_cor[1])+str(camada_5_cor[2])

    pg.display.update()

def Main ():
    global tela_heigth, tela_width, screen

    tela_width = 512
    tela_heigth = 512

    screen = pg.display.set_mode((tela_width, tela_heigth))
    pg.display.set_caption("Gerador de NFTs")
    pg.display.init()
    pg.init()
    screen.fill((255,255,255))
    running = True

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            elif event.type == pg.KEYDOWN:
                if pg.key.name(event.key) == 'return':
                    camada_1_num = random.randrange(1,len([name for name in os.listdir('./Imagens/Camada1')])+1)
                    camada_2_num = random.randrange(1,len([name for name in os.listdir('./Imagens/Camada2')])+1)
                    camada_3_num = random.randrange(1,len([name for name in os.listdir('./Imagens/Camada3')])+1)
                    camada_4_num = random.randrange(1,len([name for name in os.listdir('./Imagens/Camada4')])+1)
                    camada_5_num = random.randrange(1,len([name for name in os.listdir('./Imagens/Camada5')])+1)
                    camada_6_num = random.randrange(1,len([name for name in os.listdir('./Imagens/Camada6')])+1)
                    
                    camada_7_1_num = random.randrange(1,len([name for name in os.listdir("./Imagens/Camada7/Acessorio1/")])+1)
                    camada_7_2_num = random.randrange(1,len([name for name in os.listdir("./Imagens/Camada7/Acessorio2/")])+1)
                    camada_7_3_num = random.randrange(1,len([name for name in os.listdir("./Imagens/Camada7/Acessorio3/")])+1)

                    gerarImagemAleatoria(camada_1_num,camada_2_num,camada_3_num,camada_4_num,\
                                         camada_5_num,camada_6_num,camada_7_1_num,camada_7_2_num,\
                                         camada_7_3_num)

                elif pg.key.name(event.key) == 'backspace':
                    gerarImagens(int(input("Gerar quantas imagens?")))
                elif pg.key.name(event.key) == 's':
                    salvarImagem("Out", identidade)
                elif pg.key.name(event.key) == 'i':
                    print(f"\n----------------------\nID: {identidade}\nCamada 1: {camada_1_num}\nCamada 2: {camada_2_num}\nCamada 3: {camada_3_num}\nCamada 4: {camada_4_num}\nCamada 5: {camada_5_num}\nCamada 6: {camada_6_num}\nCamada 7 AC 1: {camada_7_1_num}\nCamada 7 AC 2: {camada_7_2_num}\nCamada 7 AC 3: {camada_7_3_num}\n")
Main()
