import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'ai_student_impact_dataset.csv', delimiter=',')

colors_list = ['#ff7675', '#74b9ff', '#55efc4', '#ffeaa7', "#af5aa4"]
purple_pallet = sns.cubehelix_palette(8)

def mejor_category_students():
    plt.figure(figsize=(5, 4))
    bars = sns.countplot(y='Major_Category',
                         data=df, order=df['Major_Category'].value_counts().index,
                         hue='Major_Category',
                         palette=colors_list)

    plt.title('Qntd de alunos em cada área', pad=15, fontweight='bold')
    plt.xlabel('')
    plt.ylabel('')
    plt.xticks([])
    plt.grid(False)

    for spine in plt.gca().spines.values():
        spine.set_visible(False)

    for container in plt.gca().containers:
        plt.gca().bar_label(container, padding=3, fontsize=10, fontweight='bold')
    plt.show()

def proportion_category_students():
    proportions = df['Major_Category'].value_counts(normalize=True)
    fig, axes = plt.subplots(1, len(proportions), figsize=(14, 4))

    if len(proportions) == 1:
        axes = [axes]

    back_collor = '#dfe6e9'

    for i, (categoria, valor) in enumerate(proportions.items()):
        ax = axes[i]

        parts = [valor, 1 - valor]
        colors = [colors_list[i % len(colors_list)], back_collor]

        wedges, texts = ax.pie(parts, colors=colors, startangle=90,
                            wedgeprops=dict(width=0.3, edgecolor='white', linewidth=2))

        ax.text(0, 0, f"{valor*100:.1f}%", ha='center', va='center',
                fontsize=14, fontweight='bold')

        ax.set_title(categoria, fontsize=12, pad=10, fontweight='bold')

    plt.suptitle('Proporção em Relação ao Total de Pessoas', fontsize=16, y=1.05, fontweight='bold')
    plt.tight_layout()
    plt.show()

def gpa_frequency():
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    sns.histplot(
    data=df,
    x='Pre_Semester_GPA',
    bins=100,
    color='#af5aa4',
    edgecolor='black',
    kde=True,
    ax=axes[0])

    axes[0].set_title('GPA no Começo do Semestre', fontweight='bold', pad=10)
    axes[0].set_xlabel('GPA')
    axes[0].set_ylabel('Qtd de Estudantes')

    sns.histplot(
    data=df,
    x='Post_Semester_GPA',
    bins=100,
    color='#af5aa4',
    edgecolor='black',
    kde=True,
    ax=axes[1])

    axes[1].set_title('GPA ao Final do Semestre', fontweight='bold', pad=10)
    axes[1].set_xlabel('GPA')
    axes[1].set_ylabel('')

    for ax in axes:
        ax.grid(False)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

    plt.suptitle('Comparação de Desempenho: Antes vs. Depois', fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.show()

def weeky_hours_distribution():
    plt.figure(figsize=(5, 4))
    sns.boxplot(x='Major_Category',
                y='Weekly_GenAI_Hours',
                data=df, hue='Major_Category',
                palette=colors_list)

    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.title('Distribuição de Horas Semanais de Uso de IA por Curso', pad=20, fontsize=14, fontweight='bold')
    plt.xlabel('Categoria do Curso', labelpad=10)
    plt.ylabel('Horas Semanais', labelpad=10)

    plt.tight_layout()
    plt.show()

def traditionalStudy_hours_distribution():
    plt.figure(figsize=(5, 4))
    sns.boxplot(x='Major_Category',
                y='Traditional_Study_Hours',
                data=df, hue='Major_Category',
                palette=colors_list)

    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.title('Distribuição de Horas Semanais Estudando por métodos tradicionais', pad=20, fontsize=14, fontweight='bold')
    plt.xlabel('Categoria do Curso', labelpad=10)
    plt.ylabel('Horas Semanais', labelpad=10)

    plt.tight_layout()
    plt.show()

def institutional_policy():
    plt.figure(figsize=(5, 4))
    bars = sns.countplot(y='Institutional_Policy',
                         data=df, order=df['Institutional_Policy'].value_counts().index,
                         hue='Institutional_Policy',
                         palette=['#56145b', '#ffb9ff', '#b059b1'])

    plt.title('Posição da instituição em relação a I.A', pad=15, fontweight='bold')
    plt.xlabel('')
    plt.ylabel('')
    plt.xticks([])
    plt.grid(False)

    for spine in plt.gca().spines.values():
        spine.set_visible(False)

    for container in plt.gca().containers:
        plt.gca().bar_label(container, padding=3, fontsize=10, fontweight='bold')
    plt.show()

def paid_IA_subscription():
    plt.figure(figsize=(5, 4))
    counts = df['Paid_Subscription'].value_counts(normalize=True)
    wedges, texts, autotexts = plt.pie(
        counts,
        autopct='%1.1f%%',
        startangle=90,
        colors=['#fc8d62', '#66c2a5']
    )

    text_lgd = [f'{val} ({c})' for val, c in zip(counts.index, df['Paid_Subscription'].value_counts().values)]

    plt.legend(
        wedges,
        text_lgd,
        title='Qtd de assinantes',
        loc='center left',
        bbox_to_anchor=(0.9, 0),
        frameon=False
    )

    plt.setp(autotexts, size=10, weight="bold")
    plt.title('Proporção dos alunos que possuem assinatura em serviços de I.A', weight="bold")
    plt.show()

def prompt_engineering_skill():
    plt.figure(figsize=(5, 4))
    bars = sns.countplot(y='Prompt_Engineering_Skill',
                         data=df, order=df['Prompt_Engineering_Skill'].value_counts().index,
                         hue='Prompt_Engineering_Skill',
                         palette=['#56145b', '#ffb9ff', '#b059b1'])

    plt.title('Autoclassificação de engenharia de prompt', pad=15, fontweight='bold')
    plt.xlabel('')
    plt.ylabel('')
    plt.xticks([])
    plt.grid(False)

    for spine in plt.gca().spines.values():
        spine.set_visible(False)

    for container in plt.gca().containers:
        plt.gca().bar_label(container, padding=3, fontsize=10, fontweight='bold')
    plt.show()

def Primary_Use_Case():
    plt.figure(figsize=(5, 4))
    bars = sns.countplot(y='Primary_Use_Case',
                         data=df, order=df['Primary_Use_Case'].value_counts().index,
                         hue='Primary_Use_Case',
                         palette=purple_pallet)

    plt.title('Uso primário da I.A', pad=15, fontweight='bold')
    plt.xlabel('')
    plt.ylabel('')
    plt.xticks([])
    plt.grid(False)

    for spine in plt.gca().spines.values():
        spine.set_visible(False)

    for container in plt.gca().containers:
        plt.gca().bar_label(container, padding=3, fontsize=10, fontweight='bold')
    plt.show()

def perceived_ai_dependency():
    plt.figure(figsize=(9, 5))
    sns.histplot(
    data=df,
    x='Perceived_AI_Dependency',
    bins=10,
    color='#af5aa4',
    edgecolor='black')

    plt.title('Dependência perceptiva da I.A', fontweight='bold', pad=10)
    plt.xlabel('Nível de depenência de I.A')
    plt.ylabel('')

    plt.grid(False)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)

    plt.tight_layout()
    plt.show()

def anxiety_level_during_exams():
    plt.figure(figsize=(5, 4))
    sns.histplot(
    data=df,
    x='Anxiety_Level_During_Exams',
    bins=10,
    color='#af5aa4',
    edgecolor='black')

    plt.title('Pontuação de ansiedade durante os exames', fontweight='bold', pad=10)
    plt.xlabel('Nível de ansiedade')
    plt.ylabel('')

    plt.grid(False)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)

    plt.tight_layout()
    plt.show()

def bournout_risk_level():
    plt.figure(figsize=(5, 5))
    bars = sns.countplot(y='Burnout_Risk_Level',
                         data=df, order=df['Burnout_Risk_Level'].value_counts().index,
                         hue='Burnout_Risk_Level',
                         palette=['#ffb9ff', '#b059b1', '#56145b'],
                         )

    plt.title('Nível de risco de Burnout', pad=15, fontweight='bold')
    plt.xlabel('')
    plt.ylabel('')
    plt.xticks([])
    plt.grid(False)

    for spine in plt.gca().spines.values():
        spine.set_visible(False)

    for container in plt.gca().containers:
        plt.gca().bar_label(container, padding=3, fontsize=10, fontweight='bold')
    plt.show()

def skill_retention_score():
    plt.figure(figsize=(5, 4))
    sns.histplot(
    data=df,
    x='Skill_Retention_Score',
    bins=100,
    color='#af5aa4',
    edgecolor='black',
    kde=True,)

    plt.title('Retenção dos alunos ao final do semestre', fontweight='bold', pad=10)
    plt.xlabel('Nível de retenção de habilidade')
    plt.ylabel('')

    plt.grid(False)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)

    plt.tight_layout()
    plt.show()
