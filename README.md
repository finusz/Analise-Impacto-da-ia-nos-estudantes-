# Analise-do-dataset-Impacto-da-ia-nos-estudantes-

  Atualmente, a presença de agentes de inteligência artificais (I.A) estão se ploriferando cada vez mais na sociedade, seja no cotidiano; nas industrias e escritórios; ou em maios acadêmicos. Visando esse último cenário, realizo aqui uma analise que teve como o _dataset_ "Impact of Ai on Students", disponibilizado pelo usuário @laveshjadon. O _dataset_ apresenta dados que simulam a realidade de 50.000 (cinquenta mil) estudantes de diversas áreas de uma universidade X. A base de dados apresenta colunas com temas de: Identificador dos estudantes; Perfil acadêmico; Comportamento de uso da I.A; Comportamento de estudos; Contexto constitucional e Saúde mental.

  A analise foi feita utilizando a linguagem Python, com o auxilio das bibliotecas: Pandas para a extração e manipulação dos dados; Matplot.pyplot e Seaborn, para a criação dos visuais.

  Antes de falar do perfil dos estudantes e a relação deles com as I.A, é importante ressaltar a posição da instituição dos estudantes em relação ao uso da ferramenta. A maior parte dos estudantes alegam que são permitidos utilizarem I.A, porem devem citar o seu uso; Cerca de 15 mil alunos são encorajados a utilizarem a ferramenta e cerca de 10 mil tem a ferramente estritamente banida pela instituição.

<img width="507" height="390" alt="image" src="https://github.com/user-attachments/assets/26e16968-606b-4299-8b79-660878644c9c" />


  Dos dados fornecidos, a área com mais alunos é a STEM - sigla para "science, technology, engineering and maths" (Ciência, tecnologia, engenharia e matemática), com cerca de 15000 mil (quinze mill) estudantes, representando 30% do total; seguido por negócios com 12 mil estudantes, representando 1/4 to total. Esses dois cursos representam mais de 50% dos dados, a outra parcela é composta por estudantes de humanas (20%), medicina (13%) e artes (11.9%).

Figura 1.2 - Quantidade de alunos por curso

<img width="507" height="390" alt="image" src="https://github.com/user-attachments/assets/6ca83e38-9b16-4ecb-b85d-c1b2fd1e84a8" />

Autor: Elaboração própria

Figura 1.3 - Proporção de alunos por curso

<img width="1389" height="388" alt="image" src="https://github.com/user-attachments/assets/e9e7d42e-707d-4b61-a397-0d291ea372a6" />

Autor: Elaboração prória

  Tendo em mente como os estudantes estão distribuidos e quais são os maiores grupos apresentados, nota-se que majotoriamente os grupos com maiores populações são de exatas. E consequentemente, passamos a questionar se eles também são os que mais utilizando I.A, o que pode-se ser observado no boxblot a seguir, em que apresentam as maiores médias de horas semanais de utilização de I.A, como também os maiores pontos máximos (_Outliers_). E em comparação a métodos de estudos tradicionais, percebe-se que são os que tem as menores médias semanais de estudo tradicional.

Figura 1.4 - Distribuição de Horas Semanais de Uso de I.A por Curso

<img width="675" height="430" alt="image" src="https://github.com/user-attachments/assets/d0789b11-9f03-4325-b9b6-b24314d49cc9" />

Autor: Elaboração própria

Figura 1.5 - Distribuição de Horas Semanais Estudando por Métodos Tradicionais por Curso

<img width="675" height="430" alt="image" src="https://github.com/user-attachments/assets/732d8ae6-3989-470e-8c24-f387bf81ba3e" />

Autor: Elaboração própria

  Apesar de utilizarem I.A por longos periodos, e até estudando com ela mais que por métodos tradicionais, os estudantes não se percebem tão dependentes da ferramente, quando se auto classificaram numa escala de 1 a 10, os níveis ficaram principalmente focados entre 2 e 4, com poucas pessoas que se consideram extremamente dependentes.

<img width="490" height="390" alt="image" src="https://github.com/user-attachments/assets/1cc4c0a8-fd5b-43bf-93b7-8ae08097abef" />

  Também nota-se essa pouca dependência em alguns outros fatores, como o usu primário da I.A pelos estudantes, como se classificam como "engenheiros de prompt" e se possuem ou não assinatura em serviços fornecidos por inteligências artificiais. Esse que, um pouco menos da metade dos estudantes revelam tem algum tipo de assinatura (47.7%). 

<img width="507" height="388" alt="image" src="https://github.com/user-attachments/assets/8cd02945-0c5f-46ab-a58c-4ce248cbb5e1" />

   O nível de engenharia que os estudantes se classificam, a maioria diz estar entre iniciante e intermediário, enquanto um pouco mais de um quarto afirma estar no nível avançado. Quando observamos o uso primário da I.A está principalmente em depurações, escrita de redações/texto e criação de ideias, tendo menos foco em resumos e gerar a resposta diretamente. A I.A aparenta estar sendo mais utilizada como um apoio do que ferramenta principal, podendo justificar a pouco dependência que a maior parte dos alunos alegam ter.

<img width="507" height="390" alt="image" src="https://github.com/user-attachments/assets/eec48ef4-c68d-4a7b-a698-9f38a238daaa" /> <img width="507" height="390" alt="image" src="https://github.com/user-attachments/assets/96e7d0e7-66c5-47ef-ad5f-8d263a252edf" />

  Consequentemente quando analisamos a média geral (GPA) dos estudantes ao longo do semestre, vemos uma mudança significativa, com as notas ocilando de 3 a 4 — sendo 4 a nota máxima —, para estar majitoriamente concentrada na nota 4. Isso, obviamente, gera algumas dúvidas em retenção dos alunos e o quanto realmente estão aprendendo, porem, nos é apresentado que —numa escala de 1 a 100—, mesmo com o uso constante de I.A, a retenção dos estudantes é, de fato, alta, e quando vemos ela ao final do semestre, vemos que há dois pontos de concentração, o primeiro, menor, entre 60 e 80, e o maior de 100 com um pico alto de estudantes.

<img width="1389" height="515" alt="image" src="https://github.com/user-attachments/assets/d6249c95-0b71-478e-890f-bec122e8205f" />

<img width="560" height="515" alt="image" src="https://github.com/user-attachments/assets/e445b4fe-23e0-46b4-bf1f-db543d56c83e" />

  Ademais, vemos que, o nível de ansiedade, numa escala de 1 a 10, se concentra na média, oscilando de 3 a 5. E o risco de burnout também varia principalmente de médio a baixo entre os estudantes.

<img width="490" height="390" alt="image" src="https://github.com/user-attachments/assets/a2f6a67a-744b-42e8-b714-e2baff3862f1" />

<img width="507" height="390" alt="image" src="https://github.com/user-attachments/assets/37d5d237-b86a-45ae-bb66-0ab9cde2cad1" />

