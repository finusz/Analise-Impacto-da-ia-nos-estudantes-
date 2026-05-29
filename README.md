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
| <img width="390" height="390" alt="image" src="https://github.com/user-attachments/assets/1cc4c0a8-fd5b-43bf-93b7-8ae08097abef" /> |
| *Autor: Elaboração própria* |

  Essa percepção dos estudantes pode ser pelas seguintes fatores comportamentais:
  * **Assinatura Paga:** Menos da metade dos estudantes (47.7%) possuem alguma assinatura em serviços de I.A, logo, possuem recursos limitados da ferramenta;
  * **Engenharia de Prompt:** A maioria se classifica como iniciante e intermediário, com apenas 27.6% (13809 estudantes) se classificando estando no nível avançado; 
  * **Casos de Uso Primários:** O principal foco de uso está no suporte, como depuração de código (debugging), escrita/rascunho de textos (copywriting) e geração de ideias (ideation). O uso para obter respostas diretas prontas ou resumos simples é minoritário. 

|Figura 3.1 - Proporção de alunos com assinatura em serviços I.A|
| :---: |
| <img width="560" height="515" src="https://github.com/user-attachments/assets/8cd02945-0c5f-46ab-a58c-4ce248cbb5e1" /> |
| *Autor: Elaboração própria* |

| Figura 3.2 - Auto Classificação de engenharia de Prompt | Figura 3.3 - Horas Semanais de Estudo Tradicional |
| :---: | :---: |
| <img width="507" height="390" alt="image" src="https://github.com/user-attachments/assets/eec48ef4-c68d-4a7b-a698-9f38a238daaa" /> | <img width="507" height="390" alt="image" src="https://github.com/user-attachments/assets/96e7d0e7-66c5-47ef-ad5f-8d263a252edf" /> |
| *Autor: Elaboração própria* | *Autor: Elaboração própria* |

---

## 4. Impacto Acadêmico e Saúde Mental

  Ao analisar a média ponderada geral (GPA) dos estudantes ao longo do semestre, vemos uma mudança significativa. As notas que oscilavam de 3.0 a 4.0, passaram a se concetrar na noxa máxima (4.0) ao fim do semestre. Essa mudança pode gerar dúvidas sobre a retenção dos alunos e o quanto estão aprendendo. Porem, as méticas de retenção de habilidad idicam dois pontos de acumulos: um intermediário (entre 60 a 80) e um pico massivo próximo a pontuação máxima (100).

|Figura 4.1 - Comparação do GPA ao começo e final do semestre|
| :---: |
| <img width="1389" height="515" alt="image" src="https://github.com/user-attachments/assets/d6249c95-0b71-478e-890f-bec122e8205f" /> |
| *Autor: Elaboração própria* |

|Figura 4.2 - Retenção dos alunos ao final do semestres|
| :---: |
| <img width="560" height="515" alt="image" src="https://github.com/user-attachments/assets/e445b4fe-23e0-46b4-bf1f-db543d56c83e" /> |
| *Autor: Elaboração própria* |

 Por fim, analisando o uso da tecnologia com os indicadores psicológicos, nota-se estabilidade:
* O nível de ansiedade durante os exames (escala de 1 a 10) mantém-se controlado na média, oscilando entre 3 e 5.
* O risco de burnout entre os estudantes varia predominantemente entre os níveis baixo e médio.

|Figura 4.3 - Pontuação de ansiedade durante os exames | Figura 4.4 - Nível de Risco de Burnout|
| :---: | :---: |
| <img width="490" height="390" alt="image" src="https://github.com/user-attachments/assets/a2f6a67a-744b-42e8-b714-e2baff3862f1" />| <img width="507" height="390" alt="image" src="https://github.com/user-attachments/assets/37d5d237-b86a-45ae-bb66-0ab9cde2cad1" /> |
| *Autor: Elaboração própria* | *Autor: Elaboração própria* |

---
