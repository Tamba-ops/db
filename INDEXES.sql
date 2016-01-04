USE DB_Tsyganov;

alter TABLE Post ADD COLUMN parent INTEGER;
ALTER TABLE Post MODIFY COLUMN parent INTEGER AFTER isSpam;

CREATE INDEX post_thread_date ON Post (thread, date);
CREATE INDEX post_user_date ON Post (User_email, date);
CREATE INDEX post_forum_email ON Post (Forum_short_name, User_email);

DROP INDEX fk_Post_Thread1_idx ON Post;
DROP INDEX fk_Post_User1_idx on Post;
DROP INDEX fk_Post_Forum1_idx ON Post;

CREATE INDEX follower_followee on Followers (Follower_email, Followee_email);
CREATE INDEX followee_follower on Followers (Followee_email, Follower_email);

CREATE INDEX thread_user_date ON Thread (User_email, date);
CREATE INDEX thread_forum_date ON Thread (Forum_short_name, date);

CREATE INDEX subscr_user_thread ON Subscriptions (User_email, Thread_id)