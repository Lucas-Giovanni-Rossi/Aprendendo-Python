# Programação Orientada a Objetos em Python

Anotações de estudo organizadas por fase.

## Fase 00 — Referências e conceitos iniciais

### Bibliografia recomendada

- **Documentação do site oficial:** Documentation → Non-English Docs.
- **Livros de Python:**
  - *Object-Oriented Python*.
  - *Python 3 — The Comprehensive Guide*.
- **Filme:** *Jogo da Imitação*.

### Autores importantes

| Nome                 | Anotações                                                                                                                   |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Alan M. Turing       | Pai da computação.                                                                                                          |
| Edsger Wybe Dijkstra | Discurso no Prêmio Turing: “Programar Humilde”.                                                                            |
| Kristen Nygaard      | Pai da OOP; criou a linguagem Simula.                                                                                         |
| Alan Curtis Kay      | Contribuiu para a evolução da OOP e para a criação da interface gráfica; criou a linguagem Smalltalk. Criador do laptop? |
| Guido van Rossum     | Criador da linguagem Python.                                                                                                  |

**Reconhecimento em destaque:** Prêmio Turing.

### Os quatro pilares da POO

| Pilar          | Ideia principal            |
| -------------- | -------------------------- |
| Abstração    | Capacidade de simplificar. |
| Encapsulamento | Proteção.                |
| Herança       | Conceito de hierarquia.    |
| Polimorfismo   | “Up em tudo”.            |

## Fase 01 — Introdução e evolução das linguagens

### Conceitos e siglas

- **POO:** Programação Orientada a Objetos.
- **OOP:** *Object-Oriented Programming*.
- **OOAD:** *Object-Oriented Analysis and Design*.
- **UML:** *Unified Modeling Language*.

A POO permite representar elementos do mundo real em sistemas computacionais. Esses elementos são representados como **objetos** (*objects*).

### Linha do tempo

#### 1950 — Linguagens de baixo nível

#### 1955 — Linguagens lineares

- `GOTO`: forçava um desvio no fluxo de execução.
- Edsger Wybe Dijkstra, indignado com as linguagens, contribuiu para a evolução das linguagens seguintes.

#### 1960 — Linguagens estruturadas

- *ALGOrithmic Language*.
- Crise do software na década de 1960.

> “A necessidade é a mãe da invenção.”
>
> — Platão

> “É preciso ter o caos dentro de si para dar à luz uma estrela dançante.”
>
> — Nietzsche

#### 1965 — Linguagens modulares

Em vez de um código grande, existem vários códigos menores e um principal.

#### 1970 — Linguagens orientadas a objetos

- Kristen Nygaard: patenteou o termo “Object”.
- Alan Curtis Kay: evento Dynabook na Xerox.

## Fase 02 — Benefícios da POO

**Mnemônico:** COMERNada.

| Característica         | Benefício                                                                                               |
| ----------------------- | -------------------------------------------------------------------------------------------------------- |
| **Confiável**    | O isolamento entre partes gera algo mais seguro. Ao alterar uma das partes, nenhuma outra é afetada.    |
| **Oportuno**      | Ao dividir tudo em partes, cada uma delas pode ser desenvolvida em paralelo.                             |
| **Manutenível**  | Atualizar é mais fácil. Uma pequena alteração beneficia todas as partes relacionadas.                |
| **Extensível**   | O sistema não é estático. Tudo deve mudar e crescer para permanecer útil.                            |
| **Reutilizável** | Objetos criados para um sistema podem ser aproveitados em outros sistemas.                               |
| **Natural**       | Mais fácil de entender, com maior atenção às funcionalidades do que aos detalhes de implementação. |

## Fase 03 — Classes, instâncias e objetos

### Classes

Classes são modelos que definem características para criar objetos.

1. **Nome da classe:** identifica o modelo.
2. **Atributos:** representam as características.
3. **Métodos:** representam as utilidades ou os comportamentos.

### Instância

**Instanciar:** ideia de transição, construção ou de “forjar” um objeto.

### Objetos

> “O objeto é a instância de uma classe.”
>
> — Guanabara

> “Objeto é uma coisa material ou abstrata que é feita a partir de um modelo e pode ser descrita por meio das suas características, comportamentos e estado atual.”
>
> — Guanabara

## Fases 04 a 06 — Mão na massa

Atividades práticas.

## Fase 07 — Herança: parte 1

- Itens superiores são os **ancestrais**.
- Itens descendentes herdam características dos ancestrais.

### Vantagens

- Reutilização de código.
- Organização hierárquica.
- Facilidade de manutenção.
- Extensibilidade.
- Suporte a polimorfismo.

## Fase 08 — Abstração

Abstrair é **ignorar o irrelevante e focar no essencial**.

**Exemplo:** não saber como o hardware do computador funciona não impede alguém de programar — ideia de interface pública.

### Vantagens

- Maior legibilidade.
- Padronização.
- Simplificação.
- Segurança.

## Fase 09 — Mão na massa

Atividades práticas.

## Fase 10 — Encapsulamento: parte 1

### Visibilidade

| Visibilidade              | Símbolo | Convenção em Python             |
| ------------------------- | -------- | --------------------------------- |
| Pública (*public*)     | `+`    | Sem prefixo.                      |
| Protegida (*protected*) | `#`    | Um sublinhado: `_atributo`.     |
| Privada (*private*)     | `-`    | Dois sublinhados: `__atributo`. |

**“Consenting adults”:** liberdade com responsabilidade.

## Fase 11 — Encapsulamento: parte 2

### Acesso a dados

- *Getters* e *setters*.
- Decorador `@property`.

## Fase 12 — Mão na massa

### Desafios

- [X] Implemente um termostato orientado a objeto
  - Minimo 16º  e Máximo de 30º
  - Inicial a 24º
  - Incremento de temperatudo de 0.5º
- [X] Simular um diário secreto orientado a objetos
  - So consegue ler com senha
- [X] Crie uma classe de hash SHA256 de uma senha
- [X] Crie um classe que represente um retângulo pelas medidas e área
- [ ] Aprimore o exercicio da ContaBancária, aplicando conceitos de encapsulamento.
- [ ] Implemente a seguinte estrutura de diagrama de classes
  - Cria "pessoa" como classe abstrata e classe filho como "aluno"
