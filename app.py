import streamlit as st
import numpy as np
import pandas as pd
import time

'''
# Where to start with your to dos?

Assign weights to your tasks and decide randomly which one to do next.
'''
list_with_weights = {}

with st.form(key='submit_tasks'):

    task_list = st.text_input('Enter what you want to do today (divided by comma)', 'Laundry, Groceries, Make dentist appointment')

    st.form_submit_button('Submit')

todolist = [x.strip() for x in task_list.split(',')]

for task in todolist:
    # f"You have left {20 - sum(list_with_weights.values())} points to assign to {len(todolist) - len(list_with_weights)} tasks."
    # if sum(list_with_weights.values()) == 20:
    #     list_with_weights[task] = st.slider(f'How important is {task}?', 0, 20, 0)
    if sum(list_with_weights.values()) < 20:
        list_with_weights[task] = st.slider(f'How important is {task} today?', 0, 20 - sum(list_with_weights.values(), 0))
    else:
        list_with_weights[task] = 0
        "You have reached the maximum weight of 20. The remaining tasks will be assigned a weight of 0."


with st.form("pick_method"):
    st.write("Now let's pick your task!")

    manual_or_automatic = st.radio('How to you want to pick your task?', ('Roll my own die', 'Roll the die for me'))

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit choice")

    twenty_numbers = np.arange(1,21)
    tasks_weights = []
    for key, value in list_with_weights.items():
        tasks_weights += [key] * value

    weighted_tasks = pd.DataFrame(twenty_numbers, columns=["Number"])
    weighted_tasks['Task'] = tasks_weights
    hdf = weighted_tasks.assign(hack='').set_index('hack')

    if submitted:
        if manual_or_automatic == 'Roll my own die':
            with st.spinner('Wait for it...'):
                time.sleep(1)
            st.success('Done!')
            hdf
        elif manual_or_automatic == 'Roll the die for me':
            with st.spinner('Rolling the die...'):
                time.sleep(1)
            todo = np.random.choice(tasks_weights)
            st.success(f'Your task is: {todo} 🎉')
            # st.write(f'Your task is: {todo}')


# st.header(f'Your task is: {todo}')
