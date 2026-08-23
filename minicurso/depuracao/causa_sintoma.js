// +---------------------------------------------+---------------------------+---------------------------------------------------------+-----------------------------------------------+
// | Sintoma                                     | Onde aparece              | Causa provável                                          | Onde está a causa                             |
// +---------------------------------------------+---------------------------+---------------------------------------------------------+-----------------------------------------------+
// | 1) TypeError adicionando valores em um loop | Dentro do loop            | input() resultado não convertido para int()              | A linha que lê a entrada do usuário,         |
// |                                             |                           |                                                         | antes do loop.                                |
// +---------------------------------------------+---------------------------+---------------------------------------------------------+-----------------------------------------------+
// | 2) O total final está errado por exatamente | O print() no final        | O loop começa no índice 1 em vez do índice 0.           | O cabeçalho do loop                           |
// | um item.                                    |                           |                                                         |                                               |
// +---------------------------------------------+---------------------------+---------------------------------------------------------+-----------------------------------------------+
// | 3) KeyError lendo de um dicionário          | O dicionário lê           | A chave nunca foi adicionada, ou foi adicionada com     | Anteriormente no programa em que o            |
// |                                             |                           | uma grafia diferente.                                   | dicionário foi construído                     |
// +---------------------------------------------+---------------------------+---------------------------------------------------------+-----------------------------------------------+
// | 4) A função retorna None em vez de um valor.| Onde o valor de retorno   | A função usa print() em vez de return                   | Dentro da definição da função                 |
// |                                             | é usado                   |                                                         |                                               |
// +---------------------------------------------+---------------------------+---------------------------------------------------------+-----------------------------------------------+
// | 5) A lista está vazia quando deveria conter | Onde a lista é lida       | Os itens foram adicionados a uma variável diferente     | Onde a lista estava sendo criada.             |
// | itens.                                      |                           | ou a lista foi redefinida dentro do loop.               |                                               |
// +---------------------------------------------+---------------------------+---------------------------------------------------------+-----------------------------------------------+
// Via: https://faq.computersciencewiki.org/index.php/intro/article/the-debugging-process

