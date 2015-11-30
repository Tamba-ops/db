DELIMITER //
  CREATE TRIGGER change_points_post BEFORE UPDATE ON Post
    FOR EACH ROW
      BEGIN
        IF new.likes > old.likes OR
          new.dislikes > old.dislikes THEN
          SET new.points = cast(new.likes as SIGNED) - cast(new.dislikes as SIGNED);
        END IF;
      END
//
DELIMITER ;


DELIMITER $$
CREATE TRIGGER change_posts_thread AFTER INSERT ON Post
FOR EACH ROW
  BEGIN
    UPDATE Thread
    SET posts = posts + 1
    WHERE id = new.thread;
  END
$$
DElIMITER ;