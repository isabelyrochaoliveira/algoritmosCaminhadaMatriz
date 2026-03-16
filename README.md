# Algoritmos de Caminhada em Matriz (Trabalho de APR)

Este projeto foi desenvolvido como parte da disciplina de Algoritmos e Programação (APR). O objetivo é explorar diferentes estratégias de navegação em uma matriz 10x10 que representa um mapa de custos (Ilhas).

---

## 🚀 Sobre o Projeto

O programa permite que o usuário escolha entre três tipos de algoritmos para atravessar um mapa, partindo da coordenada **(9,0)** (canto inferior esquerdo) até a coordenada **(0,9)** (canto superior direito). O sistema calcula o custo acumulado com base nos valores de cada célula do mapa.

### Estratégias de Caminhada:
1.  **Caminhada Fixa:** Segue um padrão pré-definido alternando movimentos para a direita e para cima.
2.  **Caminhada Aleatória:** A cada passo, o algoritmo decide aleatoriamente entre subir ou ir para a direita, realizando 10 rodadas de teste.
3.  **Caminhada Gulosa (Greedy):** A cada passo, o algoritmo analisa as células adjacentes (cima e direita) e escolhe a de menor custo.

---

## 🛠️ Tecnologias Utilizadas
* **Python 3.x**
* Biblioteca `random` (para a caminhada aleatória)
* Biblioteca `copy` (para manipulação e exibição do mapa sem alterar os dados originais)

---

## 📊 Funcionalidades
* **Menu Interativo:** Seleção simples de algoritmos via console.
* **Visualização de Progresso:** O mapa é exibido a cada 5 passos, marcando o caminho percorrido com `0` para facilitar a visualização.
* **Cálculo de Custos:** Soma dinâmica do valor de cada célula visitada.
* **Múltiplos Cenários:** Configuração preparada para três "Ilhas" (mapas) diferentes.
