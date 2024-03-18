import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from data import *

methodologies = {
    'MSF': {
        'matrix': msf_matrix,
        'roles': msf_roles
    },
    'XP': {
        'matrix': xp_matrix,
        'roles': xp_roles
    },
    'DSMS': {
        'matrix': dsms_matrix,
        'roles': dsms_roles
    },
    'OpenUP': {
        'matrix': openup_matrix,
        'roles': openup_roles
    }
}


# Оцінки компетенцій кандидатів (приклад)
candidate_scores_default = np.array([
    [0.8, 0.7, 0.9, 0.7, 0.6, 0.5, 0.8, 0.9, 0.7, 0.8],  # Кандидат 1
])
candidate_scores_default_dsms = np.array([
    [0.8, 0.7, 0.9, 0.7, 0.6, 0.5, 0.8, 0.9, 0.7, 0.8, 0.7, 0.9],  # Кандидат 1
])



def max_min_composition(candidate, roles):
    min_scores = np.minimum(candidate[:, np.newaxis, :], roles[np.newaxis, :, :])
    # Обчислення максимальних з мінімальних оцінок для кожного кандидата по ролях
    max_min_scores = np.max(min_scores, axis=2)
    return max_min_scores


# Streamlit user interface
st.title("Аналіз відповідності кандидатів до ролей")

selected_methodology = st.selectbox(
    'Виберіть методологію',
    list(methodologies.keys())  # Display the keys (methodology names) as options
)

# Get the matrix and role names for the selected methodology
role_requirements = np.array(methodologies[selected_methodology]['matrix'])
role_names = methodologies[selected_methodology]['roles']

st.subheader("Оцінки кандидата")
candidate_scores = st.data_editor(candidate_scores_default_dsms) if selected_methodology == "DSMS" else st.data_editor(candidate_scores_default)

st.subheader("Оцінки вимог до ролей у проекті, взяті з таблиці MSF")
df_role_requirements = pd.DataFrame(role_requirements, index=role_names)
st.dataframe(df_role_requirements)

max_min_scores = max_min_composition(candidate_scores, role_requirements)

st.subheader("Максимально-мінімальні оцінки відповідності кандидата до ролей")
st.write(pd.DataFrame(max_min_scores, columns=role_names))

# Гістограма
st.subheader('Гістограма оцінок відповідності кандидата до ролей')
fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(range(role_requirements.shape[0]), max_min_scores[0])
ax.set_xlabel('Роль')
ax.set_ylabel('Оцінка відповідності')
ax.set_title('Гістограма оцінок відповідності кандидата до ролей')
ax.set_xticks(range(role_requirements.shape[0]))
ax.set_xticklabels(role_names, rotation=45)
st.pyplot(fig)

# Лінійчаста діаграма
st.subheader('Лінійчаста діаграма оцінок відповідності кандидата до ролей')
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(range(role_requirements.shape[0]), max_min_scores[0], marker='o', linestyle='-')
ax.set_xlabel('Роль')
ax.set_ylabel('Оцінка відповідності')
ax.set_title('Лінійчаста діаграма оцінок відповідності кандидата до ролей')
ax.set_xticks(range(role_requirements.shape[0]))
ax.set_xticklabels(role_names, rotation=45)
ax.grid(True, which='both', linestyle='--', linewidth=0.5, color='grey')
st.pyplot(fig)

# Секторна діаграма
st.header('Секторна діаграма оцінок відповідності кандидата до ролей')
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(max_min_scores[0], labels=role_names, autopct='%1.1f%%', startangle=140)
ax.set_title('Секторна діаграма оцінок відповідності кандидата до ролей')
st.pyplot(fig)
