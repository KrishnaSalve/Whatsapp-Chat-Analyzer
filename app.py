import streamlit as st
from preprocess import preprocess
from helper import fetch_stats, most_busy_users, create_wordcloud, most_common_words, emoji_count, monthly_timeline, daily_timeline, week_activity_map, month_activity_map, activity_heatmap
import matplotlib.pyplot as plt
import seaborn as sns # type: ignore

st.sidebar.title("Whatsapp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader('Choose a file')
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode('utf-8')
    df = preprocess(data)

    st.dataframe(df)


    # fetch unique users
    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,'Overall')

    selected_user = st.sidebar.selectbox('Show Analysis wrt', user_list)

    if st.sidebar.button('Show Analysis'):
        
        num_messages, words, num_media, num_links = fetch_stats(selected_user, df)

        st.title('Top Statistics')
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header('Total Messages')
            st.title(num_messages)
        with col2:
            st.header('Total Words')
            st.title(words)
        with col3:
            st.header('Total Media files')
            st.title(num_media)
        with col4:
            st.header('Total Links')
            st.title(num_links)


        # Monthly Timeline
        st.title('Monthly Timeline')
        timeline = monthly_timeline(selected_user, df)

        fig, ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'], color = 'green')
        plt.xticks(rotation = 'vertical')
        st.pyplot(fig)


        # Daily Timeline
        st.title('Daily Timeline')
        date_timeline = daily_timeline(selected_user, df)

        fig, ax = plt.subplots()
        ax.plot(date_timeline['only_date'], date_timeline['message'], color = 'black')
        plt.xticks(rotation = 'vertical')
        st.pyplot(fig)


        # Activity Map
        st.title('Activity Map')

        col1, col2 = st.columns(2)

        with col1:
            st.header('Most busy day')
            busy_day = week_activity_map(selected_user, df)

            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values)
            plt.xticks(rotation = 'vertical')
            st.pyplot(fig)

        with col2:
            st.header('Most busy Month')
            busy_month = month_activity_map(selected_user, df)

            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color = 'orange')
            plt.xticks(rotation = 'vertical')
            st.pyplot(fig)

        
        # Activity Heatmap
        st.title('Weekly Activity Map')
        user_heatmap = activity_heatmap(selected_user, df)

        fig, ax = plt.subplots()
        ax = sns.heatmap(user_heatmap)
        st.pyplot(fig)


        # finding the busiest users in the group(Group Level)
        if selected_user == 'Overall':

            st.title('Most Busy Users')
            busy, busiest = most_busy_users(df)
            fig, ax = plt.subplots()

            col1, col2 = st.columns(2)

            with col1:
                ax.bar(busy.index, busy.values, color = 'red')
                plt.xticks(rotation = 'vertical')
                st.pyplot(fig)
            with col2:
                st.dataframe(busiest)


        # WordCloud
        st.title('WordCloud')
        df_wc = create_wordcloud(selected_user, df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)


        # Most Common words
        st.title('Most Common Words')
        most_common_df = most_common_words(selected_user, df)

        st.dataframe(most_common_df)


        # Emoji Count
        st.title('Emoji Analysis')
        emoji_df = emoji_count(selected_user, df)

        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig, ax = plt.subplots()
            ax.pie(emoji_df['Count'].head(), labels = emoji_df['Emoji'].head(), autopct = '%0.2f')
        
            st.pyplot(fig)

