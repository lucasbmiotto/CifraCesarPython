# CifraCesarPython 🐍
Esse Repositório é voltado para desenvolvimento e aplicação de um programa de encriptação em cifra de cesar.

A cifra de César é uma técnica simples de criptografia de substituição, que consiste em substituir cada letra do alfabeto por outra letra que esteja a um número fixo de posições à sua frente. Essa técnica foi nomeada em homenagem a Júlio César, que a teria usado para se comunicar com seus generais durante as Guerras Gálicas.

Por exemplo, se o número fixo for 3, a letra A seria substituída pela letra D, a letra B pela letra E e assim por diante. A tabela de substituição para esse exemplo seria a seguinte:

- A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
- D E F G H I J K L M N O P Q R S T U V W X Y Z A B C

Para usar a cifra de César, basta escolher um número fixo (chamado de "chave") e aplicá-lo a cada letra do texto que se deseja criptografar. Por exemplo, se quisermos criptografar a palavra "OLÁ", usando a chave 3, teríamos:

- O → R
- L → O
- Á → D

Assim, a palavra "OLÁ" se tornaria "ROD".

Para descriptografar o texto, basta aplicar a chave negativa (ou seja, se a chave usada na criptografia foi 3, a chave usada na descriptografia será -3) e fazer a substituição inversa das letras.

Embora a cifra de César seja uma técnica muito simples, ela é facilmente quebrável por meio de análise estatística do texto criptografado. Por essa razão, ela não é usada em aplicações de segurança modernas, mas ainda pode ser útil para fins didáticos ou de diversão.
