# Desafio PI

## Primeira etapa

Solucionei fazendo requisições à uma API e analisando os digitos de 1000 em 1000

## Segunda etapa

### Primeira estratégia

Baixei os arquivos de todos os numeros de pi, um a um e os analisei parcialmente, para isso usei a biblioteca em python do google (https://learndataanalysis.org/google-drive-api-in-python-getting-started-lesson-1/)

Abandonei essa estratégia pois os arquivos são muito grandes para baixar completamente (ja que aloca na RAM primeiro). Isso é necessário pois, como a extenção é .ycd, é necessário baixar todo o arquivo para depois descompactá-lo

### Segunda estratégia

Vou baixar txt por txt do primeiro trilhão de digitos do pi e fazer uma análise por chuncks dos arquivos (https://archive.org/download/pi_dec_1t)
