
queries = {
    'query_insert_user': """
            INSERT INTO
                User
            SET
                about = %s,
                email = %s,
                name = %s,
                username = %s
                """,

    'query_insert_follower': """INSERT INTO Followers (Follower_email, Followee_email)
                                  VALUES (%s, %s)""",

    'query_delete_follower': """DELETE FROM Followers
                              WHERE Follower_email = %s and
                              Followee_email = %s""",

    'query_select_max_id_user': "SELECT MAX(id) FROM User",


    'query_select_user': "SELECT * FROM User WHERE email = %s",

    'query_followers_user_desc': """SELECT u1.email from Followers f
                        INNER JOIN User u on
                        (u.email = f.Followee_email and u.email = %s)
                        INNER JOIN User u1 ON u1.email = f.Follower_email
                        ORDER BY u1.email DESC""",


    'query_followers_user_asc': """SELECT u1.email from Followers f
                        INNER JOIN User u on
                        (u.email = f.Followee_email and u.email = %s)
                        INNER JOIN User u1 ON u1.email = f.Follower_email
                        ORDER BY u1.email ASC""",

    'query_following_user_desc': """SELECT u1.email from Followers f
                        INNER JOIN User u on
                        (u.email = f.Follower_email and u.email = %s)
                        INNER JOIN User u1 ON u1.email = f.Followee_email
                        ORDER BY u1.email DESC""",

    'query_following_user_asc': """SELECT u1.email from Followers f
                        INNER JOIN User u on
                        (u.email = f.Follower_email and u.email = %s)
                        INNER JOIN User u1 ON u1.email = f.Followee_email
                        ORDER BY u1.email ASC""",

    'query_update_user': """UPDATE User
                        SET name = %s, about = %s
                        WHERE email = %s""",

    'query_insert_forum': """INSERT INTO
                            Forum
                          SET
                            name = %s,
                            short_name = %s,
                            User_email = %s
                          """,

    'query_select_max_id_forum': "SELECT Max(id) FROM Forum",

    'query_select_forum': "SELECT * FROM Forum WHERE short_name = %s",

    'query_insert_thread': """INSERT INTO
                                Thread
                                SET
                                date = %s,
                                isClosed = %s,
                                message = %s,
                                slug = %s,
                                title = %s,
                                User_email = %s,
                                Forum_short_name = %s
                              """,

    'query_select_max_id_thread': "SELECT Max(id) FROM Thread",

    'query_select_thread': "SELECT * FROM Thread WHERE id = %s",

    'query_update_thread_close': """UPDATE Thread
                                    SET
                                    isClosed = TRUE
                                    WHERE id = %s""",

    'query_update_thread_open': """UPDATE Thread
                                    SET
                                    isClosed = FALSE
                                    WHERE id = %s""",

    'query_update_thread_remove': """UPDATE Thread
                                    SET
                                    isDeleted = TRUE
                                    WHERE id = %s""",

    'query_update_thread_restore': """UPDATE Thread
                                    SET
                                    isDeleted = TRUE
                                    WHERE id = %s""",

    'query_subscriptions_insert': """INSERT INTO Subscriptions
                                      SET
                                      User_email = %s,
                                      Thread_id = %s""",
    'query_subscriptions_delete': """DELETE FROM Subscriptions
                                      WHERE
                                      User_email = %s AND
                                      Thread_id = %s""",

    'query_list_threads_forum': """SELECT id FROM Thread
                                    WHERE Forum_short_name = %s
                                    ORDER BY date DESC""",

    'query_list_threads_user': """SELECT id FROM Thread
                                    WHERE User_email = %s
                                    ORDER BY date DESC""",
    'query_threads_like': """UPDATE Thread
                              SET
                              likes = likes + 1
                              WHERE id = %s""",
    'query_threads_dislike': """UPDATE Thread
                              SET
                              dislikes = dislikes + 1
                              WHERE id = %s""",
    'query_update_thread': """UPDATE Thread
                                SET
                                slug = %s,
                                message = %s
                                WHERE id = %s""",
    'query_insert_post': """INSERT INTO Post
                            SET
                            date = %s,
                            message = %s,
                            Forum_short_name = %s,
                            thread = %s,
                            User_email = %s,
                            mpath = %s""",

    'query_select_post': "SELECT * FROM Post WHERE id = %s",

    'query_select_max_id_post': "SELECT max(id) FROM Post",

    'query_list_posts_forum': """SELECT id FROM Post
                                  WHERE Forum_short_name = %s
                                  ORDER BY date DESC
                                """,

    'query_list_posts_user': """SELECT id FROM Post
                                  WHERE User_email = %s
                                  ORDER BY date DESC
                                """,

    'query_list_posts_thread': """SELECT id FROM Post
                                  WHERE thread = %s
                                  ORDER BY date DESC
                                """,

    'query_posts_like': """UPDATE Post
                              SET
                              likes = likes + 1
                              WHERE id = %s""",
    'query_posts_dislike': """UPDATE Post
                              SET
                              dislikes = dislikes + 1
                              WHERE id = %s""",

    'query_update_post_remove': """UPDATE Post
                                    SET
                                    isDeleted = TRUE
                                    WHERE id = %s""",

    'query_update_post_restore': """UPDATE Post
                                    SET
                                    isDeleted = TRUE
                                    WHERE id = %s""",

    'query_update_post': """UPDATE Post
                            SET
                            message = %s
                            WHERE id = %s""",
    'query_list_users_forum': """SELECT u.email FROM Forum f
                                  JOIN Post p ON f.short_name = p.Forum_short_name
                                  AND Forum_short_name = %s
                                  JOIN User u ON u.email = f.User_email
                                  ORDER BY u.name DESC
                                """,

    'query_post_mpath': "SELECT mpath FROM Post WHERE id = %s",

    'query_count_post_in_tree': "SELECT count(*) FROM Post WHERE mpath LIKE %s",

    'query_delete': "DELETE FROM %s",

    'query_count_post': "SELECT count(*) FROM Post",

    'query_count_user': "SELECT count(*) FROM User",

    'query_count_thread': "SELECT count(*) FROM Thread",

    'query_count_forum': "SELECT count(*) FROM Forum",
}

__author__ = 'root'
