import pandas as pd
import re


def preprocess(data):
    pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    df = pd.DataFrame({'user_message': messages, 'message_date': dates})
    # convert message_date type
    # Use a regular expression to remove the trailing hyphen and any surrounding whitespace
    df['message_date'] = df['message_date'].str.replace(r'\s*-\s*', '', regex=True) 
    # Fix the format string to match month before day
    df['message_date'] = pd.to_datetime(df['message_date'], format = 'mixed') 
    # Rename message_date column name to date column
    df.rename(columns = {'message_date': 'date'}, inplace = True)

    # Separate username and messages
    users = []
    messages = []

    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])
    
    
    df['user'] = users
    df['message'] = messages
    df.drop(columns = ['user_message'], inplace = True)

    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    df['month_num'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['only_date'] = df['date'].dt.date
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute
    df.drop(columns = ['date'], inplace = True)

    period = []
    
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    return df

