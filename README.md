Esse projeto usa visão computacional para fazer o gerenciamento da situação de cada vaga de um estacionamento, para tal objetivo é usado a variação de cor para certificar que a vaga está ocupada ou não. Detalhadamente, o algoritmo fica constantemente fazendo a leitura de branco que está presente em cada vaga, assim que um automóvel entra na área demarcada da vaga o limiar de branco sobe indicando que a mesma foi ocupada. Além disso, foi utilizado um algoritmo de detecção de bordas, Canny, que permite desenhar um contorno branco envolta dos carros e deixar o fundo do vídeo preto, essa estratégia de detecção das bordas é bastante utilizada no campo da visão computacional, pois permite a suavização da imagem, redução de ruídos e outros benefícios. 