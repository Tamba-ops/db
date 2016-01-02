# coding=utf-8

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

    'query_insert_follower': """INSERT INTO Followers SET
                                    Follower_email = %s,
                                    Followee_email = %s
                                  """,

    'query_delete_follower': """DELETE FROM Followers
                              WHERE Follower_email = %s and
                              Followee_email = %s""",

    'query_select_max_id_user': "SELECT LAST_INSERT_ID()",

    'query_select_user': "SELECT * FROM User WHERE email = %s",

    'query_followers_user': """SELECT Follower_email FROM Followers
                                    force index (followee_follower)
                                    WHERE Followee_email = %s
                                    ORDER BY Follower_email DESC""",

    'query_followers_user_full': """SELECT u.* FROM Followers
                                    JOIN User u ON Follower_email = email
                                    WHERE Followee_email = %s
                                    ORDER BY Follower_email DESC""",

    'query_following_user': """SELECT Followee_email FROM Followers
                                    force index (follower_followee)
                                    WHERE Follower_email = %s
                                    ORDER BY Followee_email DESC""",

    'query_following_user_full': """SELECT u.* FROM Followers
                                    JOIN User u ON Followee_email = email
                                    WHERE Follower_email = %s
                                    ORDER BY Followee_email DESC""",

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

    'query_select_max_id_forum': "SELECT LAST_INSERT_ID()",

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

    'query_select_max_id_thread': "SELECT LAST_INSERT_ID()",

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
                                    isDeleted = FALSE
                                    WHERE id = %s""",

    'query_subscriptions_insert': """INSERT INTO Subscriptions
                                      SET
                                      User_email = %s,
                                      Thread_id = %s""",
    'query_subscriptions_delete': """DELETE FROM Subscriptions
                                      WHERE
                                      User_email = %s AND
                                      Thread_id = %s""",

    'query_list_threads_forum': """SELECT * FROM Thread
                                    WHERE Forum_short_name = %s
                                    ORDER BY date DESC""",

    'query_list_threads_user': """SELECT * FROM Thread
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

    'query_select_max_id_post': "SELECT LAST_INSERT_ID()",

    'query_list_posts_forum': """SELECT * FROM Post
                                  WHERE Forum_short_name = %s
                                  ORDER BY date DESC
                                """,

    'query_list_posts_user': """SELECT * FROM Post p
                                  WHERE p.User_email = %s
                                  ORDER BY date DESC
                                """,

    'query_list_posts_thread': """SELECT * FROM Post
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
                                    isDeleted = FALSE
                                    WHERE id = %s""",

    'query_update_post': """UPDATE Post
                            SET
                            message = %s
                            WHERE id = %s""",

    'query_list_users_forum': """SELECT u.* FROM Post p
                                  JOIN User u ON u.email = p.User_email
                                  WHERE p.Forum_short_name = %s
                                  GROUP BY u.name DESC
                                """,

    'query_post_mpath': "SELECT mpath FROM Post WHERE id = %s",

    'query_count_post_in_tree': "SELECT count(*) FROM Post WHERE mpath LIKE %s",

    'query_delete': "TRUNCATE TABLE ",

    'query_count_post': "SELECT count(*) FROM Post",

    'query_count_user': "SELECT count(*) FROM User",

    'query_count_thread': "SELECT count(*) FROM Thread",

    'query_count_forum': "SELECT count(*) FROM Forum",

    'query_change_foreign_check': 'SET foreign_key_checks = %s',

    'query_find_id_of_parent': 'SELECT id FROM Post WHERE mpath LIKE %s',

    'query_count_posts_in_thread': 'SELECT count(*) FROM Post WHERE thread = %s and isDeleted = FALSE',

    'query_post_points': 'SELECT cast(likes AS signed) - cast(dislikes AS signed) likes FROM Post WHERE id = %s',

    'query_thread_points': 'SELECT cast(likes AS signed) - cast(dislikes AS signed) likes FROM Thread WHERE id = %s',

    'query_count_user_subscriptions': """SELECT Thread_id FROM Subscriptions
                                          WHERE User_email = %s""",

    'query_remove_posts_in_deleted_thread': """UPDATE Post
                                            SET
                                            isDeleted = TRUE
                                            WHERE thread = %s
                                            """,

    'query_restore_posts_in_deleted_thread': """UPDATE Post
                                            SET
                                            isDeleted = FALSE
                                            WHERE thread = %s
                                            """,
}

__author__ = 'root'
