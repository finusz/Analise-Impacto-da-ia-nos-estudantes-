# O impacto da inteligencia artifical na vida academica dos estudantes.

  Atualmente, a presença de agentes de inteligência artificais (I.A) estão se ploriferando cada vez mais na sociedade, seja no cotidiano; nas industrias e escritórios; ou em maios acadêmicos. Visando esse último cenário, realizo aqui uma analise que teve como o _dataset_ "Impact of Ai on Students", disponibilizado pelo usuário @laveshjadon.
  
  O _dataset_ apresenta dados que simulam a realidade de **50.000 estudantes** de diversas áreas de insituições de ensino fictícias. Apresentando dados como:
  * Identificador dos estudantes;
  * Perfil acadêmico;
  * Comportamento de uso da I.A;
  * Comportamento de estudos;
  * Contexto constitucional;
  * Saúde mental.

### Metodologia
  A analise foi realizada inteiramente utilizando a linguagem Python em conjunto com as seguintes bibliotecas:
  * **Pandas:** para a extração e manipulação dos dados;
  * **Matplot.pyplot e Seaborn:** para a criação dos visuais e gráficos mais simples.

---

## 1. Perfil dos estudantes e conexto constitucional 

  Antes de avaliar o comportamento dos estudantes, é importante ressaltar a posição da instituição dos estudantes em relação ao uso da ferramenta. A maior parte dos estudantes alegam que são permitidos utilizarem I.A, porem devem citar o seu uso; Cerca de 15 mil alunos são encorajados a utilizarem a ferramenta e cerca de 10 mil tem a ferramente estritamente banida pela instituição.

| Figura 1.1 -  Posição da instituição em relação a I.A|
| :---: |
| <img width="507" height="390" alt="image" src="https://github.com/user-attachments/assets/26e16968-606b-4299-8b79-660878644c9c" /> |
| *Autor: Elaboração própria* |

  Dos estudantes analisados, a area de estudos deles foram dividos em 5, sendo elas: 
  * **STEM (Ciência, tecnologia, engenharia e matemática):** 15059 estudantes (30%);
  * **Business:** 12538 estudantes (24%);
  * **Humanas:** 9994 estudantes(20%);
  * **medicina:** 6476 estudantes (13%);
  * **Artes:** 5933 estudantes (11.9%).

  STEM e Business representam mais da metade da população apresentada, sendo os dois grupos com mais estudantes.

| Figura 1.2 - Quantidade de alunos por curso |
| :---: |
| <img width="507" height="390" alt="image" src="https://github.com/user-attachments/assets/6ca83e38-9b16-4ecb-b85d-c1b2fd1e84a8" /> |
| *Autor: Elaboração própria* |

|Figura 1.3 - Proporção de alunos por curso|
| :---: |
| <img width="1389" height="388" alt="image" src="https://github.com/user-attachments/assets/e9e7d42e-707d-4b61-a397-0d291ea372a6" /> |
| *Autor: Elaboração própria* |

---

## 2. Consumo de I.A x Estudo Tradicional

  Tendo em mente como os estudantes estão distribuidos e a maior presença de estudantes de exatas. Pode-se observar no boxplot a seguir que eles são os que mais utilizando I.A semanalmente, como também possuem os maiores pontos máximos (_Outliers_).
  Em comparação a métodos de estudos tradicionais, percebe-se que são os que possuem as menores médias semanais de estudo tradicional, possivelmente causada pela transição da metodologia de aprendizado.

| Figura 2.1 - Horas Semanais de Uso de I.A | Figura 2.2 - Horas Semanais de Estudo Tradicional |
| :---: | :---: |
| <img width="675" height="430" alt="Uso de IA por curso" src="https://github.com/user-attachments/assets/d0789b11-9f03-4325-b9b6-b24314d49cc9" /> | <img width="675" height="430" alt="Estudo tradicional por curso" src="https://github.com/user-attachments/assets/732d8ae6-3989-470e-8c24-f387bf81ba3e" /> |
| *Autor: Elaboração própria* | *Autor: Elaboração própria* |

---

## 3. Nível de Dependência e Adoção da Tecnologia

  Apesar de utilizarem I.A por longos periodos, os estudantes não se percebem dependentes da ferramente. Em uma autoavaliação de 1 a 10, as respostas ficaram concentradas entre os níveis 2 e 4, com poucos relatos de dependência extrema.


|Figura 3.1 - Proporção de alunos por curso|
| :---: |
| <img width="490" height="390" alt="image" src="https://github.com/user-attachments/assets/1cc4c0a8-fd5b-43bf-93b7-8ae08097abef" /> |
| *Autor: Elaboração própria* |

  Essa percepção dos estudantes pode ser pelas seguintes fatores comportamentais:
  * **Assinatura Paga:** Menos da metade dos estudantes (47.7%) possuem alguma assinatura em serviços de I.A, logo, possuem recursos limitados da ferramenta;
  * **Engenharia de Prompt:** A maioria se classifica como iniciante e intermediário, com apenas 27.6% (13809 estudantes) se classificando estando no nível avançado; 
  * **Casos de Uso Primários:** O principal foco de uso está no suporte, como depuração de código (debugging), escrita/rascunho de textos (copywriting) e geração de ideias (ideation). O uso para obter respostas diretas prontas ou resumos simples é minoritário. 

<p id="combos-uso" align="center">
  <img width="45%" src="https://github.com/user-attachments/assets/8cd02945-0c5f-46ab-a58c-4ce248cbb5e1" />
</p>

| Figura 3.2 - Auto Classificação de engenharia de Prompt | Figura 3.3 - Horas Semanais de Estudo Tradicional |
| :---: | :---: |
| <img width="507" height="390" alt="image" src="https://github.com/user-attachments/assets/eec48ef4-c68d-4a7b-a698-9f38a238daaa" /> | <img width="507" height="390" alt="image" src="https://github.com/user-attachments/assets/96e7d0e7-66c5-47ef-ad5f-8d263a252edf" /> |
| *Autor: Elaboração própria* | *Autor: Elaboração própria* |

  Consequentemente quando analisamos a média geral (GPA) dos estudantes ao longo do semestre, vemos uma mudança significativa, com as notas ocilando de 3 a 4 — sendo 4 a nota máxima —, para estar majitoriamente concentrada na nota 4. Isso, obviamente, gera algumas dúvidas em retenção dos alunos e o quanto realmente estão aprendendo, porem, nos é apresentado que —numa escala de 1 a 100—, mesmo com o uso constante de I.A, a retenção dos estudantes é, de fato, alta, e quando vemos ela ao final do semestre, vemos que há dois pontos de concentração, o primeiro, menor, entre 60 e 80, e o maior de 100 com um pico alto de estudantes.

<img width="1389" height="515" alt="image" src="https://github.com/user-attachments/assets/d6249c95-0b71-478e-890f-bec122e8205f" />

<img width="560" height="515" alt="image" src="https://github.com/user-attachments/assets/e445b4fe-23e0-46b4-bf1f-db543d56c83e" />

  Ademais, vemos que, o nível de ansiedade, numa escala de 1 a 10, se concentra na média, oscilando de 3 a 5. E o risco de burnout também varia principalmente de médio a baixo entre os estudantes.

<img width="490" height="390" alt="image" src="https://github.com/user-attachments/assets/a2f6a67a-744b-42e8-b714-e2baff3862f1" />

<img width="507" height="390" alt="image" src="https://github.com/user-attachments/assets/37d5d237-b86a-45ae-bb66-0ab9cde2cad1" />

