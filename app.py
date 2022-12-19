import streamlit as st
import numpy as np
import pandas as pd
import time
import math

'''
# Where to start with your to dos?

Assign weights to your tasks and decide randomly which one to do next.
'''

## * Input tasks
list_with_weights_percent = {}

with st.form(key='submit_tasks'):
    task_list = st.text_input('Enter what you want to do today (divided by comma)',
                              'Laundry, Groceries, Make dentist appointment')
    st.form_submit_button('Submit')

todolist = [x.strip() for x in task_list.split(',')]


## * Assign weights in percent
for task in todolist:
    if sum(list_with_weights_percent.values()) < 100:
        list_with_weights_percent[task] = st.slider(f'How important is {task} today?',
                                            0, 100 - sum(list_with_weights_percent.values(), 0))
    else:
        list_with_weights_percent[task] = 0
        "You have reached the maximum weight of 20. The remaining tasks will be assigned a weight of 0."


## * Pick a task percent
st.write("Now let's pick your task!")
st.write("How to you want to pick your task?")

if st.checkbox('Roll my own die'):

    die_numbers = st.radio('How many sides does your die have?', (6, 10, 20))


    if st.button('Submit'):
        numbers_dice = np.arange(1, die_numbers + 1)
        tasks_weights_percent = []
        for key, value in list_with_weights_percent.items():
            tasks_weights_percent += [key] * math.ceil((value / 100) * die_numbers)
            print(key, value, tasks_weights_percent)

        if len(tasks_weights_percent) > die_numbers:
            tasks_weights_percent = tasks_weights_percent[:die_numbers]
            print(tasks_weights_percent)
            print(len(tasks_weights_percent))

        weighted_tasks = pd.DataFrame(numbers_dice, columns=["Number"])
        weighted_tasks['Task'] = tasks_weights_percent
        hidden_index_df = weighted_tasks.assign(hack='').set_index('hack')

        with st.spinner('Wait for it...'):
            time.sleep(1)
        st.success('Done!')
        hidden_index_df

if st.checkbox('Roll the die for me'):
    with st.spinner('Rolling the die...'):
        time.sleep(1)

        twenty_numbers = np.arange(1,101)
        tasks_weights_percent = []
        for key, value in list_with_weights_percent.items():
            tasks_weights_percent += [key] * value
    todo = np.random.choice(tasks_weights_percent)
    st.success(f'Your task is: {todo} 🎉')
