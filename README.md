# Analise-do-dataset-Impacto-da-ia-nos-estudantes-

  Atualmente, a presença de agentes de inteligência artificais estão se ploriferando cada vez mais na sociedade, seja no cotidiano; nas industrias e escritórios; ou em maios acadêmicos. Visando esse último cenário, realizo aqui uma analise que teve como o _dataset_ "Impact of Ai on Students", disponibilizado pelo usuário @laveshjadon. O _dataset_ apresenta dados que simulam a realidade de 50.000 (cinquenta mil) estudantes de diversas áreas de uma universidade X. A base de dados apresenta colunas com temas de: Identificador dos estudantes; Perfil acadêmico; Comportamento de uso da I.A; Comportamento de estudos; Contexto constitucional e Saúde mental.

  A analise foi feita utilizando a linguagem Python, com o auxilio das bibliotecas: Pandas para a extração e manipulação dos dados; Matplot.pyplot e Seaborn, para a criação dos visuais.

  Dos dados fornecidos, a área com mais alunos é a STEM - sigla para "science, technology, engineering and maths" (Ciência, tecnologia, engenharia e matemática), com cerca de 15000 mil (quinze mill) estudantes, representando 30% do total; seguido por negócios com 12 mil (doze mil) estudantes, representando 1/4 to total. Esses dois cursos representam mais de 50% dos dados, a outra parcela é composta por estudantes de humanas (20%), medicina (13%) e artes (11.9%).

Figura 1.0 - Quantidade de alunos por curso

<img width="633" height="424" alt="image" src="https://github.com/user-attachments/assets/6ca83e38-9b16-4ecb-b85d-c1b2fd1e84a8" />

Autor: Elaboração própria

Figura 1.1 - Proporção de alunos por curso

<img width="1389" height="388" alt="image" src="https://github.com/user-attachments/assets/e9e7d42e-707d-4b61-a397-0d291ea372a6" />

Autor: Elaboração prória

  Tendo em mente como os estudantes estão distribuidos e quais são os maiores grupos apresentados, nota-se que majotoriamente os grupos com maiores populações são de exatas. E consequentemente, passamos a questionar se eles também são os que mais utilizando I.A, o que pode-se ser observado no boxblot a seguir, em que apresentam as maiores médias de horas semanais de utilização de I.A, como também os maiores pontos máximos (_Outliers_). E em comparação a métodos de estudos tradicionais, vemos que são os que tem a menores médias semanais.

Figura 1.2 - Distribuição de Horas Semanais de Uso de I.A por Curso

<img width="656" height="470" alt="image" src="https://github.com/user-attachments/assets/d0789b11-9f03-4325-b9b6-b24314d49cc9" />

Autor: Elaboração própria

Figura 1.3 - Distribuição de Horas Semanais Estudando por Métodos Tradicionais por Curso

<img width="775" height="470" alt="image" src="https://github.com/user-attachments/assets/732d8ae6-3989-470e-8c24-f387bf81ba3e" />

Autor: Elaboração própria
