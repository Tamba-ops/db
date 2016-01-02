USE DB_Tsyganov;

CREATE INDEX post_forum_date ON Post (Forum_short_name, date);
CREATE INDEX user_name_email ON User (name, email);
CREATE INDEX post_thread_date ON Post (thread, date);
CREATE INDEX post_user_date ON Post (User_email, date);

DROP INDEX fk_Post_Thread1_idx ON Post;
DROP INDEX fk_Post_User1_idx on Post;
DROP INDEX fk_Post_Forum1_idx ON Post;

CREATE INDEX follower_followee on Followers (Follower_email, Followee_email);
CREATE INDEX followee_follower on Followers (Followee_email, Follower_email);

CREATE INDEX thread_user_date ON Thread (User_email, date);
CREATE INDEX thread_forum_date ON Thread (Forum_short_name, date);