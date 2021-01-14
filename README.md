# Reaction Times

 Medidor de tempo de reação para o experimento bônus de F329.

## Como usar
Primeiro, configure o ambiente python 3 no seu computador

```
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```

Depois, edite a constante `MEASURES` do arquivo `reaction.py` para a quantidade de medidas que quer fazer.

### Tirando medições
1. Ao executar `python3 reaction.py`, o programa abrirá uma janela preta.
2. Pressione "s" para iniciar as medições
3. A cada medição a tela ficará branca por um tempo aleatório. Assim que ela ficar azul, aperte "s". Isso medirá seu tempo de reação.
4. Após as medições, os resultados ficarão salvos nos arquivos `reaction_times.json` e `reaction_times_raw.csv`.
