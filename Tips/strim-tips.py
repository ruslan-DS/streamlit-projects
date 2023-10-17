import pandas as pd
import streamlit as st
import numpy as np
import openai

st.set_page_config(layout='wide')

st.write(
    """
# Анализ DataSet **"Tips"** для создания портрета гостя кофейного заведения.

    """
)

tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

#ДОБАВЛЕНИЕ CHATGPT НА САЙТ ЧЕРЕЗ API, ЧТОБЫ СОЗДАТЬ ПОРТРЕТ ГОСТЯ НА ОСНОВЕ ТЕЗИСОВ - В РАЗРАБОТКЕ
# openai.api_key = "OPEN-API-KEY"
#
st.sidebar.info('Перед тем, как создать портрет гостя, изучите исследование, которое было проведено на этой странице!')
user_input = st.sidebar.text_input("You:")
#
# if user_input:
#     response = openai.Completion.create(
#         engine="davinci",
#         prompt=f"You say: {user_input}\nChatGPT:",
#         max_tokens=50
#     )
#
#     st.text("ChatGPT: " + response)



# Как влияет привычка курения гостя на средний чек гостя
st.subheader('1. Влияние привычки курения гостя на общий счет.', divider='blue')
smoker_variable = pd.DataFrame(
    {
        'Yes': tips[tips['smoker'] == 'Yes']['total_bill'].dropna().reset_index(drop=True),
        'No': tips[tips['smoker'] == 'No']['total_bill'].dropna().reset_index(drop=True)
    }
)

mean_smoker = tips.groupby('smoker', as_index=False)['total_bill'].mean()

st.line_chart(smoker_variable, color=["#0000FF", "#FF0000"])
st.info(f'Средний чек гостя, который: \n'
        f'- Курит: {round(smoker_variable["Yes"].mean(), 2)}$ \n'
        f'- Не курит: {round(smoker_variable["No"].mean(), 2)}$')



# В какой период дня (Lunch/Dinner) кафе получает наибольший доход
st.subheader('2. В какой части рабочего дня кафе получает наибольший доход?', divider='blue')

part_day = pd.DataFrame({
    'Lunch': tips[tips['time'] == 'Lunch']['total_bill'].dropna().reset_index(drop=True),
    'Dinner': tips[tips['time'] == 'Dinner']['total_bill'].dropna().reset_index(drop=True),
})

st.line_chart(part_day, color=["#0000FF", "#FF0000"])
st.info(f'Средняя цена чека в: \n'
        f'- Обед: {round(part_day["Lunch"].mean(), 2)} \n'
        f'- Ужин: {round(part_day["Dinner"].dropna().mean(), 2)}'
        )

# Гендреное различие и величина чека
st.subheader('3. Кто больше тратит денег в кафе, учитывая гендерное различие?', divider='blue')

gender_diff = pd.DataFrame(
    {
        'Male': tips[tips['sex'] == 'Male']['total_bill'].dropna().reset_index(drop=True),
        'Female': tips[tips['sex'] == 'Female']['total_bill'].dropna().reset_index(drop=True)
    }
)

st.line_chart(gender_diff, color=["#FF1493", "#0000FF"])
st.info(f'В среднем: \n'
        f'- Мужчины тратят: {round(gender_diff["Male"].mean(), 2)} \n'
        f'- Женищны тратят: {round(gender_diff["Female"].mean(), 2)}')




# Вопрос пользователю - "Опираясь на три предыдущих исследования (вопроса) определите, какой тип клиента подходит данному кафе больше всего?"
# Для этого используйте подключенный ChatGPT, который предоставлен внизу.
# Для облегчения выполнения данной задачи мы сформулируем три тезиса, которые были показаны нам с помощью трех вышеувиденных
# вопросов (исследований).
# 1. Если гость имеет привычку курить, значит средний чек его столика будет выше, чем у некурящего человека.
# 2. Основной период наибольшего получения прибыли яв-ся Dinner (ужин).
# 3. Тратят больше денег в кафе мужчины.

# ПРИМЕР ЗАПРОСА ДЛЯ chatGPT МОЖЕТ ВЫГЛЯДИТЬ ТАК:
# Учитывая три данных тезиса (перечислить), опиши наилучшие условия времени и портрет клиента, который сможет принести кафе
# наибольший доход.

# Получите ответ :)
