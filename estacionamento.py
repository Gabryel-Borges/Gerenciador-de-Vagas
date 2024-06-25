import cv2
import numpy as np

video = cv2.VideoCapture('video/estacionamento.mp4')
sucess, frame = video.read()

coord = [[8,26],[59,26],[110,26],[163,26],[209,26],[261,26],[306,26],[357,26],[409,26],[460,26],[506,26],[560,26],[2,232],[48,232],[95,232],[147,232],[193,232],[239,232],[291,232],[344,232],[392,232],[443,232],[497,232],[544,232],[592,232]] # ponto inicial do retângulo que demarca a vaga
width = 40
height = 85
qtWhite = 0

qtVagas = 0
statusVagas = [False]*25 # inicia todas as vagas com false (não ocupadas)

print(len(statusVagas))

while True:
    success, frame = video.read()
    frame = cv2.addWeighted(frame, 1.5, np.zeros(frame.shape, frame.dtype), 0, 0) # ajuste do luminosidade do vídeo (0.6 - 1.5)
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(frame_gray, 100, 200)

    intLuz = frame_gray.item(350, 632) # faz a leitura da cor desse pixel para ter um feedback de como está a intensidade da luz, e consequentemente pode fazer o melhor ajuste do parâmetro de classificação
    
    if intLuz < 135: # ajuste do parâmetro de classificação de acordo com a intensidade da luz
        intLuz = intLuz*0.1
    else:
        intLuz = 14


    i = 0
    qtVagas = 0

    for x,y in coord:
        for h in range(y, y+height):
            for w in range(x, x+width):
                cor = edges.item(h, w)

                if cor > 0:
                    qtWhite += 1

        qtWhite = round((qtWhite/(40*85))*100, 2)

        if qtWhite > intLuz: # verifica a quantidade de branco na imagem, para determinar se a vaga está ocupada ou não, observe que é levado em conta a intensidade da luz, pois a variação na intensidade luminosa reflete na mudança dos parâmetro certo para classificação
            if 560 <= x <= 600 and 26 <= y <= 111:
        
                if qtWhite > intLuz*1.5:
                    cv2.rectangle(frame, (x, y), (x+width, y+height), (0, 0, 255), 2)
                    statusVagas[i] = False
                else:
                    cv2.rectangle(frame, (x, y), (x+width, y+height), (0, 255, 0), 2)
                    statusVagas[i] = True
            else:
                cv2.rectangle(frame, (x, y), (x+width, y+height), (0, 0, 255), 2)
                statusVagas[i] = False
        else:
            cv2.rectangle(frame, (x,y), (x+width, y+height), (0, 255, 0), 2)
            statusVagas[i] = True

        
        i += 1



    for x in statusVagas:
        qtVagas += x
    
    
    cv2.putText(frame, str(25-qtVagas) + '/25', (450, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow('Video', frame)
    cv2.imshow('Bordas', edges)


    key = cv2.waitKey(50)

    if key == 27:
        break

cv2.destroyAllWindows()