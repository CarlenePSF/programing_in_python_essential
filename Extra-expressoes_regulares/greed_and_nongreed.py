"""
Quantificadores greed e non-greed (lazy)

-- Quantificadores gulosos (greed)
  - *
  - +
-- Quantificadores não gulosos
  - ? -- Usando a interrogação para interromper uma busca cada vez que ela for completa pelo padrão que escrevemos nossa
      RegEx. Retornando o mínimo de informação possível pela checagem da expressão regular.



"""
import re

# Na string abaixo queremos pegar cada uma das tags em html escrevendo uma expressão regular para essa tarefa

texto = '''<p>Eita</p> <p>Qualquer frase</p> <p>Frase 3</p> <div> </div>'''

# A escrita abaixo embora pegue toda a string não divide as tags como desejado
# Note que escrevemos como queremos que inicie a busca com a <. Depois incluímos um range de caracteres específicos
# [pdiv] que não precisariam estar em ordem necessariamente. Especificamos quantas vezes queremos que a busca pelo
# range ocorra com {1,3} e assim fechamos com >. Para incluir o que está dentro da tag indicamos tudo com um ponto e
# pedimos para incluir busca com 0 ou n repetições através do *. depois repetimos o comando para a parte inicial para
# fechar a flag tomando cuidado de incluir uma barra como \/.


print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>', texto))
# saída: >>>['<p>Eita</p> <p>Qualquer frase</p> <p>Frase 3</p> <div> </div>']

# No entanto o comportamento ainda não é o desejado, porque ele não dividiu cada tag, pois a expressão regular é
# ambígua, já que existe vários locais na string que ocorre o mesmo padrão que estamos buscando.
# Isso é conhecido como comportamento 'guloso' dos quantificadores. porque mesmo que o padrão de encerramento seja
# achado, ele continua a busca no restante da string.

# Como podemos consertar isso?? Usando o sinal de interrogação ?, que avisa para o quantificador não se comportar de
# forma 'gulosa'. Separando a string pelo padrão de inicio e fim da nossa expressão regular.

print(re.findall(r'<[pdiv]{1,3}>.*?</[pdiv]{1,3}>', texto))
# saída: >>>['<p>Eita</p>', '<p>Qualquer frase</p>', '<p>Frase 3</p>', '<div> </div>']
print(re.findall(r'<[pdiv]{1,3}>.+?</[pdiv]{1,3}>', texto))







