import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'ai_student_impact_dataset.csv', delimiter=',')

print(df.describe())
print(df.info())
colors_list = ['#ff7675', '#74b9ff', '#55efc4', '#ffeaa7', "#af5aa4"]


def mejor_category_students():
    bars = sns.countplot(y='Major_Category', data=df, order=df['Major_Category'].value_counts().index(), hue='Mejor_Category', palette=colors_list)
    plt.title('Qtd de alunos em cada área', pad=15, fontweight='bold')

    plt.xlabel('')
    plt.ylabel('')
    plt.xticks([])
    plt.grid(False)

    for spine in plt.gca().splines.values():
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
    plt.hist(df['Pre_Semester_GPA'], color='#af5aa4', edgecolor='bold')
    plt.title('Distribuição do GPA dos estudantes')
    plt.xlabel('')
    plt.ylabel('')

    plt.grid(False)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.show()

def weeky_hours_distribution():
    plt.hist(df['Weekly_GenAI_Hours'], color='#af5aa4', edgecolor='bold')
    plt.title('Distribuição das horas semanais de uso de I.A')
    plt.xlabel('')
    plt.ylabel('')

    plt.grid(False)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.show()

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

mejor_category_students()
gpa_frequency()
weeky_hours_distribution()
