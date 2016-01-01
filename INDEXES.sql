CREATE INDEX post_forum_date ON Post (Forum_short_name, date);
CREATE INDEX user_name_email ON User (name, email);
CREATE INDEX post_thread_date ON Post (thread, date);
CREATE INDEX post_user_date ON Post (User_email, date);