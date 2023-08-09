-- a trigger scripts that executes when a new row is inserted into the table

CREATE TRIGGER DECREASE_Q AFTER INSERT ON ORDERS FOR 
EACH ROW BEGIN UPDATE 
	UPDATE items
	SET
	    quantity = quantity - NEW.number
	WHERE name = NEW.item_name;
	END;
