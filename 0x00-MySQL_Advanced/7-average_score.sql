-- stored procedure scripts that computes the average score of a student

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

DELIMITER $

CREATE PROCEDURE COMPUTEAVERAGESCOREFORUSER(IN USER_ID 
INT) BEGIN UPDATE 
	UPDATE users
	SET average_score = (
	        SELECT AVG(score)
	        FROM corrections
	        WHERE user_id = user_id
	    )
	WHERE id = user_id;
	END$ 


DELIMITER ;