-- Active: 1691674992801@@127.0.0.1@3306@test_db
-- script that creates a stored procedure ComputeAverageWeightedScoreForUsers that 
-- computes and store the average weighted score for all students.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER $

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_weight FLOAT;
    DECLARE average_score FLOAT;
    DECLARE project_id INT;
    DECLARE project_score INT;
    DECLARE project_weight INT;
    DECLARE done INT DEFAULT FALSE;
    DECLARE cur CURSOR FOR SELECT project_id, score, weight FROM corrections JOIN projects ON corrections.project_id = projects.id WHERE user_id = user_id;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    SET total_score = 0;
    SET total_weight = 0;
    OPEN cur;
    read_loop: LOOP
        FETCH cur INTO project_id, project_score, project_weight;
        IF done THEN
            LEAVE read_loop;
        END IF;
        SET total_score = total_score + project_score * project_weight;
        SET total_weight = total_weight + project_weight;
    END LOOP;
    CLOSE cur;
    SET average_score = total_score / total_weight;
    UPDATE users SET average_score = average_score WHERE id = user_id;
END$

DELIMITER ;